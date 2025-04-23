import os
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import cv2
from tensorflow.keras.models import Sequential #type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense #type: ignore
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def select_csv_file():
    """Prompt the user to select a CSV file using a file dialog."""
    root = tk.Tk()
    root.withdraw()  # hide root window
    csv_file = filedialog.askopenfilename(title="Select the CSV file", filetypes=[("CSV files", "*.csv")])
    if not csv_file:
        raise ValueError("No CSV file selected")
    return csv_file

def load_and_preprocess_data(csv_file):
    """Load and preprocess the data from the CSV file."""
    data = pd.read_csv(csv_file)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.set_index('timestamp', inplace=True)
    return data

def scale_data(data, column):
    """Scale the specified column of the data to the range 0-1."""
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data[column].values.reshape(-1, 1))
    return scaled_data, scaler

def split_data(scaled_data, train_ratio=0.8):
    """Split the scaled data into training and testing sets."""
    train_size = int(len(scaled_data) * train_ratio)
    train_data, test_data = scaled_data[:train_size], scaled_data[train_size:]
    return train_data, test_data

def prepare_data(data, window_size):
    """Prepare the data for the model by creating input-output pairs."""
    x, y = [], []
    for i in range(len(data) - window_size):
        x.append(data[i:i + window_size, 0])
        y.append(data[i + window_size, 0])
    return np.array(x), np.array(y)

def create_and_train_lr_model(x_train, y_train):
    """Create and train a Linear Regression model."""
    model = LinearRegression()
    model.fit(x_train, y_train)
    return model

def plot_stock_prices(data, y_test, predicted_stock_price, title):
    """Plot actual vs predicted stock prices using Plotly."""
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index[-len(y_test):], y=y_test.flatten(), mode='lines', name='Actual Price', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=data.index[-len(predicted_stock_price):], y=predicted_stock_price.flatten(), mode='lines', name='Predicted Price', line=dict(color='red')))
    fig.update_layout(title=title, xaxis_title="Time", yaxis_title="Price")
    fig.show()

def save_candlestick_charts(data, chart_image_dir, chart_window=50):
    """Save candlestick charts in chunks to the specified directory."""
    os.makedirs(chart_image_dir, exist_ok=True)
    for i in range(0, len(data) - chart_window, chart_window):
        chart_data = data.iloc[i:i + chart_window]
        fig = go.Figure(data=[go.Candlestick(x=chart_data.index,
                                             open=chart_data['Open'],
                                             high=chart_data['High'],
                                             low=chart_data['Low'],
                                             close=chart_data['Close'])])
        fig.update_layout(title=f"Candlestick Chart {i}", xaxis_title="Time", yaxis_title="Price")
        fig.write_image(f"{chart_image_dir}/chart_{i}.png")

def preprocess_image(img_path):
    """Preprocess an image for the CNN model."""
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64))
    return img

def create_and_train_cnn_model(X_train, y_train, X_test, y_test):
    """Create and train a CNN model."""
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(3, activation='softmax'))  # Adjust the number of output classes as needed
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))
    return model

def main():
    # Select and load the CSV file
    csv_file = select_csv_file()
    data = load_and_preprocess_data(csv_file)

    # Preprocess the data
    data_for_prediction = data[['open', 'high', 'low', 'close', 'volume']]
    scaled_data, scaler = scale_data(data_for_prediction, 'close')
    train_data, test_data = split_data(scaled_data)

    # Prepare data for the model
    window_size = 10
    x_train, y_train = prepare_data(train_data, window_size)
    x_test, y_test = prepare_data(test_data, window_size)
    x_train_lr = np.reshape(x_train, (x_train.shape[0], window_size))
    x_test_lr = np.reshape(x_test, (x_test.shape[0], window_size))

    # Create and train the Linear Regression model
    model_lr = create_and_train_lr_model(x_train_lr, y_train)

    # Predict stock prices using the trained model
    predicted_stock_price = model_lr.predict(x_test_lr)
    predicted_stock_price = scaler.inverse_transform(predicted_stock_price.reshape(-1, 1))
    y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

    # Plot actual vs predicted stock prices
    plot_stock_prices(data, y_test, predicted_stock_price, "Stock Price Prediction (CSV-Based)")

    # Save candlestick charts
    chart_image_dir = "chart_images"
    save_candlestick_charts(data_for_prediction, chart_image_dir)

    # Load and preprocess chart images
    image_files = os.listdir(chart_image_dir)
    X, y = [], []
    for img_file in image_files:
        img = preprocess_image(os.path.join(chart_image_dir, img_file))
        X.append(img)
        y.append(1)  # Dummy label, replace with actual labels if available
    X = np.array(X).reshape(-1, 64, 64, 1)
    y = np.array(y)

    # Split the image data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the CNN model
    model_cnn = create_and_train_cnn_model(X_train, y_train, X_test, y_test)

    # Evaluate the CNN model
    loss, accuracy = model_cnn.evaluate(X_test, y_test)
    print(f"Test Accuracy: {accuracy*100:.2f}%")

    # Predict stock prices up to a specified date and time
    target_date_str = input("Enter the target date and time (MM/DD/YYYY HH:MM:SS): ")
    target_date = datetime.strptime(target_date_str, "%m/%d/%Y %H:%M:%S")
    filtered_data = data[data.index <= target_date]
    scaled_filtered_data = scaler.transform(filtered_data['close'].values.reshape(-1, 1))
    x_filtered, _ = prepare_data(scaled_filtered_data, window_size)
    x_filtered_lr = np.reshape(x_filtered, (x_filtered.shape[0], window_size))
    predicted_filtered_stock_price = model_lr.predict(x_filtered_lr)
    predicted_filtered_stock_price = scaler.inverse_transform(predicted_filtered_stock_price.reshape(-1, 1))

    # Plot actual vs predicted stock prices with user-defined colors
    predicted_price_color = input("Enter the color for the predicted price line: ")
    actual_price_color = input("Enter the color for the actual price line: ")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered_data.index[-len(predicted_filtered_stock_price):], y=filtered_data['close'][-len(predicted_filtered_stock_price):], mode='lines', name='Actual Price', line=dict(color=actual_price_color)))
    fig.add_trace(go.Scatter(x=filtered_data.index[-len(predicted_filtered_stock_price):], y=predicted_filtered_stock_price.flatten(), mode='lines', name='Predicted Price', line=dict(color=predicted_price_color)))
    fig.update_layout(title=f"Stock Price Prediction up to {target_date_str}", xaxis_title="Time", yaxis_title="Price")
    fig.show()

if __name__ == "__main__":
    main()
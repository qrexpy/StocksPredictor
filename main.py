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

# create tk root window
root = tk.Tk()
root.withdraw()  # hide root window

# open file dialog to select csv file
csv_file = filedialog.askopenfilename(title="Select the CSV file", filetypes=[("CSV files", "*.csv")])

# Check if a file was selected
if not csv_file:
    raise ValueError("No CSV file selected")

# load csv file
data = pd.read_csv(csv_file)

# convert 'timestamp' to datetime and set it as index
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

# select columns for prediction
data_for_prediction = data[['open', 'high', 'low', 'close', 'volume']]

# scale 'close' prices to range 0-1
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data_for_prediction['close'].values.reshape(-1, 1))

# split data into training and testing (80% training, 20% testing)
train_size = int(len(scaled_data) * 0.8)
train_data, test_data = scaled_data[:train_size], scaled_data[train_size:]

# prepare data for the model
def prepare_data(data, window_size):
    x, y = [], []
    for i in range(len(data) - window_size):
        x.append(data[i:i + window_size, 0])
        y.append(data[i + window_size, 0])
    return np.array(x), np.array(y)

# set window size for the model
window_size = 10
x_train, y_train = prepare_data(train_data, window_size)
x_test, y_test = prepare_data(test_data, window_size)

# reshape data for the LR model
x_train_lr = np.reshape(x_train, (x_train.shape[0], window_size))
x_test_lr = np.reshape(x_test, (x_test.shape[0], window_size))

# create and train the LR model
model_lr = LinearRegression()
model_lr.fit(x_train_lr, y_train)

# predict stock prices using the trained model
predicted_stock_price = model_lr.predict(x_test_lr)

# transform the scaled data back to the original scale
predicted_stock_price = scaler.inverse_transform(predicted_stock_price.reshape(-1, 1))
y_test = scaler.inverse_transform(y_test.reshape(-1, 1))

# plot actual vs predicted stock prices using plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index[-len(y_test):], y=y_test.flatten(), mode='lines', name='Actual Price', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=data.index[-len(predicted_stock_price):], y=predicted_stock_price.flatten(), mode='lines', name='Predicted Price', line=dict(color='red')))
fig.update_layout(title="Stock Price Prediction (CSV-Based)", xaxis_title="Time", yaxis_title="Price")
fig.show()

# make directory for chart images
chart_image_dir = "chart_images"
os.makedirs(chart_image_dir, exist_ok=True)

# prepare data for creating candlestick charts
data_for_plot = data[['open', 'high', 'low', 'close', 'volume']]
data_for_plot.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# plot and save candlestick charts in chunks (50 data points)
chart_window = 50
for i in range(0, len(data_for_plot) - chart_window, chart_window):
    chart_data = data_for_plot.iloc[i:i + chart_window]
    fig = go.Figure(data=[go.Candlestick(x=chart_data.index,
                                         open=chart_data['Open'],
                                         high=chart_data['High'],
                                         low=chart_data['Low'],
                                         close=chart_data['Close'])])
    fig.update_layout(title=f"Candlestick Chart {i}", xaxis_title="Time", yaxis_title="Price")
    fig.write_image(f"{chart_image_dir}/chart_{i}.png")

# preprocess images for the CNN model
def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (64, 64))
    return img

# load and preprocess the chart images
image_files = os.listdir(chart_image_dir)
labels = []

X = []
y = []

for img_file in image_files:
    img = preprocess_image(os.path.join(chart_image_dir, img_file))
    X.append(img)
    y.append(1)  # Dummy label, replace with actual labels if available

# convert the image data to numpy arrays and reshape for the CNN model
X = np.array(X).reshape(-1, 64, 64, 1)
y = np.array(y)

# split the image data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create the CNN model
model_cnn = Sequential()
model_cnn.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 1)))
model_cnn.add(MaxPooling2D(pool_size=(2, 2)))
model_cnn.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model_cnn.add(MaxPooling2D(pool_size=(2, 2)))
model_cnn.add(Flatten())
model_cnn.add(Dense(128, activation='relu'))
model_cnn.add(Dense(3, activation='softmax'))  # Adjust the number of output classes as needed

# compile the CNN model
model_cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train the CNN model
model_cnn.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# evaluate the CNN model on the test data
loss, accuracy = model_cnn.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy*100:.2f}%")

# prompt the user to input a target date and time
target_date_str = input("Enter the target date and time (MM/DD/YYYY HH:MM:SS): ")
target_date = datetime.strptime(target_date_str, "%m/%d/%Y %H:%M:%S")

# filter the data up to the specified date and time
filtered_data = data[data.index <= target_date]

# prepare the data for prediction
scaled_filtered_data = scaler.transform(filtered_data['close'].values.reshape(-1, 1))
x_filtered, _ = prepare_data(scaled_filtered_data, window_size)

# reshape the data for the Linear Regression model
x_filtered_lr = np.reshape(x_filtered, (x_filtered.shape[0], window_size))

# predict stock prices using the trained model
predicted_filtered_stock_price = model_lr.predict(x_filtered_lr)

# transform the scaled data back to the original scale
predicted_filtered_stock_price = scaler.inverse_transform(predicted_filtered_stock_price.reshape(-1, 1))

# prompt the user to input colors for the predicted and actual prices
predicted_price_color = input("Enter the color for the predicted price line: ")
actual_price_color = input("Enter the color for the actual price line: ")

# plot the actual vs predicted stock prices up to the specified date and time with user-defined colors using plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=filtered_data.index[-len(predicted_filtered_stock_price):], y=filtered_data['close'][-len(predicted_filtered_stock_price):], mode='lines', name='Actual Price', line=dict(color=actual_price_color)))
fig.add_trace(go.Scatter(x=filtered_data.index[-len(predicted_filtered_stock_price):], y=predicted_filtered_stock_price.flatten(), mode='lines', name='Predicted Price', line=dict(color=predicted_price_color)))
fig.update_layout(title=f"Stock Price Prediction up to {target_date_str}", xaxis_title="Time", yaxis_title="Price")
fig.show()
import pandas as pd
import mplfinance as mpf
import os
import tkinter as tk
from tkinter import filedialog

# make window then hide it
root = tk.Tk()
root.withdraw()

# ask user to select a CSV file via file explorer
csv_file = filedialog.askopenfilename(
    title="Select a CSV file",
    filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
)

# read csv file user inserted
data = pd.read_csv(csv_file)

# convert timestamp to datetime and set it as index
data['timestamp'] = pd.to_datetime(data['timestamp'])
data.set_index('timestamp', inplace=True)

# make columns for plotting in chart
columns = ['open', 'high', 'low', 'close', 'volume']
data_for_plot = data[[col for col in columns if col in data.columns]]

# gives user the selected columns for plotting
print(f"Selected columns for plotting: {data_for_plot.columns.tolist()}")

# ask user to select a folder to save the chart
output_folder = filedialog.askdirectory(title="Select a folder to save the chart")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
output_folder = os.path.abspath(output_folder)

# generate output file name
output_png = os.path.join(output_folder, os.path.splitext(os.path.basename(csv_file))[0] + '_chart.png')

# ask user to select chart type and style
chart_type = input("""Type one of the types of the following:
- Candlestick chart (candle) <--- Default
- Open, High, Low, Close chart (ohlc) <---- Most used
- Line chart (line)
- Renko chart (renko)
- Point and Figure chart (pnf)
- Heikin-Ashi chart (heikinashi)
""")

chart_style = input("""Type one of the styles of the following:
- Default style (default)
- Classic style (classic)
- Mike style (mike)
- Charles style (charles)
- Yahoo style (yahoo) <--- Default
- Nightclouds style (nightclouds)
- SAS style (sas)
- Stars and Stripes style (starsandstripes)
- Brasil style (brasil)
- Blueskies style (blueskies)
- IBD style (ibd)
- Binance style (binance)
- Checkers style (checkers)
""")

# ask user to input chart title
usertitle = input("Enter the title of the chart: ")

# generate chart
mpf.plot(data_for_plot, type=chart_type, volume=True, style=chart_style, title=usertitle, 
         ylabel="Price", savefig=output_png)

# give user the path of saved chart
print(f"Chart saved as: {output_png}")

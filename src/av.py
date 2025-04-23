import sys
import requests
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QTabWidget, QComboBox, QFileDialog, QCheckBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class SymbolFinderApp(QMainWindow):
    """
    Main application class for the Alpha Vantage App.
    Provides functionality to search symbols and download CSV data using Alpha Vantage API.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alpha Vantage App")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #2e2e2e; color: #ffffff;")

        self.api_key = None

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tabs = self.create_tabs()
        self.layout.addWidget(self.tabs)

        self.api_key_tab = QWidget()
        self.symbol_search_tab = QWidget()
        self.download_csv_tab = QWidget()

        self.tabs.addTab(self.api_key_tab, "API Key")
        self.tabs.addTab(self.symbol_search_tab, "Symbol Search")
        self.tabs.addTab(self.download_csv_tab, "Download CSV")

        self.init_api_key_tab()
        self.init_symbol_search_tab()
        self.init_download_csv_tab()

    def create_tabs(self):
        """
        Creates and configures the tab widget for the application.
        """
        tabs = QTabWidget()
        tabs.setFont(QFont("Arial", 14))
        tabs.setStyleSheet("QTabWidget::pane { border: 1px solid #444; } QTabBar::tab { background: #444; color: #fff; padding: 10px; } QTabBar::tab:selected { background: #666; }")
        return tabs

    def init_api_key_tab(self):
        """
        Initializes the API Key tab with input field and save button.
        """
        layout = QVBoxLayout()

        label = QLabel("Enter Alpha Vantage API Key:")
        label.setFont(QFont("Arial", 14))
        layout.addWidget(label)

        self.api_key_input = QLineEdit()
        self.api_key_input.setFont(QFont("Arial", 14))
        layout.addWidget(self.api_key_input)

        save_button = QPushButton("Save API Key")
        save_button.setFont(QFont("Arial", 14))
        save_button.setStyleSheet("background-color: #4CAF50; color: white;")
        save_button.clicked.connect(self.save_api_key)
        layout.addWidget(save_button)

        self.api_key_tab.setLayout(layout)

    def save_api_key(self):
        """
        Saves the API key entered by the user.
        """
        self.api_key = self.api_key_input.text()
        print(f"API Key saved: {self.api_key}")

    def init_symbol_search_tab(self):
        """
        Initializes the Symbol Search tab with input field, search button, and result table.
        """
        layout = QVBoxLayout()

        label = QLabel("Enter Company/Currency Name:")
        label.setFont(QFont("Arial", 14))
        layout.addWidget(label)

        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 14))
        layout.addWidget(self.input_field)

        search_button = QPushButton("Search")
        search_button.setFont(QFont("Arial", 14))
        search_button.setStyleSheet("background-color: #4CAF50; color: white;")
        search_button.clicked.connect(self.search_symbol)
        layout.addWidget(search_button)

        self.result_table = self.create_result_table()
        layout.addWidget(self.result_table)

        self.symbol_search_tab.setLayout(layout)

    def create_result_table(self):
        """
        Creates and configures the result table for displaying search results.
        """
        table = QTableWidget()
        table.setFont(QFont("Arial", 12))
        table.setStyleSheet("""
            QTableWidget { background-color: #444; color: #fff; gridline-color: #666; }
            QHeaderView::section { background-color: #555; color: #fff; }
            QTableWidget::item { border: 1px solid #666; }
        """)
        return table

    def init_download_csv_tab(self):
        """
        Initializes the Download CSV tab with input fields, function selector, and download button.
        """
        layout = QVBoxLayout()

        label = QLabel("Enter Symbol:")
        label.setFont(QFont("Arial", 14))
        layout.addWidget(label)

        self.symbol_input = QLineEdit()
        self.symbol_input.setFont(QFont("Arial", 14))
        layout.addWidget(self.symbol_input)

        function_label = QLabel("Select Function:")
        function_label.setFont(QFont("Arial", 14))
        layout.addWidget(function_label)

        self.function_combo = self.create_function_combo()
        layout.addWidget(self.function_combo)

        self.parameters_layout = QVBoxLayout()
        layout.addLayout(self.parameters_layout)

        download_button = QPushButton("Download CSV")
        download_button.setFont(QFont("Arial", 14))
        download_button.setStyleSheet("background-color: #4CAF50; color: white;")
        download_button.clicked.connect(self.download_csv)
        layout.addWidget(download_button)

        self.download_csv_tab.setLayout(layout)
        self.update_parameters()

    def create_function_combo(self):
        """
        Creates and configures the function combo box for selecting API functions.
        """
        combo = QComboBox()
        combo.setFont(QFont("Arial", 14))
        combo.addItems([
            "TIME_SERIES_INTRADAY",
            "TIME_SERIES_DAILY",
            "TIME_SERIES_DAILY_ADJUSTED",
            "TIME_SERIES_WEEKLY",
            "TIME_SERIES_WEEKLY_ADJUSTED",
            "TIME_SERIES_MONTHLY",
            "TIME_SERIES_MONTHLY_ADJUSTED",
            "GLOBAL_QUOTE",
            "REALTIME_BULK_QUOTES"
        ])
        combo.currentTextChanged.connect(self.update_parameters)
        return combo

    def update_parameters(self):
        """
        Updates the parameters layout based on the selected function.
        """
        for i in reversed(range(self.parameters_layout.count())):
            widget = self.parameters_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        function = self.function_combo.currentText()
        if function == "TIME_SERIES_INTRADAY":
            self.add_intraday_parameters()
        elif function in ["TIME_SERIES_DAILY", "TIME_SERIES_DAILY_ADJUSTED"]:
            self.add_daily_parameters()
        elif function in ["TIME_SERIES_WEEKLY", "TIME_SERIES_WEEKLY_ADJUSTED", "TIME_SERIES_MONTHLY", "TIME_SERIES_MONTHLY_ADJUSTED"]:
            self.add_generic_parameters()
        elif function == "GLOBAL_QUOTE":
            self.add_generic_parameters()
        elif function == "REALTIME_BULK_QUOTES":
            self.add_bulk_quotes_parameters()
        else:
            self.symbol_input.setPlaceholderText("Enter Symbol")

    def add_intraday_parameters(self):
        """
        Adds parameters specific to TIME_SERIES_INTRADAY function.
        """
        self.interval_input = QLineEdit()
        self.interval_input.setPlaceholderText("Interval (e.g., 1min, 5min, 15min, 30min, 60min)")
        self.parameters_layout.addWidget(self.interval_input)

        self.adjusted_checkbox = QCheckBox("Adjusted")
        self.adjusted_checkbox.setChecked(True)
        self.parameters_layout.addWidget(self.adjusted_checkbox)

        self.extended_hours_checkbox = QCheckBox("Extended Hours")
        self.extended_hours_checkbox.setChecked(True)
        self.parameters_layout.addWidget(self.extended_hours_checkbox)

        self.month_input = QLineEdit()
        self.month_input.setPlaceholderText("Month (YYYY-MM)")
        self.parameters_layout.addWidget(self.month_input)

        self.outputsize_combo = QComboBox()
        self.outputsize_combo.addItems(["compact", "full"])
        self.parameters_layout.addWidget(self.outputsize_combo)

        self.datatype_combo = QComboBox()
        self.datatype_combo.addItems(["json", "csv"])
        self.parameters_layout.addWidget(self.datatype_combo)

    def add_daily_parameters(self):
        """
        Adds parameters specific to daily functions.
        """
        self.outputsize_combo = QComboBox()
        self.outputsize_combo.addItems(["compact", "full"])
        self.parameters_layout.addWidget(self.outputsize_combo)

        self.datatype_combo = QComboBox()
        self.datatype_combo.addItems(["json", "csv"])
        self.parameters_layout.addWidget(self.datatype_combo)

    def add_generic_parameters(self):
        """
        Adds generic parameters for weekly, monthly, and global quote functions.
        """
        self.datatype_combo = QComboBox()
        self.datatype_combo.addItems(["json", "csv"])
        self.parameters_layout.addWidget(self.datatype_combo)

    def add_bulk_quotes_parameters(self):
        """
        Adds parameters specific to REALTIME_BULK_QUOTES function.
        """
        self.symbol_input.setPlaceholderText("Enter up to 100 symbols separated by commas")
        self.datatype_combo = QComboBox()
        self.datatype_combo.addItems(["json", "csv"])
        self.parameters_layout.addWidget(self.datatype_combo)

    def search_symbol(self):
        """
        Searches for symbols using the Alpha Vantage API and displays results in the table.
        """
        if not self.api_key:
            print("API Key is not set.")
            return

        query = self.input_field.text()
        if query:
            url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={query}&apikey={self.api_key}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                self.populate_result_table(data)
            else:
                self.result_table.setRowCount(0)
                self.result_table.setColumnCount(0)

    def populate_result_table(self, data):
        """
        Populates the result table with search results.
        """
        if "bestMatches" in data:
            matches = data["bestMatches"]
            self.result_table.setRowCount(len(matches))
            self.result_table.setColumnCount(2)
            self.result_table.setHorizontalHeaderLabels(["Symbol", "Name"])
            for row, match in enumerate(matches):
                symbol_item = QTableWidgetItem(match["1. symbol"])
                name_item = QTableWidgetItem(match["2. name"])
                symbol_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                name_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.result_table.setItem(row, 0, symbol_item)
                self.result_table.setItem(row, 1, name_item)
        else:
            self.result_table.setRowCount(0)
            self.result_table.setColumnCount(0)

    def download_csv(self):
        """
        Downloads CSV data using the Alpha Vantage API based on user inputs.
        """
        if not self.api_key:
            print("API Key is not set.")
            return

        symbol = self.symbol_input.text()
        function = self.function_combo.currentText()
        if symbol and function:
            params = self.build_api_params(symbol, function)
            url = f"https://www.alphavantage.co/query"
            response = requests.get(url, params=params)
            self.save_csv(response)

    def build_api_params(self, symbol, function):
        """
        Builds the API parameters based on user inputs and selected function.
        """
        params = {
            "function": function,
            "symbol": symbol,
            "apikey": self.api_key,
            "datatype": "csv"
        }
        if function == "TIME_SERIES_INTRADAY":
            params["interval"] = self.interval_input.text()
            params["adjusted"] = str(self.adjusted_checkbox.isChecked()).lower()
            params["extended_hours"] = str(self.extended_hours_checkbox.isChecked()).lower()
            if self.month_input.text():
                params["month"] = self.month_input.text()
            params["outputsize"] = self.outputsize_combo.currentText()
            params["datatype"] = self.datatype_combo.currentText()
        elif function in ["TIME_SERIES_DAILY", "TIME_SERIES_DAILY_ADJUSTED"]:
            params["outputsize"] = self.outputsize_combo.currentText()
            params["datatype"] = self.datatype_combo.currentText()
        elif function in ["TIME_SERIES_WEEKLY", "TIME_SERIES_WEEKLY_ADJUSTED", "TIME_SERIES_MONTHLY", "TIME_SERIES_MONTHLY_ADJUSTED"]:
            params["datatype"] = self.datatype_combo.currentText()
        elif function == "GLOBAL_QUOTE":
            params["datatype"] = self.datatype_combo.currentText()
        elif function == "REALTIME_BULK_QUOTES":
            symbols = symbol.split(',')
            if len(symbols) > 100:
                symbols = symbols[:100]
            params["symbol"] = ','.join(symbols)
            params["datatype"] = self.datatype_combo.currentText()
        return params

    def save_csv(self, response):
        """
        Saves the CSV file to the user's selected location.
        """
        if response.status_code == 200:
            save_path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)")
            if save_path:
                with open(save_path, 'wb') as file:
                    file.write(response.content)
                print(f"CSV file saved to {save_path}")
        else:
            print("Failed to download CSV")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SymbolFinderApp()
    window.show()
    sys.exit(app.exec())
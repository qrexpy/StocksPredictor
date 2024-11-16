![icons8-stocks-128](https://github.com/user-attachments/assets/ef29c1a1-4dc2-43a0-add2-86affd69c777)

# `Stocks Predictor`

#### <code>❯ Made by Qrexxed</code>

<p align="left">
	<img src="https://img.shields.io/github/license/unerrored/Stocks_Predictor?style=flat&logo=opensourceinitiative&logoColor=white&color=370164" alt="license">
	<img src="https://img.shields.io/github/last-commit/unerrored/Stocks_Predictor?style=flat&logo=git&logoColor=white&color=370164" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/unerrored/Stocks_Predictor?style=flat&color=370164" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/unerrored/Stocks_Predictor?style=flat&color=370164" alt="repo-language-count">
</p>
<p align="left">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
- [📌 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

<code>❯ Stocks predictor is an app which predicts stocks from a local file (.csv or .xslx)</code>

---

## 👾 Features

<code>❯ Accurate prediction model (thanks to ChatGPT)</code>

<code>❯ Supports CSV, XSLX, and PNG charts (soon)</code>

<code>❯ Doesn't take time to predict stocks.</code>

---

## 📂 Repository Structure

```sh
└── Stocks_Predictor/
    ├── LICENSE
    ├── currency_daily_BTC_EUR.csv
    ├── README.md
    ├── candlestickchart
    │   ├── candlestick_chart.png
    │   ├── chartgenerator.py
    │   └── intraday_5min_IBM.csv
    ├── example_stocks
    │   ├── crypto_5min.csv
    │   ├── btc_euro_daily.csv
    │   ├── intraday_5min.csv
    │   └── ...
    └── main.py
```

---

## 🧩 Modules

<details closed><summary>Repository folder</summary>

| File | Summary |
| --- | --- |
| [main.py](https://github.com/unerrored/Stocks_Predictor/blob/main/main.py) | <code>❯ Main program</code> |

</details>

<details closed><summary>candlestickchart</summary>

| File | Summary |
| --- | --- |
| [chartgenerator.py](https://github.com/unerrored/Stocks_Predictor/blob/main/candlestickchart/chartgenerator.py) | <code>❯ Generates candlestick charts using .csv</code> |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version 3.12`

### 📦 Installation

Build the project from source:

1. Clone the repository:
```sh
❯ git clone https://github.com/unerrored/Stocks_Predictor
```

2. Navigate to the project directory:
```sh
❯ cd Stocks_Predictor
```

3. Install the required dependencies using pip:
```sh
❯ pip install pandas numpy matplotlib mplfinance scikit-learn opencv-python keras
```

### 🤖 Usage

To run the project, run the following file:

```sh
❯ main.py
```

To run the chart generator, run the following file:

```sh
❯ candlestickchart/chartgenerator.py
```

---

## 📌 Project Roadmap

- [ ] **`Task 1`**: <strike>Add XSLX support</strike> <-- Won't be used
- [ ] **`Task 2`**: Add PNG support
- [ ] **`Task 3`**: Create GUI for program

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/unerrored/Stocks_Predictor/issues)**: Submit bugs found or log feature requests for the `Stocks_Predictor` project.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/unerrored/Stocks_Predictor
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/unerrored/Stocks_Predictor/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=unerrored/Stocks_Predictor">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MIT LICENSE](https://choosealicense.com/licenses/mit/). For more details, refer to the [LICENSE](https://raw.githubusercontent.com/unerrored/Stocks_Predictor/refs/heads/main/LICENSE/) file.

---

## 🙌 Acknowledgments

- Icons8
- Readme-AI
- Plotly

---

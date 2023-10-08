# ExcelGraphicx

ExcelGraphicx is a web application that allows you to convert .xlsx and .csv files into interactive charts.

## Table of Contents

- [Overview](#overview)
- [Screenshots](#screenshots)
- [Features](#features)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [License](#license)
- [Feedback and Contributions](#feedback-and-contributions)

## Overview

ExcelGraphicx is a user-friendly tool for data visualization. It simplifies the process of creating charts from Excel (.xlsx) and CSV files. With ExcelGraphicx, you can quickly turn your data into insightful visualizations without the need for complex software or coding.

## Screenshots

### Home Page - File Upload
![Home Page - File Upload](https://snipboard.io/NlIARC.jpg)

### Selecting Axis
![Selecting Axis](https://snipboard.io/LDaAYi.jpg)

### Generated Graphic
![Generated Graphic](https://snipboard.io/R8F1ES.jpg)

## Features

- **Easy File Upload:** Simply upload your .xlsx or .csv files to get started.
- **Intuitive Interface:** Easily select your data and axis for chart creation.
- **Interactive Charts:** View and interact with your charts directly in the browser.
- **Export Options:** Download your charts for presentations and reports.
- **No Coding Required:** No coding or technical skills needed.

## Requirements

Before using this project, ensure that you have the following software installed in your development environment:

* **Python (3.6 or later):** You can download Python from [the official Python website.](https://www.python.org/downloads/)

![python](https://logosmarcas.net/wp-content/uploads/2021/10/Python-Logo.png)

## Installation and Setup

**1 - Clone or Download the Repository:**

Clone this repository to your local development environment or download the source code.

```bash
git clone https://github.com/Mulekotd/exel-graphicx.git

cd exel-graphicx
```

**2 - Install Dependencies with pip:**

Open a terminal and run:

```bash
pip install flask pyChart.JS pandas python-decouple
```

**3 - Configure the environment variable:**

Example .env file:

```.env
FLASK_SECRET_KEY=your_key_here
```

**4 - Start in your local machine:**

```psql
python .\main.py
```

## Usage

1. Visit the http://localhost:5000/.
2. Click the "Upload" button on the home page.
3. Select your .xlsx or .csv file.
4. Choose your data and axis settings.
5. Click "Generate Chart" to create your visualization.
6. Explore and interact with your chart.
7. Download the chart as .PDF.

## License

This project is open-source and is provided under the MIT License. You are free to use and modify it as needed. Feel free to contribute to the project or report any issues on the GitHub repository.

![mit](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/MIT_logo.svg/1920px-MIT_logo.svg.png)

## Feedback and Contributions

We welcome feedback, suggestions, and contributions from the community. If you have ideas for improvements or encounter any issues, please don't hesitate to [open an issue](https://github.com/Mulekotd/excel-graphicx/issues) on GitHub.

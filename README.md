# Auto Ticket/Product Purchase Application
[![English](https://img.shields.io/badge/Read-English-blue)](README.md)
[![繁體中文](https://img.shields.io/badge/讀-繁體中文-red)](README.cn.md)



This ticket crawling application, developed using Python and Selenium, is designed to automate the process of buying tickets or products online.

## Features

- Automatically navigates to a specified webpage.
- Automatically fills in login information.
- Automatically fills in personal details required for ticket purchase or shopping.
- Automates the checkout process.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: You'll need Python installed on your computer. Visit the [official Python website](https://www.python.org/downloads/) and download the version appropriate for your system.

- **Selenium**: The script uses Selenium for web automation. Install it via pip with the command:
    ```sh
    pip install selenium
    ```

- **Web Browser**: Ensure you have a supported web browser like Google Chrome or Firefox installed.

- **WebDriver**: Download the WebDriver for your browser:
    - For Chrome, get ChromeDriver from [ChromeDriver downloads](https://chromedriver.chromium.org/).
    - For Firefox, get Web Driver from [Mozilla Web Doc](https://developer.mozilla.org/en-US/docs/Web/WebDriver).

- **Additional Python Packages**: If the script uses other packages, you might need to install them. Typically, these will be listed in a `requirements.txt` file, which you can install all at once using:
    ```sh
    pip install -r requirements.txt
    ```

- **Text Editor/IDE (Optional)**: For editing or reviewing the script, use a text editor like Visual Studio Code, Sublime Text, or an IDE like PyCharm.


## Installation

1. Clone the repository to your local machine:
    ```sh
   git clone https://github.com/mikehsin/Ticket-Crawler.git
   ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```


## How to Use

1. Update the variables in `script.py`, including the target URL, username, password, etc.
2. Run the script:
    ```sh
    python ticket.py
    ```

## Important Notes

- Ensure your use complies with the terms of service of the target website.
- This script is provided without warranty of any kind. The author does not hold any legal liability for any actions taken by the users.
- This code is open-source. Feel free to contribute to its development and enhancement.

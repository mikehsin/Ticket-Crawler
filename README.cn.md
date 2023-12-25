# 搶票機器人
[![English](https://img.shields.io/badge/Read-English-blue)](https://github.com/mikehsin/Ticket-Crawler#)
[![繁體中文](https://img.shields.io/badge/讀-繁體中文-red)](https://github.com/mikehsin/Ticket-Crawler/blob/main/README.cn.md)

這個使用Python和Selenium開發的網頁爬蟲應用程式旨在自動化購買網上票券或商品的過程。

## 功能

- 自動導航至指定網頁。
- 自動填寫登入資訊。
- 自動填寫購票或購物所需的個人資訊。
- 自動進行結帳過程。

## 前提條件

在開始之前，請確保您已滿足以下要求：

- **Python**: 您需要在電腦上安裝Python。訪問[官方Python網站](https://www.python.org/downloads/)並下載適合您系統的版本。

- **Selenium**: 腳本使用Selenium進行網頁自動化。通過pip使用以下命令安裝：
    ```sh
    pip install selenium
    ```

- **網絡瀏覽器**: 確保您安裝了支持的網絡瀏覽器，如Google Chrome或Firefox。

- **WebDriver**: 下載適合您瀏覽器的WebDriver：
    - Chrome用戶，從[ChromeDriver下載頁面](https://chromedriver.chromium.org/)獲取ChromeDriver。
    - Firefox用戶，從[Mozilla Web Doc](https://developer.mozilla.org/en-US/docs/Web/WebDriver)獲取Web Driver。

- **額外的Python包**: 如果腳本使用其他包，您可能需要安裝它們。通常，這些將列在`requirements.txt`文件中，您可以使用以下命令一次性安裝所環境參數：
    ```sh
    pip install -r requirements.txt
    ```
- **文本編輯器/IDE (可選)**: 用於編輯或查看腳本，可以使用像Visual Studio Code、Sublime Text的文本編輯器或像PyCharm的IDE。


## 安裝

1. 克隆儲存庫到本地：
    ```sh
   git clone https://github.com/mikehsin/Ticket-Crawler.git
   ```

2. 安裝所需的Python套件：
    ```sh
    pip install -r requirements.txt
    ```


## 使用方式

1. 更新`ticket.py`中的變量，包括目標網址、帳號、密碼等。
2. 執行腳本：
    ```sh
    python ticket.py
    ```


## 注意事項
- 請確保您的使用符合目標網站的服務條款。
- 本腳本不提供任何形式的保證。作者不對用戶的任何行為承擔法律責任。
- 這段代碼是開源的。歡迎大家貢獻自己的力量來進行開發和完善。
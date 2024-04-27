# 導入必要的库
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# 設置 Chrome 驅動程式的路徑和啟動 WebDriver
service = Service('chromedriver')
driver = webdriver.Chrome(service=service)

# 打開目標網頁
driver.get("https://search.books.com.tw/search/query/key/%E7%A8%8B%E5%BC%8F/cat/all")

# 等待網頁加載，確保所需元素已經存在於網頁中
wait = WebDriverWait(driver, 10)
books = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "table-td")))

# 獲取網頁源碼
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# 解析網頁並抓取資料
data = []
index = 1

for book in soup.select('.table-td'):
    try:
        # 解析書籍資訊
        title = book.select_one("h4 a").text
        language = book.select_one(".type > p:nth-of-type(1)").text
        author = book.select_one(".author a").text
        price_info = book.select_one(".price").text.split(',')
        price = price_info[-1].strip()
        image_url = book.select_one("img")['data-src'].split("&")[0].replace("&amp;", "&")
        
        # 將解析的資料存儲到字典中，然後添加到列表
        temp_data = {
            "Title": title,
            "Language": language,
            "Author" : author,
            "Price": price,
            "ImageURL" : image_url
        }
        data.append(temp_data)
        
        index += 1
    except:
        continue

# 將抓取的資料轉換為 DataFrame，並保存為 CSV 檔案
df = pd.DataFrame(data)
df.to_csv("books.csv", encoding='utf_8_sig', index=False)

# 關閉瀏覽器
driver.quit()

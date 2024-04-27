# 學習分析工具(大數據教育學程)

廖執善 博士 Tom Liao, 業界講師 Ryan Chung

contact: benfeng99@gmail.com  
my blog:https://breeze0305.github.io/about/  
Discord:breeze0305

***
## HW2
> requirements:  
> pip install pandas  
> pip install selenium  
> pip install webdriver_manager  
> pip install beautifulsoup4  
> pip install requests  

### 使用requests
[main_requests.py](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/main_requests.py) 為執行檔案，[requests_books.csv](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/requests_books.csv)為爬取的內容。

### 使用selenium
[main_selenium.py](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/main_selenium.py) 為執行檔案，[Chromedriver](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/chromedriver.exe)是符合我本地的chrome driver，如需執行，請更改成自己的版本，[selenium_books.csv](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/selenium_books.csv)為爬取的內容。

```
爬取網頁:博客來網站搜尋(程式)
url:https://search.books.com.tw/search/query/key/%E7%A8%8B%E5%BC%8F/cat/all
```

## 爬取內容

* 書名
* 語言
* 作者
* 價格
* 書的圖片


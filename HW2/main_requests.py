import requests
import pandas as pd
from bs4 import BeautifulSoup



if __name__ == '__main__':
    # 設定目標網址
    url = "https://search.books.com.tw/search/query/key/%E7%A8%8B%E5%BC%8F/cat/all"

    # 發送 HTTP 請求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'  # 確保正確的編碼

    # 解析網頁內容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有 'table-td' class 的 div 標籤
    items = soup.find_all('div', class_='table-td')
    index = 1
    data = []
    
    # 遍歷每個項目，爬取需要的資訊
    for item in items:
        try:
            title_tag = item.find('h4').find('a')
            title = title_tag.get_text(strip=True)
            language = item.find('div', class_='type clearfix').find('p').text.strip()
            authors = [a.text for a in item.find('p', class_='author').find_all('a')]
            author = ', '.join(authors)
            price_info = item.find('ul', class_='price clearfix').find('li').get_text(strip=True)
            price = price_info.split(',')[-1].strip()
            image_url = item.find('div', class_='box').find('img')['data-src']

            # 將資料存儲到字典中
            temp_data = {
                "Title": title,
                "Language": language,
                "Author": author,
                "Price": price,
                "Image URL": image_url
            }
            data.append(temp_data)

            print(f"----- Book {index} -----")
            print(f"Title: {title}")
            print(f"Language: {language}")
            print(f"Authors: {', '.join(authors)}")
            print(f"Price: {price}")
            print(f"Image URL: {image_url}")
            index+=1
        except:
            continue
    
    df = pd.DataFrame(data)
    filename = 'requests_books.csv'
    df.to_csv(filename, index=False, encoding='utf_8_sig')
# 這段程式碼是使用子進程來執行pip安裝cssselect模組，並使用requests和lxml.html模組來解析網頁內容。


# 導入sys模組，用於訪問系統相關的功能。
import sys

# 導入subprocess模組，用於建立和管理子進程，以執行命令行操作。
import subprocess

# 使用check_call函數執行指定的命令，該函數會等待命令完成並檢查返回碼。
# 在這裡，指定的命令是一個列表，包含要在命令行中執行的命令以及相應的參數。其中：
# -`sys.executable`提供Python解釋器的路徑，以確保在正確的環境中執行pip。
# -`-m pip` 表示使用Python的pip模組。
# -`install cssselect` 是指定要安裝的模組。
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cssselect'])

# 導入requests函式庫，它是用於向網站發送HTTP請求以取得網頁資源的常用函式庫。
import requests

# 導入lxml函式庫中的html模組，用於解析HTML文件並建構ElementTree物件。
from lxml import html

# 發送一個GET請求到指定的URL（"http://www.flag.com.tw/books/school_code_n_algo"），
# 並將回應儲存在變數r中。
r = requests.get("http://www.flag.com.tw/books/school_code_n_algo")

# 使用lxml.html模組中的fromstring()函式將回應的HTML文本轉換為ElementTree物件，儲存在變數tree中。
tree = html.fromstring(r.text)

# 使用CSS選擇器來選擇特定的HTML元素。這裡選擇了第一個`<img>`元素，並將其儲存在tag_img中。
tag_img = tree.cssselect("body > section.allbooks > table > tr:nth-child(2) > td:nth-child(1) > a > img")[0]

# 輸出`tag_img`元素的內容。
print(tag_img)
print('---------------------------')

# 輸出`tag_img.tag`元素的標籤名稱。
print(tag_img.tag)
print('---------------------------')

# 輸出圖片的URL。
print(tag_img.attrib["src"])
print('---------------------------')

# 使用CSS選擇器來選擇第一個`<p>`元素，並將其儲存在`tag_p`中。
#tag_p = tree.cssselect("body > section.allbooks > table > tr:nth-child(2) > td:nth-child(1) > a > p")[0]


tag_p = tree.cssselect("body > section.allbooks > table > tr:nth-child(2) > td:nth-child(2) > a > p")[0]

# 輸出`tag_p`元素的內容。
print(tag_p)
print('---------------------------')

# 輸出`tag_p`元素的標籤名稱。
print(tag_p.tag)
print('---------------------------')

# 輸出`tag_p`元素的文本內容為
# 世界第一簡單的 Python「超」入門 - 零基礎 OK！ChatGPT 隨時當助教！。
print(tag_p.text_content())
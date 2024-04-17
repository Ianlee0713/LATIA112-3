# 學習分析工具(大數據教育學程)

廖執善 博士 Tom Liao, 業界講師 Ryan Chung

contact: benfeng99@gmail.com  
my blog:https://breeze0305.github.io/about/  
Discord:breeze0305

> 有考慮開設python家教班(須付費)，教授一些python的基礎知識和語法(系統化的教學)  
> 可能每個禮拜線上google meet上課，有意願的同學可以私訊我IG:boku_kaze詢問細節  
> 直接私訊說明你是誰，我會在統計後考慮要不要開班  
> 越多人會越便宜，不限定修課同學(但一批頂多4人，太多人就沒辦法全部照顧到)  
> 曾在補習班教國小國中python班，他們都可以理解了，更何況是大學生  
> 如果有需要任何客制化教學，可以再私訊詢問  
```
詢問問題請有禮貌，先告知你的身分，並詳細說明你的問題。
有必要的情況下請附上截圖與檔案。
👍
Please ask questions politely, state your identity first, and provide detailed explanations of your questions.  
If necessary, please attach screenshots and files.
```
***
## HW1

[main.py](https://github.com/breeze0305/LATIA112-2/blob/main/HW1/main.py) 為執行檔案，使用[student-behavior.csv](https://github.com/breeze0305/LATIA112-2/blob/main/HW1/student-behavior.csv) ([Kaggle/student-behavior](https://www.kaggle.com/datasets/gunapro/student-behavior/))作為統計的資料集，預設使用[TaipeiSansTCBeta](https://github.com/breeze0305/LATIA112-2/blob/main/HW1/TaipeiSansTCBeta-Regular.ttf)字體，使用[matplotlib](https://matplotlib.org/)繪製圖表，程式執行完畢後，圖片會存在同目錄下的[answer_pic](https://github.com/breeze0305/LATIA112-2/tree/main/HW1/answer_pic)。

```
資料集說明:此資料集為這是一個有關學生行為的csv數據,出自Kaggle開放式平台的數據  
網頁:https://www.kaggle.com/datasets/gunapro/student-behavior/
```
***
## HW2

[main.py](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/main.py) 為執行檔案，[Chromedriver](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/chromedriver.exe)是符合我本地的chrome driver，如需執行，請更改成自己的版本，[books.csv](https://github.com/breeze0305/LATIA112-2/blob/main/HW2/books.csv)為爬取的內容。

```
爬取網頁:博客來網站搜尋(程式)
url:https://search.books.com.tw/search/query/key/%E7%A8%8B%E5%BC%8F/cat/all
```
## week 1

## week 2
### 影響大學生每周讀書時間的理由
* 是否有打工需求  
* 課業壓力多寡
* 社團、系上活動籌備多寡  
### 分析大專院校校別學生數
* 各大學的男女分佈
* 各 __等級別__ 的性別分佈
* 各大學的博士、碩士生比例

## week 3

回答"分析大專院校校別學生數" -> [answer code](https://github.com/breeze0305/LATIA112-2/blob/main/week3/main.py)  


## week 4

### 影響大學生每周讀書的理由
* 大一、大二、大三、大四學生的讀書平均時間
* 平均3C的使用時間
* 每個年級的平均學分數

| 欄位名稱     | 資料尺度 | 類型      |
|--------------|----------|-----------|
| 學年度        | 名目尺度 | category  |
| 三年級女      | 等比尺度 | int       |
| 學校代碼      | 名目尺度 | string    |
| 四年級男      | 等比尺度 | int       |
| 學校名稱      | 名目尺度 | string    |
| 四年級女      | 等比尺度 | int       |
| 日間∕進修別   | 名目尺度 | category  |
| 五年級男      | 等比尺度 | int       |
| 等級別        | 名目尺度 | category  |
| 五年級女      | 等比尺度 | int       |
| 總計         | 等比尺度 | int       |
| 六年級男      | 等比尺度 | int       |
| 男生計       | 等比尺度 | int       |
| 六年級女      | 等比尺度 | int       |
| 女生計       | 等比尺度 | int       |
| 七年級男      | 等比尺度 | int       |
| 一年級男      | 等比尺度 | int       |
| 七年級女      | 等比尺度 | int       |
| 一年級女      | 等比尺度 | int       |
| 延修生男     | 等比尺度 | int       |
| 二年級男      | 等比尺度 | int       |
| 延修生女     | 等比尺度 | int       |
| 二年級女      | 等比尺度 | int       |
| 縣市名稱      | 名目尺度 | string    |
| 三年級男      | 等比尺度 | int       |
| 體系別       | 名目尺度 | category  |

## week 5

## week 6

## week 7

## week 8

## week 9

## week 10

## week 11

## week 12

## week 13

## week 14

## week 15

## week 16
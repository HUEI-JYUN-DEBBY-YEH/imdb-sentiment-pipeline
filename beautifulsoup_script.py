import requests
from bs4 import BeautifulSoup
import json

# 請求網頁資料
url = 'https://www.imdb.com/title/tt33175825/reviews/?ref_=tt_ururv_sm'
headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url)

# 結構化HTML
soup = BeautifulSoup(res.text, 'html.parser')

# 找到JSON的資料(唯一一個<script>)
script = soup.find('script', id = '__NEXT_DATA__')
json_text = script.string
data = json.loads(json_text)

# 嘗試進入JSON結構(User Review)
try:
    reviews = data['props']['pageProps']['contentData']['subNavReviews']['total']
    print(f"總評論數: {reviews}")
except:
    print("目前尚未定位到完整review資料，需人工檢查JSON結構")

# 若要debug，可以下面這一行列印出全部JSON結構方便觀察
# print(json.dumps(data. indent=2))

# 存成JSON檔案(暫存資料)
with open("comment.json", "w", encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON初步資料儲存成功!請打開comment.json觀察內部結構。")
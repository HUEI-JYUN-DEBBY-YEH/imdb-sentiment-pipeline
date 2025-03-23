import requests
import json

# 請求網址（來自你提供的 GraphQL API）
url = 'https://caching.graphql.imdb.com/?operationName=TitleReviewsRefine&variables=%7B%22after%22%3A%22g4xorermtizcsyih7svxrojrrdt42aj73end37pqcwb32u3bnet26cs5partaiojg4k4tbdohd53nlnj4jhqctq%22%2C%22const%22%3A%22tt33175825%22%2C%22filter%22%3A%7B%7D%2C%22first%22%3A25%2C%22locale%22%3A%22zh-TW%22%2C%22sort%22%3A%7B%22by%22%3A%22HELPFULNESS_SCORE%22%2C%22order%22%3A%22DESC%22%7D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%2289aff4cd7503e060ff1dd5aba91885d8bac0f7a21aa1e1f781848a786a5bdc19%22%2C%22version%22%3A1%7D%7D'

# HTTP headers（你提供的完整模擬瀏覽器）
headers = {
    'Accept': 'application/graphql+json, application/json',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/json',
    'Origin': 'https://www.imdb.com',
    'Referer': 'https://www.imdb.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'x-imdb-client-name': 'imdb-web-next',
    'x-imdb-client-rid': 'NPRSAE7893D581CWCVWY',
    'x-imdb-user-country': 'TW',
    'x-imdb-user-language': 'zh-TW'
    # 🟡 Cookies 通常不用加，除非 request 被拒
}

# 發送請求
response = requests.get(url, headers=headers)

# 確認回傳成功
if response.status_code == 200:
    data = response.json()
    reviews = data['data']['title']['reviews']['edges']

    all_reviews = []
    for review in reviews:
        node = review['node']
        text = node['text']['originalText']['plaidHtml']
        author = node['author']['nickName']
        rating = node.get('authorRating', None)  # 有些沒給分
        all_reviews.append({
            'author': author,
            'text': text,
            'rating': rating
        })

    # 儲存為 JSON 檔案
    with open('imdb_reviews.json', 'w', encoding='utf-8') as f:
        json.dump(all_reviews, f, ensure_ascii=False, indent=2)

    print(f"✅ 成功擷取 {len(all_reviews)} 則評論，已儲存至 imdb_reviews.json")
else:
    print(f"❌ 請求失敗，HTTP 狀態碼：{response.status_code}")
import requests
import json
import time

base_url = 'https://caching.graphql.imdb.com/'

params_template = {
    "operationName": "TitleReviewsRefine",
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "89aff4cd7503e060ff1dd5aba91885d8bac0f7a21aa1e1f781848a786a5bdc19"
        }
    },
    "variables": {
        "const": "tt33175825",
        "filter": {},
        "first": 25,
        "locale": "zh-TW",
        "sort": {
            "by": "HELPFULNESS_SCORE",
            "order": "DESC"
        },
        "after": None
    }
}

headers = {
    'Accept': 'application/graphql+json, application/json',
    'Accept-Language': 'zh-TW,zh;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://www.imdb.com',
    'Referer': 'https://www.imdb.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'x-imdb-client-name': 'imdb-web-next',
    'x-imdb-user-country': 'TW',
    'x-imdb-user-language': 'zh-TW'
}

all_reviews = []
page = 1
has_next_page = True
end_cursor = None

while has_next_page:
    params_template["variables"]["after"] = end_cursor

    res = requests.post(
        url=base_url + "?operationName=TitleReviewsRefine",
        headers=headers,
        json={
        "operationName": params_template["operationName"],
        "variables": params_template["variables"],
        "extensions": params_template["extensions"]
        }
    )

    if res.status_code != 200:
        print(f"❌ Page {page} failed with status code: {res.status_code}")
        break

    data = res.json()
    edges = data["data"]["title"]["reviews"]["edges"]
    page_info = data["data"]["title"]["reviews"]["pageInfo"]

    for edge in edges:
        node = edge["node"]
        text = node["text"]["originalText"].get("plaidHtml", "")
        author = node["author"].get("nickName", "unknown")
        rating = node.get("authorRating", None)

        all_reviews.append({
            "author": author,
            "text": text,
            "rating": rating
        })

    print(f"✅ Page {page} done: {len(edges)} reviews")
    has_next_page = page_info["hasNextPage"]
    end_cursor = page_info["endCursor"]
    page += 1
    time.sleep(1)

# 儲存 JSON
with open("imdb_reviews_all.json", "w", encoding="utf-8") as f:
    json.dump(all_reviews, f, ensure_ascii=False, indent=2)

print(f"🎉 所有評論抓取完畢，共 {len(all_reviews)} 則，已儲存為 imdb_reviews_all.json")
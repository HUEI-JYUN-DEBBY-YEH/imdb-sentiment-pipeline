import json
import re
import html

# 讀入 JSON 檔
with open("imdb_reviews_all.json", "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []

for item in data:
    raw_text = item["text"]

    # 去除 HTML 標籤
    text = re.sub(r"<.*?>", "", raw_text)

    # 解碼 HTML 字元（例如 &quot; → "）
    text = html.unescape(text)

    # 去掉換行符號
    text = text.replace("\n", " ").replace("\r", " ")

    # 刪掉前後空白
    text = text.strip()

    # 篩掉過短的句子
    if len(text.split()) > 5:
        cleaned.append({
            "text": text,
            "rating": item.get("rating", None)
        })

# 儲存成清洗後 JSON
with open("imdb_reviews_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(cleaned, f, ensure_ascii=False, indent=2)

print(f"✅ 清洗完成，留下 {len(cleaned)} 筆乾淨評論！")

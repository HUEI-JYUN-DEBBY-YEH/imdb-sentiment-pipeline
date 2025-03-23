from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import json
import re
import html

# 模型設定
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

clf = pipeline("sentiment-analysis", model=model_name, tokenizer=tokenizer, truncation=True)

# Tokenizer 與模型（可選，若需細看）
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# 載入 IMDb 清洗過的 JSON
with open("imdb_reviews_cleaned.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 預備儲存分類結果
results = []

# 預備簡易清洗函式（防萬一）
def clean_text(text):
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# 主迴圈：分類每筆評論
for item in data:
    cleaned_text = clean_text(item["text"])
    prediction = clf(cleaned_text, truncation=True)[0]  # e.g. {'label': 'POSITIVE', 'score': 0.998}

    results.append({
        "text": cleaned_text,
        "label": prediction["label"],
        "score": prediction["score"],
        "rating": item.get("rating")
    })

# 儲存結果
with open("imdb_reviews_classified.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ 完成分類，共 {len(results)} 筆資料，已儲存為 imdb_reviews_classified.json")
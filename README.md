This project presents a sentiment analysis pipeline utilizing the IMDb movie reviews dataset. It involves data preprocessing, model training, and evaluation phases, providing insights into the application of NLP techniques for sentiment classification tasks.

# 🎬 IMDb Attack on Titan Sentiment Classifier

本專案透過 Hugging Face pipeline 工具，對《進擊的巨人：最終話》IMDB 影評進行情緒分類。

## 📌 專案目標
- 練習 BeautifulSoup + Network API 自動爬 IMDb 影評
- 使用 transformers pipeline 模型進行情緒分類
- 結果視覺化、整理成資料集與技術報告

## 🛠️ 技術工具
- Python, BeautifulSoup, requests
- Hugging Face transformers (`distilbert-base-uncased-finetuned-sst-2-english`)
- PyTorch backend
- JSON, pandas, matplotlib

## 📁 專案架構
- `imdb_scraper_full.py`: 自動翻頁爬蟲
- `tokenizer_sentiment_pipeline.py`: 推論主程式
- `imdb_reviews_cleaned.json`: 清洗過文本
- `imdb_reviews_classified.json`: 含分類結果的 JSON

## 📊 結果摘要
1. 情緒分佈總覽：
- 共有 61 筆評論，其中： 
  **正向評論（POSITIVE）**佔約 77%
  **負向評論（NEGATIVE）**約佔 23%
➡️ 這顯示大多數觀眾對《Attack on Titan: The Final Attack》給予高度正評

2. 文字雲（WordCloud）洞察重點：
- Positive 常見詞彙：
  **masterpiece, thank, story, perfect, Isayama, character, emotional, freedom**
➡️ 表達出對劇情、角色深度、主題與創作者的感激與讚賞
- Negative 常見詞彙：
  **ending, disappointing, Armin, sense, felt, waste, lack, mess**
➡️ 多聚焦在劇情收尾與角色安排引發的失落或失望感

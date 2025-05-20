This project was part of my journey toward building fair, human-centered AI for workplace transformation.

# 🎬 Sentiment Analysis with Transformers Pipeline

*IMDb Review Classification using Pretrained Models*

This project demonstrates how to quickly deploy a **sentiment analysis pipeline** using Hugging Face's `transformers` library, without any custom training or fine-tuning. It showcases how pretrained models can be leveraged directly to analyze user-generated text with minimal setup.

---

## 💡 Why This Matters

While building custom models is valuable, many practical use cases can benefit from **zero-shot or pretrained pipelines**, especially when time or compute resources are limited. This project illustrates how an NLP engineer can **rapidly prototype sentiment analysis** systems using Hugging Face’s ecosystem — ideal for experimentation, PoC demos, or bootstrapping internal tools.

---

## 🧭 Project Overview

```mermaid
flowchart TD
    A[Input: IMDb movie review] --> B[transformers.pipeline("sentiment-analysis")]
    B --> C[Pretrained Model (e.g., distilbert-base-uncased-finetuned-sst-2)]
    C --> D[Prediction: POSITIVE / NEGATIVE + confidence score]
```

* **Pipeline Type**: Sentiment classification
* **Model Used**: `distilbert-base-uncased-finetuned-sst-2-english` (default from `transformers`)
* **Task**: Classify each review as `POSITIVE` or `NEGATIVE`
* **Output**: Label + Confidence Score (e.g., `POSITIVE (0.998)`)

---

## 📁 Repository Structure

```bash
imdb-sentiment-pipeline/
├── inference_pipeline.py     # Main script using Hugging Face pipeline
├── sample_data/
│   └── imdb_reviews.csv      # Sample reviews for batch inference
└── README.md
```

---

## 🚀 How to Use

1. **Install Dependencies**:

   ```bash
   pip install transformers pandas
   ```

2. **Run Inference**:

   ```bash
   python inference_pipeline.py
   ```

3. **Expected Output**:
   For each review, the script returns a sentiment label and confidence score.

---

## 🧪 Sample Output

| Review                           | Prediction | Confidence |
| -------------------------------- | ---------- | ---------- |
| "An amazing movie experience."   | POSITIVE   | 0.995      |
| "The story was weak and boring." | NEGATIVE   | 0.987      |

---

## 🛠 Future Enhancements

* Add Streamlit UI for interactive review scoring
* Compare multiple models (BERT, RoBERTa, DistilBERT)
* Enable multi-language sentiment pipelines
* Fine-tune on domain-specific datasets (e.g., finance, healthcare)

---

## 🧠 Learnings

* Hugging Face `pipeline` enables fast experimentation without training
* Pretrained models perform well on generic sentiment tasks
* Ideal for early-stage prototyping and PoC delivery

---

## ✍️ Author

**Debby Yeh**
NLP Application Engineer in Training
🔗 [Portfolio (Notion)](https://mango-mapusaurus-5df.notion.site/Debby-Yeh-Portfolio-1ca5118474d2801caa58de564fb53e38)
💡 Focus: NLP pipelines, vector search, model deployment


# 📹📝 YouTube Video Transcriber & Summarizer using Gemini Pro

This project uses **Google Gemini Pro** to build an LLM-powered app that takes a **YouTube video URL**, fetches the transcript, and provides a concise **summary**. Ideal for quick understanding of lectures, podcasts, or long-form videos.

---

## 📂 Project Structure

```
End To End Youtube Video Transcribe Summarizer LLM App With Google Gemini Pro/
├── app.py             # Streamlit UI for URL input and summarization display
└── requirements.txt
```

---

## 🚀 Features

- 🔗 Accepts YouTube URL input
- 🧠 Uses LangChain or pytube/youtube-transcript-api to extract transcript
- ✍️ Sends transcript to Gemini Pro LLM for intelligent summarization
- 🎯 Highlights key points and optionally returns bullet-form summary

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> 🔐 Requires Gemini API key and internet access to fetch transcripts.

---

## 💡 Use Cases

- Students summarizing long lectures
- Professionals reviewing webinars or product demos
- Fast content extraction from interviews and talks

---

## 🔭 Future Enhancements

- Add topic tagging from video
- Export summary to PDF
- Support multi-lingual transcripts


---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

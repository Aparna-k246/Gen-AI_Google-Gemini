# 🧠🖼️ LLM + Vision: End-to-End GenAI App using Google Gemini Pro

This project demonstrates an **end-to-end application** built using **Google Gemini Pro** that combines **text generation** with **large image understanding**. It allows users to input text or upload images and receive intelligent responses — all via a **Streamlit UI**.

---

## 📂 Project Structure

```
Building End to End LLM and Large image model  application using Gemini pro/
├── app.py           # Streamlit UI: handles both text and image input
├── vision.py        # Handles image parsing using Gemini Vision API
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 Features

- 🌐 Text prompt generation using Gemini Pro LLM
- 🖼️ Upload images (e.g., charts, receipts, diagrams) and get context-aware insights
- 🧠 Unified workflow for multi-modal AI interaction
- ✅ Built with production-ready Python code and modular functions

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> 🔐 Requires Gemini Pro API key (`GOOGLE_API_KEY` or `.env` file)

---

## 💡 Example Use Cases

- Upload a screenshot and ask “Summarize this chart.”
- Input text like “Generate a creative story about a robot dog.”
- Upload a food image and ask “Estimate calories.”

---

## 🔭 Future Enhancements

- Add PDF and audio support (multimodal fusion)
- Integrate memory to hold ongoing context
- Add Gemini Pro model selector via dropdown

---


## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

# 💬 Conversational Q&A Chatbot using Google Gemini Pro (LLM + Streamlit)

An intelligent chatbot built with **Google Gemini Pro** that supports **multi-turn, contextual conversations**. It can handle open-domain questions, retain chat history, and simulate human-like dialogue using LangChain memory and prompt engineering.

---

## 📂 Project Structure

```
Conversational Q&A Chatbot using Gemini Pro/
├── qachat.py          # Core Streamlit app for Gemini-based chatbot
├── requirements.txt   # Python dependencies
├── LICENSE
└── README.md
```

---

## 🚀 Features

- 💡 Real-time Q&A via Google Gemini Pro API
- 🧠 Memory-enabled multi-turn conversation (LangChain ConversationBuffer)
- 🗣️ Handles natural language prompts with follow-up context
- 🖥️ Simple and responsive Streamlit UI

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run qachat.py
```

> 🔐 Add your `GOOGLE_API_KEY` in `.env` or environment variables.

---

## 💬 Example Dialogue

- **User**: “What is LangChain?”
- **Bot**: “LangChain is a framework for building applications using LLMs...”
- **User**: “Can you compare it with LlamaIndex?”
- **Bot**: “Sure! LangChain focuses more on chaining and tools...”

---

## 🔭 Future Enhancements

- Add persona and tone controls (e.g., formal, friendly)
- Extend memory to long-term via Redis or external DB
- Add user authentication and chat logging

---


## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

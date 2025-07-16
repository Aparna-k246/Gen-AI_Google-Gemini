# 📄📚 Multi-PDF Chatbot using LangChain + Google Gemini Pro

An interactive chatbot that allows users to **upload and query multiple PDFs** simultaneously using **LangChain** for chunking/retrieval and **Google Gemini Pro** for answer generation. Perfect for extracting insights from large document sets.

---

## 📂 Project Structure

```
Chat with multiple Pdf Documents using Langchain and Google Gemini Pro/
├── app.py               # Streamlit UI: PDF uploader, query box, and result area
└── requirements.txt     # Dependencies
```

---

## 🚀 Features

- 📑 Upload multiple PDFs and chat with them
- 🔍 Uses LangChain to chunk and embed document content
- 💬 Gemini Pro generates accurate, context-aware answers
- 🧠 Maintains document context across queries

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> ⚙️ Add your Gemini API key in `.env` or as an environment variable: `GOOGLE_API_KEY=your_key_here`.

---

## 💡 Use Cases

- Research literature review from multiple papers
- Chat with legal contracts, policies, or financial reports
- Ask questions across mixed domains (PDFs with different subjects)

---

## 🔭 Future Enhancements

- Add chat history with memory
- PDF summarization before full query
- Use cloud storage for larger PDFs

---

## 📸 Screenshot Placeholder

```md
![Multi-PDF Chat UI](../assets/multi-pdf-chat-ui.png)
```

---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

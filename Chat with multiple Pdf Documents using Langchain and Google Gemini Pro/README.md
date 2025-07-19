# 📄📚 Multi-PDF Chatbot using LangChain + Google Gemini Pro

An interactive chatbot that allows users to **upload and query multiple PDFs** using **LangChain** for chunking/retrieval and **Google Gemini Pro** for intelligent answer generation. Designed with a **modular, production-ready architecture** under `src/`.

---

## 📂 Project Structure

```
multi-pdf-gemini-chat/
├── app.py                   # Streamlit app UI
├── src/
│   ├── chains.py            # Loads prompt + QA chain
│   ├── pdf_utils.py         # Extracts raw text from uploaded PDFs
│   ├── chunk_utils.py       # Splits text into chunks using LangChain
│   ├── vector_utils.py      # Creates & loads FAISS vector store
│   └── env_loader.py        # Loads environment variables from .env
├── faiss_index/             # Saved vector DB
├── .env                     # Contains your API key (excluded from repo)
└── requirements.txt         # Python dependencies
```

---

## 🚀 Key Features

- 📄 Upload and query **multiple PDFs**
- 🧠 Uses **LangChain** for context-rich chunking + retrieval
- 💬 Uses **Google Gemini Pro** for natural, accurate responses
- 🔗 Modular code under `src/` for easy maintenance & reuse
- 🔐 API key managed securely with `.env` file

---

## 📌 Prompt Template (in `chains.py`)

> _“If the answer is not in the provided context, respond with: 'Answer is not available in the context.'”_

- Custom-crafted to **minimize hallucination**
- Built using `PromptTemplate` + `load_qa_chain` with Gemini Pro

---

## 💻 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

➡️ Then add your Google API key to a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 🧠 Use Cases

- 🔬 Literature review across research PDFs
- 📃 Legal contract analysis
- 💼 Financial report Q&A
- 🏫 Students querying lecture notes

---

## 🎯 For Recruiters / Hiring Managers

- ✅ Showcases **modular GenAI architecture**
- ✅ Integrates **LangChain + Gemini Pro + FAISS** in a clean RAG pipeline
- ✅ Demonstrates practical problem-solving via LLM-based retrieval
- ✅ Portfolio-ready: deployable, readable, and scalable

---

## 🔭 Roadmap

- [x] Modularize all components into `src/` ✅
- [ ] Add Dockerfile for containerized deployment
- [ ] Add chat history and session memory
- [ ] Add HuggingFace or Streamlit Cloud deployment script
- [ ] Enable multi-user session capability

---

## 📫 Let's Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

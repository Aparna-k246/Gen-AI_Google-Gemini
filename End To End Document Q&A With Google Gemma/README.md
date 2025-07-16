# 📄📊 End-to-End Document Q&A System using Google Gemma

An intelligent document QA system that reads **multiple government PDFs**, processes them using **Google Gemma models**, and answers user queries based on embedded content. Built for scale with LangChain, vector stores, and a clean user interface.

---

## 📂 Project Structure

```
End To End Document Q&A With Google Gemma/
├── app.py                # Main Streamlit app for PDF-based Q&A
├── requirements.txt      # All dependencies
└── us_census/
    ├── acsbr-015.pdf
    ├── acsbr-016.pdf
    ├── acsbr-017.pdf
    └── p70-178.pdf       # Sample government reports
```

---

## 🚀 Features

- 🧾 Upload and query multiple government/statistical PDFs
- 📚 Chunk and embed documents using LangChain + Gemini-compatible methods
- 🤖 Gemini/Gemma LLM provides precise answers based on source documents
- 🖥️ Streamlit-based UI for end-user interaction

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> 📌 Place any new PDFs in the `us_census/` folder before running.

---

## 💬 Example Questions

- “What was the median household income in 2017?”
- “Summarize the findings of acsbr-016.pdf.”
- “How does population distribution change across reports?”

---

## 🔭 Future Enhancements

- Add document upload functionality to UI
- Enable multi-language PDF parsing
- Add table-based visualizations and highlights

---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

# 🧠📄 Resume ATS Ranking System using Google Gemini Pro (LLM-based)

This project builds an **LLM-powered Resume Ranking System** using **Google Gemini Pro**. It takes textual resumes, compares them with a job description, and returns **match scores**, extracted skills, and feedback — enabling fast and intelligent candidate screening.

---

## 📂 Project Structure

```
End To End Resume ATS Tracking LLM Project With Google Gemini Pro/
├── app.py               # Streamlit UI for uploading resume and JD
└── requirements.txt
```

---

## 🚀 Features

- 📥 Upload plain text or PDF resumes
- 📋 Input job descriptions manually or via file
- 🤖 Google Gemini Pro evaluates candidate–JD fit using reasoning and skill extraction
- 📈 Displays a match percentage with explanation

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> 🔐 Set your Gemini Pro `GOOGLE_API_KEY` in `.env` or your terminal.

---

## 💡 Example Use Case

- HR uploads a resume for a "Data Scientist"
- System returns 82% match with skills like Python, NLP, TensorFlow
- Feedback: "Lacks experience in cloud ML deployment"

---

## 🔭 Future Enhancements

- Batch upload of multiple resumes
- Export ranked list with scores
- Add recruiter dashboard and feedback override

---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

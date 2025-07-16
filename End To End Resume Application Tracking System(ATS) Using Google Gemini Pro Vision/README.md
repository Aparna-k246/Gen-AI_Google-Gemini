# 📄📊 Resume Application Tracking System (ATS) using Gemini Pro Vision

This project uses **Google Gemini Pro Vision** to build an intelligent **Resume Screening ATS** system that extracts structured data from resumes (images or PDFs) and evaluates them based on predefined job criteria — enabling automated shortlisting and ranking.

---

## 📂 Project Structure

```
End To End Resume Application Tracking System(ATS) Using Google Gemini Pro Vision/
├── app.py               # Streamlit app for uploading resumes and displaying ranking
└── requirements.txt     # Dependencies for Gemini Vision + LangChain
```

---

## 🚀 Features

- 📤 Upload resume image or scanned PDF
- 🤖 Extract candidate info (skills, experience, education) using Gemini Vision
- ✅ Match against job requirements and assign scores
- 📈 Streamlit-based UI for visual ATS pipeline

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> 🔐 Make sure your `GOOGLE_API_KEY` is set up in `.env` or the environment.

---

## 💡 Sample Use Case

- Upload 10 resumes for a "Python Backend Developer"
- Automatically extract skills & compare with job JD
- See a ranked list of top candidates based on match score

---

## 🔭 Future Enhancements

- Support PDF parsing alongside images
- Add feedback loop for recruiter override
- Export shortlisted resumes to CSV or ATS integration

---


## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

# 💬📊 Text-to-SQL App using Google Gemini Pro (with SQLite)

This end-to-end GenAI project allows users to **ask natural language questions** and automatically **generate SQL queries**, which are executed on a connected **SQLite database**. Powered by **Google Gemini Pro**, the app acts as a no-code/low-code analytics assistant.

---

## 📂 Project Structure

```
End to End Text to SQL LLM App along with Quering SQL database using Gemini Pro/
├── app.py           # Streamlit app: user input → Gemini prompt → SQL query
├── sqlite.py        # Sample SQLite database setup and schema
└── requirements.txt
```

---

## 🚀 Features

- 🧠 Converts natural language queries into executable SQL
- 🗃️ Queries SQLite database directly and shows table results
- 🤖 Gemini Pro handles prompt generation for accurate SQL creation
- 📊 Clean Streamlit UI for input and results panel

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

> 📁 Ensure the SQLite database is present or gets created by `sqlite.py`.

---

## 💬 Example Prompts

- “Show total sales by region.”
- “List customers with pending invoices.”
- “What is the average salary by department?”

---

## 🔭 Future Enhancements

- Add schema visualizer
- Support multiple SQL engines (MySQL, PostgreSQL)
- Add query validation + undo history

---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

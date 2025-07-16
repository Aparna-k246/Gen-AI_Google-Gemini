# 🗞️🕵️‍♀️ News Reporter AI Agent using CrewAI + Gemini Pro

This project builds a team of autonomous **AI agents** using **CrewAI**, each with specific roles — such as **news researcher**, **fact-checker**, and **story writer** — to collaboratively produce high-quality news summaries using **Google Gemini Pro**.

---

## 📂 Project Structure

```
News Reporter AI Agent Using CrewAI/
├── agents.py           # Defines each AI agent with its tools and goals
├── crew.py             # CrewAI crew configuration and task distribution
├── tasks.py            # Task prompts and role responsibilities
├── tools.py            # Tooling used by agents (e.g. web search, summarizers)
└── requirements.txt
```

---

## 🚀 Features

- 👥 Multi-agent system using CrewAI
- 🧠 Specialized roles: researcher, summarizer, fact-checker
- 🔍 Each agent uses Gemini Pro to complete its task
- 📰 Output: well-written, factual news article summaries

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
python crew.py
```

> 🔑 Requires `GOOGLE_API_KEY` and optionally a news API key depending on tools used.

---

## 💡 Example Workflow

1. **Research Agent** finds top trending AI news
2. **Fact Checker** validates sources and claims
3. **Writer Agent** summarizes findings into a coherent article

---

## 🔭 Future Enhancements

- Add memory/context to agents across sessions
- Enable voice/news reader output
- Deploy agent crew to stream news in real time


---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

# 🧾🌍 Multilingual Invoice Extractor using Gemini Pro Vision

A powerful GenAI solution that **extracts structured information from multilingual invoices** using **Google Gemini Pro Vision API**. This project processes invoices in various formats and languages and returns clean, structured fields such as vendor, date, total, tax, and currency.

---

## 📂 Project Structure

```
End to End Multi Language Invoice Extractor Project using Gemini Pro LLM Model/
├── vision.py             # Core script for image input and field extraction
├── requirements.txt
└── LICENSE
```

---

## 🚀 Features

- 📤 Upload invoice images (JPG/PNG/PDF)
- 🌐 Extracts fields across multiple languages (English, French, Hindi, etc.)
- 📊 Outputs structured JSON or table of invoice data
- 🧠 Gemini Vision API understands layout, text blocks, and field positions

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
python vision.py
```

> 🗝️ Add your `GOOGLE_API_KEY` for Gemini Vision in `.env` or as an environment variable.

---

## 🧾 Sample Output Format

```json
{
  "Vendor": "Amazon",
  "Date": "2024-06-15",
  "Total": "₹1,349.00",
  "Currency": "INR",
  "Tax": "₹249.00"
}
```

---

## 💡 Use Cases

- Automate invoice processing in global supply chains
- Handle receipts and bills from multiple countries
- Digitize accounts payable workflows using GenAI

---

## 🔭 Future Enhancements

- Add support for real-time file uploads via Streamlit
- Integrate OCR fallback for low-confidence cases
- Add automatic currency detection

---



## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

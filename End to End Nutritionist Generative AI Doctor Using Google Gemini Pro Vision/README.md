# 🥗🧠 Nutritionist AI Doctor using Google Gemini Pro Vision

A healthcare-focused GenAI project that allows users to upload **food images** and receive **nutritional analysis**, diet recommendations, and health advice using **Google Gemini Pro Vision API**. Acts as a **virtual AI nutritionist** for lifestyle improvement and meal tracking.

---

## 📂 Project Structure

```
End to End Nutritionist Generative AI Doctor Using Google Gemini Pro Vision/
├── health.py             # Core script for food image analysis and response
└── requirements.txt
```

---

## 🚀 Features

- 🍱 Upload food images to get nutrition breakdown
- 🧠 Gemini Pro Vision interprets image context and meal type
- 🍽️ Suggests portion control tips and healthy alternatives
- 🖥️ CLI-based output with optional UI extension

---

## 🛠️ How to Run

```bash
pip install -r requirements.txt
python health.py
```

> 🔐 Set your `GOOGLE_API_KEY` in the environment or `.env` file.

---

## 🍎 Sample Output

```json
{
  "Meal": "Grilled Paneer Salad",
  "Calories": "320 kcal",
  "Protein": "24g",
  "Suggestions": [
    "Add avocado for healthy fats",
    "Reduce dressing to lower sugar intake"
  ]
}
```

---

## 💡 Use Cases

- Health-conscious meal planning and tracking
- Personalized diet insights from food images
- AI assistant for gyms, clinics, or wellness apps

---

## 🔭 Future Improvements

- Add support for multi-item plates and regional cuisine
- Integrate daily calorie tracker
- Build complete Streamlit UI for meal logging


---

## 📫 Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Aparna-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/aparna-k-628005167/)

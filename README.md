# 🧠 AI Study Quiz Generator

A web app that turns your study notes or any topic into a multiple choice quiz instantly — powered by the Claude API.

Built as a portfolio project to learn Python API integration, prompt engineering, and building real AI-powered apps.

---

## 🎯 What It Does

- Paste any study notes or type a topic

- Choose how many questions (2–10)

- Claude generates a formatted multiple choice quiz with answers

---

## 🛠️ Tech Stack

- **Python** — core logic

- **Streamlit** — web UI

- **Anthropic Claude API** — quiz generation

- **python-dotenv** — secure API key management

---

## 🔑 Why You Need Your Own API Key

This app is intentionally built so each user supplies their own Anthropic API key.

This is standard practice for API-based projects — it means no shared credentials,

no surprise bills, and no rate limit issues for anyone. It also demonstrates secure

API key handling, which is a real-world engineering requirement.

Get one at [console.anthropic.com](https://console.anthropic.com)
---

## 🚀 Run It Yourself

### 1. Clone the repo

```bash

git clone [https://github.com/BlakeRad/quiz-generator.git](https://github.com/BlakeRad/quiz-generator.git)

cd quiz-generator

```

### 2. Install dependencies

```bash

pip install anthropic streamlit python-dotenv

```

### 3. Add your API key

Create a `.env` file in the root folder:

```

ANTHROPIC_API_KEY=your-key-here

```

### 4. Run the app

```bash

streamlit run app.py

```

---

## 💡 What I Learned

- How to authenticate and call a real third-party API

- Prompt engineering — structuring prompts to get consistent formatted output

- Secure API key handling with `.env` and `.gitignore`

- Building a functional UI with Streamlit

- Error handling for real-world API issues like auth errors and rate limits

---


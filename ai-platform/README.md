# 🚀 AI Platform

A multi-functional AI platform that integrates multiple AI capabilities into a single application.

This module contains **two implementations of the same platform**, using different AI providers:

* 🔵 OpenAI API
* 🟣 Gemini API

---

## 🧠 Features

Both implementations provide:

### 🤖 Chat Agent

* Conversational AI with memory
* Context-aware responses

### 📄 Document Analyzer

* PDF and TXT support
* Multi-file upload
* Analysis types:

  * Summary
  * Key points
  * Critique

### 🖼️ Image Analyzer

* Image understanding
* Multi-image support
* Contextual descriptions

---

## 🔀 Platform Variants

### 🔵 OpenAI Version

📁 `/openai-api/`
👉 [View OpenAI Platform](./openai-api/README.md)

* Uses OpenAI models (`gpt-4o-mini`)
* Image processing via base64
* Structured and consistent responses

---

### 🟣 Gemini Version

📁 `/gemini-api/`
👉 [View Gemini Platform](./gemini-api/README.md)

* Uses Gemini models (`gemini-1.5-flash`)
* Native multimodal support (no base64)
* Faster response generation

---

## 🛠️ Technologies Used

* Python
* OpenAI API
* Gemini API
* Streamlit
* PyPDF2
* Pillow
* python-dotenv

---

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/Yanmaiscedo/ai-multi-tools.git
cd ai-multi-tools/ai-platform
```

Then choose which implementation to run:

---

### ▶️ OpenAI Platform

```bash
cd openai-api
pip install -r requirements.txt
streamlit run main.py
```

---

### ▶️ Gemini Platform

```bash
cd gemini-api
pip install -r requirements.txt
streamlit run main.py
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
```

---

## 📌 Project Purpose

This project demonstrates:

* AI integration with multiple providers
* Modular system architecture
* Multimodal AI (text, documents, images)
* Comparison between OpenAI and Gemini

---

## 📈 Future Improvements

* Unified interface (switch between providers)
* Persistent memory (database)
* API version (FastAPI)
* Deployment (Streamlit Cloud / Render)
* Multi-agent orchestration
# 🚀 Gemini AI Platform

A multi-functional AI platform built using the Gemini API.
This application demonstrates multimodal AI capabilities with fast and efficient responses.

---

## 🧠 Features

### 🤖 Chat Agent

* Conversational AI
* Fast response generation
* Lightweight interaction

### 📄 Document Analyzer

* PDF and TXT support
* Multi-file processing
* Flexible analysis:

  * Summary
  * Key insights
  * Critique

### 🖼️ Image Analyzer

* Native multimodal image understanding
* No base64 required
* Direct image input support
* Detailed descriptions

---

## 🛠️ Technologies Used

* Python
* Gemini API (`gemini-1.5-flash`)
* Streamlit
* PyPDF2
* Pillow
* python-dotenv

---

## ⚙️ Setup

```bash
git clone https://github.com/Yanmaiscedo/ai-multi-tools.git
cd ai-multi-tools/gemini-api
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📌 How It Works

* Uses Gemini multimodal API
* Accepts text and images natively
* Processes documents and images with unified model

---

## ⚠️ Notes

* Faster responses compared to some models
* Native image support simplifies implementation
* May differ in output style compared to OpenAI

---

## ⚖️ OpenAI vs Gemini (Quick Comparison)

| Feature          | OpenAI          | Gemini         |
| ---------------- | --------------- | -------------- |
| Image Input      | Base64 required | Native support |
| Speed            | Moderate        | Fast           |
| Output Style     | More structured | More flexible  |
| Setup Complexity | Medium          | Simple         |

---

## 📈 Future Improvements

* Unified interface (switch between providers)
* Performance benchmarking
* Advanced prompt templates
* Deployment optimization
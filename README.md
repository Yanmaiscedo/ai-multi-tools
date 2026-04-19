# 🚀 AI Multi Tools

A comprehensive collection of AI-powered applications, ranging from standalone tools to fully integrated AI platforms.

This repository demonstrates practical implementations of modern AI using **multiple providers**, including OpenAI and Gemini APIs.

---

## 🧠 Projects Overview

### 🔹 1. Simple AI Modules (OpenAI)

Located in `/3-Simple-AIs/`

#### 🤖 AI Agent

👉 [View documentation](./3-Simple-AIs/agent/README.md)

* Conversational agent
* Task execution with tools
* Prompt-based reasoning (ReAct pattern)

#### 📄 PDF Reader

👉 [View documentation](./3-Simple-AIs/pdf_reader/README.md)

* Extracts and analyzes PDF content
* Summarization
* Question answering

#### 🖼️ Image Analyzer

👉 [View documentation](./3-Simple-AIs/image_analizer/README.md)

* Image understanding
* Object classification
* Visual content analysis

---

### 🔹 2. 🚀 AI Platforms

Located in `/ai-platform/`
👉 [View documentation](./ai-platform/openai-api/README.md)

2 unified AI systems powered by Gemini and OpenAI APIs:

* 🤖 Chat Agent with memory
* 📄 Multi-document analyzer (PDF + TXT)
* 🖼️ Image analyzer (Vision with base64)
* 🎯 Prompt templates (summary, critique, key points)

---

## 🛠️ Technologies Used

* Python
* OpenAI API
* Gemini API
* LangChain / LangGraph
* Streamlit
* PyPDF2 / pdfplumber
* PIL / OpenCV

---

## ⚙️ Setup

```bash
git clone https://github.com/Yanmaiscedo/ai-multi-tools.git
cd ai-multi-tools
pip install -r requirements.txt
```
You can use UV if you want:
```bash
git clone https://github.com/Yanmaiscedo/ai-multi-tools.git
cd ai-multi-tools
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
```

---

## ▶️ Usage

Each project has its own instructions:

### 🔹 Simple AIs

* 🤖 [AI Agent](./3-Simple-AIs/agent/README.md)
* 📄 [PDF Reader](./3-Simple-AIs/pdf_reader/README.md)
* 🖼️ [Image Analyzer](./3-Simple-AIs/image_analizer/README.md)

### 🔹 AI Platforms

* 🚀 [OpenAI Platform](./openai-api/README.md)
* 🚀 [Gemini Platform](./gemini-api/README.md)

---

## 📌 Project Purpose

This repository was developed to demonstrate:

* AI integration with multiple providers (OpenAI & Gemini)
* Modular and scalable system design
* Real-world AI applications
* Multimodal AI (text, documents, and images)
* Comparison between different AI APIs

---

## 📈 Future Improvements

* API version (FastAPI)
* Persistent memory (database)
* Authentication system
* Deployment (Streamlit Cloud / Render)
* Multi-agent orchestration

---

## 👨‍💻 Author

Yan Teixeira

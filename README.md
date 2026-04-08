# 🚀 AI Multi Tools

A collection of AI-powered applications built using the OpenAI API.
This project demonstrates practical implementations of AI in different domains.

---

## 🧠 Features

### 🤖 AI Agent

* Conversational agent
* Task execution
* Prompt-based reasoning

### 📄 PDF Reader

* Extracts and analyzes PDF content
* Summarization
* Question answering

### 🖼️ Image Analyzer

* Image understanding
* Description generation
* Visual content analysis

---

## 🛠️ Technologies Used

* Python
* OpenAI API
* LangChain / LangGraph *(if used)*
* PyPDF / pdfplumber
* PIL / OpenCV

---

## ⚙️ Setup

```bash
git clone https://github.com/seu-usuario/ai-multi-tools.git
cd ai-multi-tools
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run each module(you can use bash or uv):
- agent
```bash
cd agent
python main.py
```
```uv
cd agent
uv run main.py
```
- pdf_reader
```bash
cd pdf_reader
python main.py
```
```uv
cd pdf_reader
uv run streamlit run main.py
```
- image_analyzer
```bash
cd image_analyzer
python main.py
```
```uv
cd image_analyzer
uv run streamlit run main.py
```

---

## 📌 Project Purpose

This project was developed to practice and demonstrate:

* AI integration with APIs
* Real-world use cases
* Modular system design

---

## 📈 Future Improvements

* Web interface (Streamlit or React)
* API deployment
* Multi-agent orchestration
* Memory system

---

## 👨‍💻 Author

Yan Teixeira

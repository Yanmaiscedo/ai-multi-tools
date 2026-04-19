# 🚀 OpenAI AI Platform

A multi-functional AI platform built using the OpenAI API.
This application integrates chat, document analysis, and image understanding into a single system.

---

## 🧠 Features

### 🤖 Chat Agent

* Conversational AI with memory
* Context-aware responses
* Continuous interaction

### 📄 Document Analyzer

* Supports PDF and TXT files
* Multi-file upload
* Analysis types:

  * Summary
  * Detailed analysis
  * Key points
  * Critique

### 🖼️ Image Analyzer

* Image understanding using OpenAI Vision
* Supports multiple images
* Base64 encoding for local image processing
* Contextual and descriptive analysis

---

## 🛠️ Technologies Used

* Python
* OpenAI API (`gpt-4o-mini`)
* Streamlit
* PyPDF2
* Pillow
* python-dotenv

---

## ⚙️ Setup

```bash
git clone https://github.com/Yanmaiscedo/ai-multi-tools.git
cd ai-multi-tools/openai-api
pip install -r requirements.txt
```
You can use UV if you want:
```bash
git clone https://github.com/Yanmaiscedo/ai-multi-tools.git
cd ai-multi-tools/openai-api
uv sync
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```
You can use UV if you want:
```bash
uv run streamlit run main.py
```

---

## 📌 How It Works

* Chat uses OpenAI chat completions
* Documents are parsed and sent as structured prompts
* Images are converted to base64 and processed using multimodal input

---

## ⚠️ Notes

* Ensure your API key has available credits
* Large files may impact response time
* Image processing uses base64 encoding for compatibility

---

## 📈 Future Improvements

* Streaming responses (real-time chat)
* Persistent chat memory (database)
* API version with FastAPI
* Authentication system
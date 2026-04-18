import streamlit as st
import os
import io
import PyPDF2
from PIL import Image
from dotenv import load_dotenv
from openai import OpenAI

# ---------------- CONFIG ---------------- #
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Platform", page_icon="🚀", layout="wide")

# ---------------- SESSION MEMORY ---------------- #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- FUNCTIONS ---------------- #

def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text


def build_prompt(template, content):
    templates = {
        "Summary": f"Summarize the following content:\n{content}",
        "Detailed Analysis": f"Provide a detailed analysis:\n{content}",
        "Key Points": f"Extract key points:\n{content}",
        "Critique": f"Provide constructive critique:\n{content}",
    }
    return templates.get(template, content)


def ask_ai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content


# ---------------- UI ---------------- #
st.title("🚀 AI Platform")
st.markdown("Multi-functional AI system powered by OpenAI")

tab1, tab2, tab3 = st.tabs(["🤖 Chat Agent", "📄 Document Analyzer", "🖼️ Image Analyzer"])

# ---------------- 🤖 CHAT AGENT ---------------- #
with tab1:
    st.header("AI Chat Agent")

    user_input = st.text_input("Ask something")

    if st.button("Send"):
        if user_input:
            st.session_state.chat_history.append(("user", user_input))

            response = ask_ai(user_input)

            st.session_state.chat_history.append(("ai", response))

    for role, message in st.session_state.chat_history:
        if role == "user":
            st.markdown(f"**You:** {message}")
        else:
            st.markdown(f"**AI:** {message}")


# ---------------- 📄 DOCUMENT ANALYZER ---------------- #
with tab2:
    st.header("Document Analyzer")

    template = st.selectbox(
        "Choose analysis type",
        ["Summary", "Detailed Analysis", "Key Points", "Critique"],
        key="pdf_template"
    )

    uploaded_files = st.file_uploader(
        "Upload PDF or TXT files",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

    if uploaded_files:
        if st.button("Analyze Documents"):
            combined_text = ""

            for file in uploaded_files:
                if file.type == "application/pdf":
                    combined_text += extract_pdf_text(file)
                else:
                    combined_text += file.read().decode("utf-8")

            prompt = build_prompt(template, combined_text)

            with st.spinner("Analyzing..."):
                result = ask_ai(prompt)
                st.markdown(result)


# ---------------- 🖼️ IMAGE ANALYZER ---------------- #
with tab3:
    st.header("Image Analyzer")

    template = st.selectbox(
        "Choose analysis type",
        ["Summary", "Detailed Analysis", "Key Points", "Critique"],
        key="image_template"
    )

    uploaded_images = st.file_uploader(
        "Upload images",
        type=["jpg", "png"],
        accept_multiple_files=True
    )

    if uploaded_images:
        for img_file in uploaded_images:
            image = Image.open(img_file)
            st.image(image, caption=img_file.name)

        if st.button("Analyze Images"):
            with st.spinner("Analyzing images..."):
                for img_file in uploaded_images:
                    image = Image.open(img_file)

                    prompt = build_prompt(template, "Describe and analyze this image")

                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {"type": "text", "text": prompt},
                                    {"type": "image_url", "image_url": {"url": img_file}}
                                ]
                            }
                        ]
                    )

                    st.markdown(f"### 📸 {img_file.name}")
                    st.write(response.choices[0].message.content)
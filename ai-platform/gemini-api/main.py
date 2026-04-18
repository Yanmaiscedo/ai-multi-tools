import streamlit as st
import os
import io
import PyPDF2
from PIL import Image
from dotenv import load_dotenv
from google import genai

# ---------------- CONFIG ---------------- #
# A configuração da página DEVE ser a primeira linha do Streamlit
st.set_page_config(page_title="AI Platform", page_icon="🚀", layout="wide")

load_dotenv()
# Inicializando o cliente com a nova SDK (Google GenAI)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_ID = "gemini-1.5-flash"

# ---------------- SESSION MEMORY ---------------- #
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- FUNCTIONS ---------------- #

def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

def build_prompt(template, content):
    templates = {
        "Summary": f"Summarize the following content:\n{content}",
        "Detailed Analysis": f"Provide a detailed analysis:\n{content}",
        "Key Points": f"Extract key points:\n{content}",
        "Critique": f"Provide constructive critique:\n{content}",
    }
    return templates.get(template, content)

# ---------------- UI ---------------- #
st.title("🚀 AI Platform")
st.markdown("Multi-functional AI system powered by Gemini")

tab1, tab2, tab3 = st.tabs(["🤖 Chat Agent", "📄 Document Analyzer", "🖼️ Image Analyzer"])

# ---------------- 🤖 CHAT AGENT ---------------- #
with tab1:
    st.header("AI Chat Agent")

    # Layout do chat
    chat_container = st.container()
    
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask something:")
        submitted = st.form_submit_button("Send")

    if submitted and user_input:
        st.session_state.chat_history.append(("user", user_input))
        
        # Chamada correta usando o client
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_input
        )
        
        st.session_state.chat_history.append(("ai", response.text))

    # Mostrar histórico
    with chat_container:
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.chat_message("user").write(message)
            else:
                st.chat_message("assistant").write(message)

# ---------------- 📄 DOCUMENT ANALYZER ---------------- #
with tab2:
    st.header("Document Analyzer")

    template_pdf = st.selectbox(
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

            prompt = build_prompt(template_pdf, combined_text)

            with st.spinner("Analyzing..."):
                response = client.models.generate_content(model=MODEL_ID, contents=prompt)
                st.markdown("### Analysis Result")
                st.markdown(response.text)

# ---------------- 🖼️ IMAGE ANALYZER ---------------- #
with tab3:
    st.header("Image Analyzer")

    template_img = st.selectbox(
        "Choose analysis type",
        ["Summary", "Detailed Analysis", "Key Points", "Critique"],
        key="image_template"
    )

    uploaded_images = st.file_uploader(
        "Upload images",
        type=["jpg", "png", "jpeg"],
        accept_multiple_files=True
    )

    if uploaded_images:
        # Mostrar prévia das imagens
        cols = st.columns(len(uploaded_images))
        for idx, img_file in enumerate(uploaded_images):
            image = Image.open(img_file)
            cols[idx].image(image, caption=img_file.name, use_container_width=True)

        if st.button("Analyze Images"):
            with st.spinner("Analyzing images..."):
                for img_file in uploaded_images:
                    image = Image.open(img_file)
                    
                    # Para a SDK 'google-genai', passamos uma lista com o texto e a imagem
                    prompt = build_prompt(template_img, "Analyze this image")
                    
                    response = client.models.generate_content(
                        model=MODEL_ID,
                        contents=[prompt, image]
                    )

                    st.markdown(f"---")
                    st.markdown(f"### 📸 {img_file.name}")
                    st.write(response.text)
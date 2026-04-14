import streamlit as st
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

st.title("📃 AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")

analyze = st.button("Analyze Resume")

# ---------------- FILE PROCESSING ---------------- #

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# ---------------- AI ANALYSIS ---------------- #

def analyze_resume(text, job_role):
    client = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
    Analyze this resume and provide a structured response:

    1. Overall Score (0-100)
    2. Summary (short)
    3. Key Strengths (bullet points)
    4. Areas for Improvement (bullet points)
    5. Suggested Skills to Add
    6. Tailored Suggestions for {job_role if job_role else 'general job applications'}

    Resume:
    {text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert HR recruiter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1200
    )

    return response.choices[0].message.content


# ---------------- MAIN LOGIC ---------------- #

if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content...")
            st.stop()

        with st.spinner("Analyzing your resume..."):
            result = analyze_resume(file_content, job_role)

        st.markdown("## 📊 Analysis Results")
        st.markdown(result)

        # Download botão
        st.download_button(
            label="📥 Download Analysis",
            data=result,
            file_name="resume_analysis.txt",
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
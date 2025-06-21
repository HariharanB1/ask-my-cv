import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load the CV
def load_cv():
    with open("cv.txt", "r", encoding="utf-8") as file:
        return file.read()

# Ask the CV
def ask_cv(question, cv_text):
    prompt = f"""
You are a helpful assistant. Only answer using the information provided in Hariharan's CV below.
Do not guess or invent. If something is not mentioned, respond with "This information is not available in the CV."

CV:
{cv_text}

Question: {question}
Answer:
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("Ask My CV 👔🧠")
st.caption("Built by Hariharan Balaji")

cv_text = load_cv()

question = st.text_input("Ask about Hariharan's CV:")

if question:
    with st.spinner("Thinking..."):
        answer = ask_cv(question, cv_text)
    st.markdown("**Answer:**")
    st.write(answer)

import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ENVIRONMENT VARIABLE SETUP
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key:
    genai.configure(api_key=google_api_key)
else:
    st.error("GOOGLE_API_KEY not found. Check your .env file.")

# Streamlit UI
st.title("Gemini API Demo (Domain Specific)")

# Ask for domain
domain = st.selectbox(
    "Choose a domain:",
    ["Science", "Maths", "Technology", "History", "General Knowledge"]
)

# Ask for question
input_text = st.text_input("Enter your question:")

# When user inputs a question, call Gemini
if input_text:
    prompt = f"You are a knowledgeable assistant. Answer ONLY within the domain specified by the user.\nDomain: {domain}\nQuestion: {input_text}"
    
    model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-pro if enabled
    response = model.generate_content(prompt)
    
    st.write(response.text)

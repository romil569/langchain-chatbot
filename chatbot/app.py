import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize Ollama smollm model
llm = ChatOllama(model="smollm")

# Prompt template for summarizing email content
email_prompt = PromptTemplate(
    input_variables=["email"],
    template="Summarize the following email in 2-3 concise sentences:\n\n{email}"
)

# Create chain
email_summarizer_chain = LLMChain(llm=llm, prompt=email_prompt)

# Streamlit UI
st.title("📧 Email Summarizer")
st.write("Paste your email content below and get a concise 2-3 sentence summary.")

# Text area for input
email_text = st.text_area("Email Content", height=200)

# Button to trigger summarization
if st.button("Summarize"):
    if not email_text.strip() or len(email_text.split()) < 3:
        st.warning("⚠️ Please provide the complete email body (more than just a name or subject).")
    else:
        with st.spinner("Summarizing..."):
            summary = email_summarizer_chain.invoke({"email": email_text})
        st.subheader("✍️ Summary")
        st.write(summary["text"])

import streamlit as st
from prompts import generate_questions
from utils import analyze_sentiment, translate_text
import openai
import os

st.set_page_config(page_title="AI Hiring Assistant", page_icon="🧠")
st.title("🤖 TalentScout - AI Hiring Assistant Chatbot")

# API Key
openai.api_key = os.getenv("OPENAI_API_KEY", "your-openai-api-key")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.form("candidate_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    exp = st.slider("Years of Experience", 0, 30, 1)
    position = st.text_input("Desired Position(s)")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (comma-separated)")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.session_state.messages.append({"role": "user", "content": f"My name is {name}. I am experienced in {tech_stack}"})
    st.success("Thank you! Generating technical questions based on your tech stack...")

    stack_list = [tech.strip() for tech in tech_stack.split(",")]
    questions = generate_questions(stack_list)

    for tech, qs in questions.items():
        st.subheader(f"🧪 {tech} Questions:")
        for i, q in enumerate(qs, 1):
            st.write(f"**Q{i}:** {q}")

    sentiment = analyze_sentiment(f"My name is {name}. I have {exp} years experience.")
    st.info(f"💬 Sentiment Detected: **{sentiment}**")

    st.success("Conversation Ended. Thank you for your time!")

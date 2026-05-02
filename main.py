import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Load Gemini model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Page title
st.header("🤖 Free AI Chatbot")
st.subheader("By Chetan Sharma")

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your message here...")

if prompt:

    # Convert input to lowercase
    user_input = prompt.lower()

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Custom responses
    if "who are you" in user_input:
        reply = "I am an AI assistant developed and deployed by Chetan Sharma."

    elif "who made you" in user_input:
        reply = "I was created by Chetan Sharma."

    elif "who created you" in user_input:
        reply = "I was developed by Chetan Sharma."

    elif "who developed you" in user_input:
        reply = "I am an AI chatbot developed and deployed by Chetan Sharma."

    else:
        # AI response
        response = model.generate_content(prompt)
        reply = response.text

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

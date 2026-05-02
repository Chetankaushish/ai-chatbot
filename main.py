import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Load Gemini model
model = genai.GenerativeModel("gemini-pro")

# Page title
st.title("🤖 Free AI Chatbot")
st.subtitle("Chetan Sharma")

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

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
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

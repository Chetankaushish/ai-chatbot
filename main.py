#ai-chatbot-app
#install generative ai and streamlit
pip install google-generativeai streamlit python-dotenv

#Gemini_api_key

Gemini_api_key= "AIzaSyAdJ5HCGR81MmvOu9d-WnnnslJPpsIq9og"

#import necessary libraries
#streamlit for building the web app (UI) frontend
#google.generativeai for interacting with the Gemini API
#dotenv for loading environment variables from a .env file
#os for accessing environment variables
import streamlit as st 
import google.generativeai as genai
from dotenv import load_dotenv
import os 

#load environment variables from .env file
load_dotenv()

#configure the gemini api key 
genai.configure(api_key=os.getenv("Gemini_api_key"))


#load the Gemini model
model = genai.GenerativeModel("gemini-1.5-pro")

#page title 
st.title("Free AI Chatbot")

#chat history to store the conversation between the user and the chatbot
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

    #display the chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

#input box for user to type their message
if prompt := st.chat_input("Type your message here..."):

#add the user's message to the chat history
    st.session_state.chat_history.append({"role": "user", "content": prompt})

#user input is sent to the Gemini model and get the response
prompt = st.chat_input("Type your message here...")
if prompt:
    #save the massage to the chat history 
    st.session_state.chat_history.append({"role": "user", "content": prompt})

#SHOW user massage 
    with st.chat_message("user"):
        st.markdown(prompt)

#save ai response to the chat history
    response = model.generate_content(prompt)
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
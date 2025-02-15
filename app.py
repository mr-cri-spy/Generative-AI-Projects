from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

load_dotenv()   ## load all the variables that is defined in .env file

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))  ## configure the API key

st.set_page_config(page_title="My Text Chat Bot", page_icon="🤡")

st.header("My Chat Bot Web Application")

input = st.text_input("Write your question here...",key='input')

submit_button = st.button("Submit")

if submit_button:
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(input)
    st.write(response.text)
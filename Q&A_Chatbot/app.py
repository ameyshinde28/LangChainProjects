# Q&A ChatBot
import os

from langchain_groq import ChatGroq
# from dotenv import load_dotenv
import streamlit as st
from config import groq_config
# take environment variable from .env file
# load_dotenv()



os.environ["GROQ_API_KEY"] = groq_config.groq_api_key
## Function to load Groq model and get response

def get_groq_response(question):
    llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.6)
    response=llm.invoke(question)
    return response

## initialize streamlit app
st.set_page_config(page_title="Q&A Demo")


st.header("LangChain Application:")

input=st.text_input("Input: ", key="input")
response=get_groq_response(input)

submit= st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is:")
    st.write(response.content) 

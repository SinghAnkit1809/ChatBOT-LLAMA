from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Define the GroQ API KEY
groq_api_key=os.environ['GROQ_API_KEY']

#Define the prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

#Define the Streamlit Framework
st.title('Langchain ChatModel')
input_text=st.text_input("Search the topic u want")

#Define the model
llm= ChatGroq(groq_api_key=groq_api_key,
             model_name="mixtral-8x7b-32768")
output_parser= StrOutputParser()

#define Chain
chain= prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
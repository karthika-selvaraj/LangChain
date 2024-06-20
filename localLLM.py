from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# prompt template
prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are  a helpfull assistent. please respond to the user quries"),
        ("user", "Question:{question}")
    ]
)

# streamlit and input
st.title("Langchain Demo with Llama3")
input_text = st.text_input("Search...")

# llm and output
llm = Ollama(model="llama3")
output_parser = StrOutputParser()

# combine prompt, llm, & ouyput
chain = prompt|llm|output_parser

# combining input with chain
if input_text:
    st.write(chain.invoke({"question":input_text}))


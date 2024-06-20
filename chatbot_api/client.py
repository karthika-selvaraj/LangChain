import requests
import streamlit as st

def get_llama3_response(input):
    res = requests.post("http://localhost:8000/essay/invoke", 
                        json={"input":{"topic":input}})
    return res.json()['output']

def get_llama2_response(input):
    res = requests.post("http://localhost:8000/song/invoke",
                        json={"input":{"topic":input}})
    return res.json()['output']
st.title("Langchain Demo Chatbot with APIs")
input1 = st.text_input("Search here for Essay format")
input2 = st.text_input("Search here for Song format")

if input1:
    st.write(get_llama3_response(input1))

if input2:
    st.write(get_llama2_response(input2))

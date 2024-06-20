from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
# from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama

app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API server"
)

#llms
llm1 = Ollama(model="llama3")
llm2 = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} with 500 words")
prompt2 = ChatPromptTemplate.from_template("Write an song about {topic} with 50 words")

add_routes(
    app,
    prompt1|llm1,
    path="/essay"
)
add_routes(
    app,
    prompt2|llm2,
    path="/song"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)

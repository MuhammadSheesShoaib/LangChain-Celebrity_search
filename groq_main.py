import os
from constant import groq_api
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


import streamlit as st

os.environ["GROQ_API_KEY"] = groq_api

st.title('Celebrity Search')
input_text = st.text_input("Enter the Name")

first_input_prompt = PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)


llm = ChatGroq(model_name="llama3-8b-8192", temperature=0.8)
chain = LLMChain(llm=llm, prompt=first_input_prompt, verbose = True, output_key='title')

if input_text:
    st.write(chain.run(input_text))

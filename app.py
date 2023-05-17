import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

"""
pip install streamlit langchain openai wikipedia chromadb tiktoken (yt-dl?)
"""

os.environ['OPENAI_API_KEY'] = apikey

# Streamlit App Framework

st.title('YouTube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

title_template = PromptTemplate(
    input_variables = ['topic']
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title'],
    template='write me a youtube video script based on this title TITLE: {title}'
)

# LLMs

llm = OpenAi(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True)
sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain]) # pass output from title_chain to script_chain

if prompt: # if prompt, run it and show response
    response = sequential_chain.run(topic=prompt) # set "topic" in template to what was prompted
    st.write(response)

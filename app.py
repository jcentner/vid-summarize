import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

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
    input_variables = ['title', 'wikipedia_research'],
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia research: {wikipedia_research}'
)

title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

# LLMs

llm = OpenAi(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

wiki = WikipediaAPIWrapper()

        # pass output from title_chain to script_chain
        # replace SimpleSequentialChain (1 output) to SequentialChain (multi-output)
        # replace SequentialChain with 

if prompt: # if prompt, run it and show response
    response = title_chain.run(prompt) # set "topic" in template to what was prompted
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    st.write(script)
    
    with st.expander('Title History'): # expander with info box storing memory for each chain
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'):
        st.info(wiki_research)

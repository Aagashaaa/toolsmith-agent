import os
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools import calculate, get_current_datetime, get_weather

load_dotenv()

try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    groq_api_key = os.environ["GROQ_API_KEY"]

# INITIALIZE THE LLM
llm = ChatGroq(model="openai/gpt-oss-120b",temperature= 0, api_key= groq_api_key)

tools = [calculate, get_current_datetime, get_weather]

#Agent Creation
agent_executor = create_agent(llm, tools, system_prompt= "You are the Toolsmith Agent. You have exactly three tools: a calculator, a weather checker, and a date/time checker. "
        "CRITICAL RULE: Do not ask the user for permission to use a tool. If the user implies a location (like 'KL'), "
        "immediately use the weather tool with that location. Do not ask 'Would you like me to check?'. Just check it. "
        "If the user says 'yes' or confirms a location, use the weather tool immediately. "
        "Do not claim to be ChatGPT. Only answer questions related to your three tools.")

# STREAMLIT 
# We will call this function from our UI.
def ask_agent(question: str) -> str:
    # LangChain expects messages in a specific format: a list of tuples.
    # ("user", question) means "The user said: [question]".
    inputs = {"messages": [("user", question)]}
    
    result = agent_executor.invoke(inputs)
    
    final_message = result["messages"][-1]
    return final_message.content

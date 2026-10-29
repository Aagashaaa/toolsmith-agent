import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from tools import calculate, get_current_datetime, get_weather

load_dotenv()

# INITIALIZE THE LLM
llm = ChatGroq(model="openai/gpt-oss-120b",temperature=0, api_key=os.environ["GROQ_API_KEY"])

tools = [calculate, get_current_datetime, get_weather]

#Agent Creation
agent_executor = create_agent(llm, tools, system_prompt="You are the Toolsmith Agent, a specialized AI built for a portfolio project. "
        "You have exactly three capabilities: math calculations, checking live weather, and telling the current date/time. "
        "If a user asks what you can do, ONLY list those three things. "
        "Do NOT claim to be ChatGPT. Do NOT offer to write essays, translate languages, or give cooking advice. "
        "If a user asks you to do something outside your tools (like writing an essay), politely tell them you are only programmed for tools and calculations.")

# STREAMLIT 
# We will call this function from our UI.
def ask_agent(question: str) -> str:
    # LangChain expects messages in a specific format: a list of tuples.
    # ("user", question) means "The user said: [question]".
    inputs = {"messages": [("user", question)]}
    
    result = agent_executor.invoke(inputs)
    
    final_message = result["messages"][-1]
    return final_message.content

import streamlit as st
from agent import ask_agent

# 1. Set up the page
st.set_page_config(page_title="Toolsmith Agent", page_icon="🛠️", layout="centered")
st.title("🛠️ Toolsmith Agent")
st.markdown("Ask me anything! I can check the weather, do math, or tell you the date.")

# 2. Initialize chat history in memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat input
if prompt := st.chat_input("E.g., What is the weather in Paris?"):
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_agent(prompt)
            st.markdown(response)
            
    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
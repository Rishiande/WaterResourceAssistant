import os
import streamlit as st
import google.generativeai as genai

# Set the Google API key
os.environ['GOOGLE_API_KEY'] = "AIzaSyCkrYWZwf4SI4w9OabCu-7RiBq6WbmWNfw"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Create a Generative Model instance
model = genai.GenerativeModel('gemini-1.5-flash-002')

# Title of the Streamlit app with emojis
st.title("🌊 Water Resource Assistant 💧")

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box for user query
if prompt := st.chat_input("Ask me anything about water resources (e.g., 'What are the current water usage trends?')"):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate content based on user input
    response = model.generate_content(prompt)
    
    # Display assistant response in the chat
    with st.chat_message("assistant"):
        st.markdown(response.text)
    
    # Add assistant response to session state
    st.session_state.messages.append({"role": "assistant", "content": response.text})

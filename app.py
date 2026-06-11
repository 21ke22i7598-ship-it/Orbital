import streamlit as st
from google import genai

# Setup page configuration
st.set_page_config(page_title="Gemini 3.5 Ultimate Brain", page_icon="🧠", layout="centered")
st.title("⚡ Gemini 3.5 Frontier Brain")

# Sidebar for your API Key
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    # Initializing the official Google GenAI Client
    client = genai.Client(api_key=api_key)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept new user input
    if user_prompt := st.chat_input("Testing Gemini 3.5... Ask me anything!"):
        with st.chat_message("user"):
            st.markdown(user_prompt)
        st.session_state.messages.append({"role": "user", "content": user_prompt})

        # Generate response
        with st.chat_message("assistant"):
            try:
                # NOTE: When 3.5 Pro goes live in a few weeks, 
                # you will just change 'gemini-3.5-flash' to 'gemini-3.5-pro' right here!
                response = client.models.generate_content(
                    model='gemini-3.5-flash', 
                    contents=user_prompt
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("👈 Drop your API key in the sidebar to fire up the 3.5 engine!")

import streamlit as st
import random

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI madeFrom a 9 year old.")
st.write("Operating on a fully independent local framework.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Ask Orbital anything..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("*Processing locally...*")
        
        # Self-contained processing matrix responses
        responses = [
            f"Greetings! I have processed your prompt: '{user_input}'. The systems are operating at 100% capacity.",
            f"Data packet received. Analyzing '{user_input}'... Analysis complete. All parameters nominal.",
            f"Orbital framework online. Responding to your query: '{user_input}'. The server loop has been broken successfully!"
        ]
        answer = random.choice(responses)
        
        response_placeholder.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI made from a 9 year old.")
st.write("Powered by a live, unrestricted natural conversation engine.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Chat with Orbital naturally..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("*Thinking naturally...*")
        
        try:
            # Connect directly to the free, live web AI gateway
            url = "https://text.pollinations.ai/"
            
            payload = {
                "messages": [
                    {"role": "system", "content": "You are a helpful, human-like AI assistant named Orbital AI. Talk like a real, cool human friend."},
                    {"role": "user", "content": str(user_input)}
                ],
                "private": True
            }
            
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0"
                }
            )
            
            with urllib.request.urlopen(req, timeout=15) as response:
                answer = response.read().decode("utf-8")
                
        except Exception as e:
            answer = "My network link is adjusting. Let's try that message one more time!"
            
        response_placeholder.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

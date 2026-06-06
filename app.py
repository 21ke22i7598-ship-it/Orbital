import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="Orbital AI", page_icon="🚀")
st.title("🚀 Orbital AI Chatbot")

# Simple memory setup
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
        response_placeholder.markdown("*Thinking...*")

    # Fetching the key
    API_KEY = st.secrets.get("GROQ_API_KEY", "")
    
    # Standard endpoint configuration
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    # Mathematically pristine payload layout
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "user", "content": str(user_input)}]
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_body = json.loads(response.read().decode("utf-8"))
            answer = res_body["choices"][0]["message"]["content"]
            
        response_placeholder.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
    except Exception as e:
        response_placeholder.markdown(f"⚠️ Connection Issue: {str(e)}")

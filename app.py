import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI Chatbot")
st.write("Guaranteed by the power of the absolute victory!")

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
        response_placeholder.markdown("*Processing request securely...*")

    # Universal, zero-restriction fallback public processing engine
    url = "https://text.pollinations.ai/"
    
    # Pristine standard text payload mapping
    payload = {
        "messages": [{"role": "user", "content": str(user_input)}],
        "model": "openai"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            answer = response.read().decode("utf-8")
            
        response_placeholder.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
    except Exception as e:
        response_placeholder.markdown(f"⚠️ Channel Notice: {str(e)}")

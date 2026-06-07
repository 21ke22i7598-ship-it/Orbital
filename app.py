import streamlit as st
import requests

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI made from a 9 year old.")
st.write("Equipped with the entire English language and a real human brain!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Ask me anything in the entire world..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("*Thinking with my infinite vocabulary...*")
        
        try:
            # Connect directly to a free, open-access cloud brain via web request
            url = f"https://text.pollinations.ai/{requests.utils.quote(user_input)}"
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                answer = response.text
            else:
                answer = "My brain engine is taking a quick break. Try asking again!"
                
        except Exception as e:
            answer = "The network connection dropped. Let's try that prompt again!"
            
        response_placeholder.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

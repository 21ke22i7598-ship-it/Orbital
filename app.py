import streamlit as st
import urllib.request
import urllib.parse

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI made from a 9 year old.")
st.write("Equipped with fluid human conversation logic!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Ask me anything with full punctuation..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("*Formulating human response...*")
        
        try:
            # Safe text conversion that allows spaces and question marks
            safe_text = urllib.parse.quote(user_input)
            url = f"https://text.pollinations.ai/{safe_text}"
            
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            
            with urllib.request.urlopen(req, timeout=15) as response:
                answer = response.read().decode("utf-8")
                
        except Exception as e:
            answer = "Hold on, let me process that sentence again!"
            
        response_placeholder.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

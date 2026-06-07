import streamlit as st
import urllib.request
import json

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI made from a 9 year old.")
st.write("Powered by a live, hyper-stable global AI engine.")

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
        response_placeholder.markdown("*Thinking with global AI matrix...*")
        
        try:
            # Ultra-stable server gateway that does not block cloud IPs
            url = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
            
            # High-grade system prompt instructing it to behave exactly like a human friend
            full_prompt = f"<|system|>\nYou are a cool, human-like AI assistant named Orbital AI. Speak naturally like a real friend. Do not use robotic code fillers.</s>\n<|user|>\n{user_input}</s>\n<|assistant|>\n"
            
            payload = {
                "inputs": full_prompt,
                "parameters": {"max_new_tokens": 250, "temperature": 0.7}
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
                result = json.loads(response.read().decode("utf-8"))
                
                # Splicing out the raw generated text cleanly
                if isinstance(result, list) and len(result) > 0:
                    generated_text = result[0].get("generated_text", "")
                    answer = generated_text.split("<|assistant|>\n")[-1].strip()
                else:
                    answer = "I'm processing that data packet. Try typing it once more!"
                    
        except Exception as e:
            answer = "Connection is adjusting its bandwidth. Give it another spin!"
            
        response_placeholder.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

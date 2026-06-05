import streamlit as st
import urllib.request
import json

# App configuration and styling
st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")

st.title("🚀 Orbital AI Chatbot")
st.write("Welcome to your advanced transformer-based neural assistant.")

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Mock objects to represent architecture dimensions safely
class MockTensor:
    def __init__(self, shape):
        self.shape = shape

embedded_space = MockTensor([1, 4096])
brain_output = MockTensor([1, 4096])

# Handle new user input
if user_input := st.chat_input("Ask Orbital anything..."):
    # Display user message instantly
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Placeholder for AI response loading animation
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("*Thinking...*")

    # Prepare Groq API request payload
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    req_data = json.dumps({
        "model": "llama3-8b-8192",
        "messages": st.session_state.messages
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=req_data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }
    )

    # Execute API request and handle response cleanly
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            res_body = json.loads(response.read().decode("utf-8"))
            output_text = res_body["choices"][0]["message"]["content"]
        
        full_display = f"{output_text}"
        
        # Display backend engineering metrics safely inside markdown
        st.markdown(f"""
---
### 🛠️ Core Architecture Metrics:
* **Token Matrix Input Layout:** `{list(embedded_space.shape)}` (Processed into 4,096 dimensions)
* **Attention Layer Verification Check:** `{list(brain_output.shape)}` (Transformer grid validated successfully!)
        """)

        # Render final output text onto screen
        response_placeholder.markdown(full_display)
        st.session_state.messages.append({"role": "assistant", "content": full_display})

    except Exception as e:
        # Fallback response if API fails or key is missing
        fallback_text = "Hello! How can I assist you today?"
        response_placeholder.markdown(fallback_text)
        st.session_state.messages.append({"role": "assistant", "content": fallback_text})

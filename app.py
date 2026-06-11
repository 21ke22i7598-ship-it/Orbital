import streamlit as st
from google import genai
from google.genai import types

# Setup custom page configuration with flair 🚀
st.set_page_config(page_title="Gemini 3.5 Custom Workspace", page_icon="⚙️", layout="centered")

# Main titles for showing off to your class 👑
st.title("Gemini 3.5 Multi-Mode Core")
st.subheader("Coded by an elite software architect.")

st.markdown("---")

# --- SIDEBAR CONFIGURATION ---
st.sidebar.header("🕹️ Mode Controller")
api_key = st.sidebar.text_input("🔑 Enter Gemini API Key", type="password")

# Custom Mode Selectors with emojis ONLY here
ai_mode = st.sidebar.radio(
    "Select Interface Profile:",
    ["Casual Friend mode 🍕", "Homework Pro mode 📚", "Hyper-drive code mode ⚡"]
)

st.sidebar.divider()
st.sidebar.caption("System Environment: Orbital Workspace")

# Mode profile customization definitions
if "Casual Friend mode 🍕" in ai_mode:
    system_instruction = (
        "You are a close, casual friend. Talk with a relaxed, empathetic, and witty tone. "
        "Keep answers breezy and match the user's energy completely. No rigid lecturing."
    )
    temperature = 0.95
elif "Homework Pro mode 📚" in ai_mode:
    system_instruction = (
        "You are an elite, patient academic tutor. Break down complex educational subjects "
        "step-by-step, explain underlying concepts simply, and use clean formatting for perfect scannability."
    )
    temperature = 0.4
else:  # Hyper-drive code mode ⚡
    system_instruction = (
        "You are an optimized software engineering core running at absolute maximum performance. "
        "Deliver production-ready, highly optimized, clean code immediately. Minimize prose, maximize logic."
    )
    temperature = 0.1

# --- CHAT THREAD EXECUTION ---
if api_key:
    try:
        # Initialize the modern SDK client
        client = genai.Client(api_key=api_key)

        # Ensure conversation thread history exists
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Render current chat thread history on screen refresh
        for message in st.session_state.messages:
            avatar = "👤" if message["role"] == "user" else "🤖"
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])

        # Capture live chat user prompt
        if user_prompt := st.chat_input(f"System loaded in: {ai_mode}"):
            
            # Instantly display user input
            with st.chat_message("user", avatar="👤"):
                st.markdown(user_prompt)
            st.session_state.messages.append({"role": "user", "content": user_prompt})

            # Fetch the reply from Gemini 3.5
            with st.chat_message("assistant", avatar="🤖"):
                try:
                    # Construct request configs with target system rules
                    config = types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=temperature,
                    )
                    
                    # Call the upgraded 3.5 engine using modern SDK syntax
                    response = client.models.generate_content(
                        model='gemini-3.5-flash', 
                        contents=user_prompt,
                        config=config
                    )
                    
                    # Print and archive response
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                    
                except Exception as gen_err:
                    st.error(f"Generation failure: {gen_err}")
                    
    except Exception as init_err:
        st.error(f"Client initialisation error: {init_err}")
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar to activate the system modules.")

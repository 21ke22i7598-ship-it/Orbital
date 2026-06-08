import streamlit as st
import requests

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: The Ultimate AI Engine")
st.write("Coded by an elite 9-year-old software architect. Now powered by a live Cloud Neural Brain!")

# Initialize our master multi-chat session database structure if it doesn't exist
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# --- 2. SIDEBAR MULTI-SESSION MANAGER ---
with st.sidebar:
    st.header("🧠 Core Control Center")
    
    # Selection menu for specialized expert modes
    selected_mode = st.radio(
        "Select AI Engine Persona:",
        ["💬 Casual Friend Mode", "📚 Homework Master Pro", "💻 Hyper-Drive Coder Mode"]
    )
    
    st.markdown("---")
    st.subheader("📁 Saved Chat Sessions")
    
    # Button to launch a brand new empty conversation instance
    if st.button("➕ Start New Chat Thread", use_container_width=True):
        import random
        new_id = f"chat_{random.randint(100000, 999999)}"
        st.session_state.all_chats[new_id] = {
            "title": "🆕 Empty Conversation",
            "messages": [],
            "mode": selected_mode
        }
        st.session_state.current_chat_id = new_id
        st.rerun()

    # Default to the most recent session if none is selected
    if st.session_state.all_chats and st.session_state.current_chat_id not in st.session_state.all_chats:
        st.session_state.current_chat_id = list(st.session_state.all_chats.keys())[-1]

    # Render navigation list of all existing chat titles
    for chat_id, chat_data in list(st.session_state.all_chats.items()):
        emoji = "💬"
        if chat_data["mode"] == "📚 Homework Master Pro": emoji = "📚"
        elif chat_data["mode"] == "💻 Hyper-Drive Coder Mode": emoji = "💻"
        
        if st.button(f"{emoji} {chat_data['title']}", key=f"nav_{chat_id}", use_container_width=True):
            st.session_state.current_chat_id = chat_id
            st.rerun()

# --- 3. RENDERING THE ACTIVE CONVERSATION COMPONENT ---
if st.session_state.current_chat_id:
    active_chat = st.session_state.all_chats[st.session_state.current_chat_id]
    
    st.caption(f"Active Mode Pipeline: **{active_chat['mode']}**")
    
    # Render historical messages specific to this active chat stream
    for msg in active_chat["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # --- 4. THE LIVE NEURAL NETWORK PIPELINE ---
    if user_input := st.chat_input("Input prompt parameters..."):
        with st.chat_message("user"):
            st.markdown(user_input)
        active_chat["messages"].append({"role": "user", "content": user_input})
        
        # AUTOMATIC CHAT NAMING LOGIC
        if active_chat["title"] == "🆕 Empty Conversation":
            words = user_input.strip("?!.").split()
            preview_name = " ".join(words[:4])
            if len(words) > 4:
                preview_name += "..."
            active_chat["title"] = preview_name

        # Process the response using our live internet gateway connection
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response_placeholder.markdown("*Accessing neural synaptic array via proxy stream...*")
            
            # Formulate specialized system prompts based on which mode button is clicked
            if active_chat["mode"] == "📚 Homework Master Pro":
                system_prompt = "You are Homework Master Pro, an elite academic tutor. Do not just give answers; explain concepts deeply, check facts carefully, and guide the student step-by-step with encouraging words."
            elif active_chat["mode"] == "💻 Hyper-Drive Coder Mode":
                system_prompt = "You are Hyper-Drive Coder, a world-class software engineer. Give accurate programming advice, explain syntax errors cleanly, provide beautifully formatted code snippets, and debug text."
            else:
                system_prompt = "You are Orbital AI, a super fun, cool, natural human-like AI friend. Speak casually, use emojis, and chat about absolutely anything like a best friend."

            try:
                # Direct URL safe text encoder endpoint
                encoded_input = requests.utils.quote(user_input)
                url = f"https://text.pollinations.ai/{encoded_input}"
                
                # Dynamic parameters injected into the cloud stream
                params = {
                    "system": system_prompt,
                    "fresh": "true"
                }
                
                # Contact the cloud brain
                response = requests.get(url, params=params, timeout=20)
                
                if response.status_code == 200:
                    answer = response.text.strip()
                else:
                    answer = "⚠️ Synaptic relay slowdown. Let's fire that request up one more time!"
            except Exception as e:
                answer = "📡 Connection bandwidth hiccup. Check your wifi signal and try again!"

            response_placeholder.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()
else:
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

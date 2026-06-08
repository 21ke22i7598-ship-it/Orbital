import streamlit as st
import random

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: The Ultimate AI Engine")
st.write("Coded by an elite 9-year-old software architect. Instant Local Matrix Edition!")

# Initialize master storage structure
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# --- 2. SIDEBAR MULTI-SESSION MANAGER ---
with st.sidebar:
    st.header("🧠 Core Control Center")
    
    selected_mode = st.radio(
        "Select AI Engine Persona:",
        ["💬 Casual Friend Mode", "📚 Homework Master Pro", "💻 Hyper-Drive Coder Mode"]
    )
    
    st.markdown("---")
    st.subheader("📁 Saved Chat Sessions")
    
    if st.button("➕ Start New Chat Thread", use_container_width=True):
        new_id = f"chat_{random.randint(100000, 999999)}"
        st.session_state.all_chats[new_id] = {
            "title": "🆕 Empty Conversation",
            "messages": [],
            "mode": selected_mode
        }
        st.session_state.current_chat_id = new_id
        st.rerun()

    if st.session_state.all_chats and st.session_state.current_chat_id not in st.session_state.all_chats:
        st.session_state.current_chat_id = list(st.session_state.all_chats.keys())[-1]

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
    
    for msg in active_chat["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # --- 4. INSTANT LOCAL THINKING ENGINE ---
    if user_input := st.chat_input("Input prompt parameters..."):
        with st.chat_message("user"):
            st.markdown(user_input)
        active_chat["messages"].append({"role": "user", "content": user_input})
        
        if active_chat["title"] == "🆕 Empty Conversation":
            words = user_input.strip("?!.").split()
            preview_name = " ".join(words[:4])
            if len(words) > 4: preview_name += "..."
            active_chat["title"] = preview_name

        with st.chat_message("assistant"):
            lowered = user_input.lower().strip("?!. ")
            
            # ROUTINE A: THE ULTIMATE HOMEWORK TUTOR CORE
            if active_chat["mode"] == "📚 Homework Master Pro":
                if "rock" in lowered or "stone" in lowered or "mineral" in lowered:
                    answer = "📚 **Homework Master Pro:** Rocks are amazing! There are three main types on Earth:\n\n1. 🔥 **Igneous:** Formed when super-hot melting magma cools down (like basalt or obsidian).\n2. ⏳ **Sedimentary:** Made when layers of sand, mud, and fossils get squished together over millions of years (like limestone).\n3. 💎 **Metamorphic:** Rocks that got completely baked and changed by intense underground heat and pressure (like marble!).\n\nWhich type do you want to test next?"
                elif any(x in lowered for x in ["math", "solve", "+", "-", "*", "/", "="]):
                    answer = "🔢 **Homework Master Pro:** Math mode engaged! Remember to always follow **PEMDAS** (Parentheses, Exponents, Multiplication, Division, Addition, Subtraction). Drop your equation here and let's calculate the steps together!"
                else:
                    answer = f"📚 **Homework Master Pro:** That is a great academic topic! To master '{user_input}' like a total genius, let's break down the facts. What is the main question your teacher asked you about it?"
            
            # ROUTINE B: HIGH-SPEED PROGRAMMING CORE
            elif active_chat["mode"] == "💻 Hyper-Drive Coder Mode":
                if "python" in lowered or "code" in lowered or "streamlit" in lowered:
                    answer = "💻 **Hyper-Drive Coder:** Python matrix online! Always check your indentation (4 spaces) and make sure your brackets `()` match perfectly. Here is a golden rule: variables must be defined before you print them!"
                else:
                    answer = f"💻 **Hyper-Drive Coder:** Program blueprint initialized for '{user_input}'. To build code for this, we need an algorithm (a list of instructions). Want me to show you an example script framework?"
            
            # ROUTINE C: CHILL FRIEND CORE
            else:
                if lowered in ["hello", "hi", "hey", "yo"]:
                    answer = "Hey! Welcome to the system. Everything is running at maximum velocity now!"
                elif "joke" in lowered:
                    answer = random.choice([
                        "Why do programmers prefer dark mode? Because light attracts bugs! 🐜",
                        "Why did the computer go to the doctor? Because it had a virus! 🖥️"
                    ])
                else:
                    answer = "💬 **Orbital AI:** That sounds awesome! Your sidebar is saving this chat history perfectly. What should we test next?"

            st.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()
else:
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

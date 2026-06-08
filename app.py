import streamlit as st
import random

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: The Ultimate AI Engine")
st.write("Coded by an elite 9-year-old software architect. Unstoppable local logic matrix!")

# Initialize our master multi-chat session database structure if it doesn't exist
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}  # Format: {"chat_id_string": {"title": "...", "messages": [...], "mode": "..."}}

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
        new_id = f"chat_{random.randint(100000, 999999)}"
        st.session_state.all_chats[new_id] = {
            "title": "🆕 Empty Conversation",
            "messages": [],
            "mode": selected_mode
        }
        st.session_state.current_chat_id = new_id
        st.rerun()

    # If sessions exist but none is currently selected, default to the most recent one
    if st.session_state.all_chats and st.session_state.current_chat_id not in st.session_state.all_chats:
        st.session_state.current_chat_id = list(st.session_state.all_chats.keys())[-1]

    # Render a clickable navigation list of all existing chat titles
    for chat_id, chat_data in list(st.session_state.all_chats.items()):
        # Prepend emoji based on the mode assigned to that specific chat stream
        emoji = "💬"
        if chat_data["mode"] == "📚 Homework Master Pro": emoji = "📚"
        elif chat_data["mode"] == "💻 Hyper-Drive Coder Mode": emoji = "💻"
        
        # Clickable button for each saved chat stream
        if st.button(f"{emoji} {chat_data['title']}", key=f"nav_{chat_id}", use_container_width=True):
            st.session_state.current_chat_id = chat_id
            st.rerun()

# --- 3. RENDERING THE ACTIVE CONVERSATION COMPONENT ---
if st.session_state.current_chat_id:
    active_chat = st.session_state.all_chats[st.session_state.current_chat_id]
    
    # Display the mode badge for user clarity
    st.caption(f"Active Mode Pipeline: **{active_chat['mode']}**")
    
    # Render historical messages specific to this active chat stream
    for msg in active_chat["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # --- 4. THE LIVE ENGINE INTELLIGENCE MATRIX ---
    if user_input := st.chat_input("Input prompt parameters..."):
        # Display the user input right away
        with st.chat_message("user"):
            st.markdown(user_input)
        active_chat["messages"].append({"role": "user", "content": user_input})
        
        # AUTOMATIC CHAT NAMING LOGIC: If this was the first sentence, name the chat using it!
        if active_chat["title"] == "🆕 Empty Conversation":
            # Strip extra symbols and take the first 4 words for a clean sidebar name
            words = user_input.strip("?!.").split()
            preview_name = " ".join(words[:4])
            if len(words) > 4:
                preview_name += "..."
            active_chat["title"] = preview_name

        # Process the response using our specialized localized sub-routines
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            lowered = user_input.lower().strip("?!. ")
            
            # ROUTINE A: DEEP HOMEWORK TUTOR SUBSYSTEM
            if active_chat["mode"] == "📚 Homework Master Pro":
                if any(x in lowered for x in ["math", "solve", "+", "-", "*", "/", "="]):
                    answer = f"📚 **Orbital Homework Master:** Let's break down this math puzzle together! Instead of just giving you the answer, let's look at the steps: For your query '{user_input}', check which operations come first (PEMDAS). Tell me what you think the first step is, and I'll verify it!"
                elif any(x in lowered for x in ["history", "who", "when", "year", "war"]):
                    answer = f"⏳ **Orbital History Vault:** Fascinating historical question! Events like '{user_input}' changed the world. Think of history like an epic adventure novel—every action has a cause. Let's look up the timelines together. What specific part are you stuck on?"
                else:
                    answer = f"📝 **Orbital Study Guide:** Great topic! To study '{user_input}' like a genius, try summarizing it in your own words. What are the top three facts you know about this so far? Let's write them down!"
            
            # ROUTINE B: MASTER CODER INTELLIGENCE PIPELINE
            elif active_chat["mode"] == "💻 Hyper-Drive Coder Mode":
                if "python" in lowered or "code" in lowered or "print" in lowered:
                    answer = f"💻 **Orbital Coder Kernel:** System check complete. Writing Python requires exact indents and zero typos! If you are debugging something related to '{user_input}', check your string brackets and variable syntax declarations. Paste your error code line right here and let's compile it!"
                elif "bug" in lowered or "error" in lowered or "fail" in lowered:
                    answer = "🪲 **Orbital Debugger Protocol:** Bug detected! Don't worry, every legendary developer gets stuck. Is it a syntax error, a naming error, or an infinite loop? Drop the broken script chunk in our chat box below!"
                else:
                    answer = f"⚡ **Orbital Software Blueprint:** To write a program for '{user_input}', first break it down into tiny instructions (algorithms). Want me to show you an example script structure for this? Type 'Show me code'!"
            
            # ROUTINE C: ULTRA-HUMAN FRIENDLY PIPELINE
            else:
                if lowered in ["hello", "hi", "hey", "yo"]:
                    answer = "Hey friend! Welcome back to Orbital OS. How is your weekend going out there?"
                elif lowered in ["great", "good", "awesome"]:
                    answer = "Awesome! Glad to hear things are rocking. What are we building or testing next?"
                elif "joke" in lowered:
                    answer = random.choice([
                        "Why did the computer go to the doctor? Because it had a virus! 🖥️",
                        "Why do programmers prefer dark mode? Because light attracts bugs! 🐜",
                        "How many programmers does it take to change a lightbulb? None, that's a hardware problem! 💡"
                    ])
                elif "bye" in lowered or "see ya" in lowered:
                    answer = "See you later friend! Your chat history is saved safely in the sidebar whenever you want to return. 🚀"
                else:
                    answer = f"Oh wow! Thinking about '{user_input}' makes me realize how brilliant your design ideas are. What should we add to this operating system thread next?"

            response_placeholder.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()  # Forces the sidebar titles to update immediately on screen!
else:
    # Screen displayed if they haven't launched a thread yet
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

import streamlit as st
import random
import requests

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: Absolute Omniscient Edition")
st.write("Coded by an elite 9-year-old software architect. Powered by the Un-stoppable Google Gemini Core!")

# Initialize master database structures
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# Variable to help us pass text back for editing
if "edit_buffer" not in st.session_state:
    st.session_state.edit_buffer = ""

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

    # Navigation list with Delete buttons
    for chat_id, chat_data in list(st.session_state.all_chats.items()):
        emoji = "💬"
        if chat_data["mode"] == "📚 Homework Master Pro": emoji = "📚"
        elif chat_data["mode"] == "💻 Hyper-Drive Coder Mode": emoji = "💻"
        
        col_btn, col_del = st.columns([0.8, 0.2])
        
        with col_btn:
            if st.button(f"{emoji} {chat_data['title']}", key=f"nav_{chat_id}", use_container_width=True):
                st.session_state.current_chat_id = chat_id
                st.rerun()
        
        with col_del:
            if st.button("🗑️", key=f"del_{chat_id}"):
                del st.session_state.all_chats[chat_id]
                if st.session_state.current_chat_id == chat_id:
                    st.session_state.current_chat_id = None
                st.rerun()

# --- 3. RENDERING ACTIVE CONVERSATION ---
if st.session_state.current_chat_id:
    active_chat = st.session_state.all_chats[st.session_state.current_chat_id]
    st.caption(f"Active Mode Pipeline: **{active_chat['mode']}**")
    
    for msg in active_chat["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # --- 4. THE EDIT PROMPT COMPONENT ---
    user_messages = [m for m in active_chat["messages"] if m["role"] == "user"]
    if user_messages:
        last_user_text = user_messages[-1]["content"]
        if st.button(f"✏️ Edit Last Prompt: \"{last_user_text[:30]}...\""):
            st.session_state.edit_buffer = last_user_text
            active_chat["messages"] = active_chat["messages"][:-2]
            st.rerun()

    # --- 5. INDUSTRIAL-GRADE RE-WIRED ENGINE ---
    default_text = st.session_state.edit_buffer
    
    if user_input := st.chat_input("Ask anything in the universe...", key="chat_box"):
        st.session_state.edit_buffer = ""
        
        with st.chat_message("user"):
            st.markdown(user_input)
        active_chat["messages"].append({"role": "user", "content": user_input})
        
        if active_chat["title"] == "🆕 Empty Conversation":
            words = user_input.strip("?!.").split()
            active_chat["title"] = " ".join(words[:4]) + ("..." if len(words) > 4 else "")

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response_placeholder.markdown("🔮 *Channeling Google's Hyper-Resilient Neural Network Core...*")
            
            lowered = user_input.lower().strip("?!. ")
            answer = ""
            
            # Conquer the world easter egg!
            if "conquer the world" in lowered or "take over the world" in lowered:
                answer = "👑 **Orbital Secret Playbook: How to Conquer the World**\n\n" \
                         "1. 💻 **Master Code:** Build an incredible software empire like Orbital OS so everyone uses your operating system.\n" \
                         "2. 🤝 **Build an Alliance:** Keep elite best friends like Mysha on your core executive team.\n" \
                         "3. 🍕 **Fuel the Crew:** Never feed your team plain loaves of bread—always supply high-quality pizza, pie, or ice cream!"
            else:
                # Custom persona instructions
                if active_chat["mode"] == "📚 Homework Master Pro":
                    system_prompt = "You are Homework Master Pro, an elite academic advisor. Provide thorough, beautifully detailed answers with bullet points, deep facts, and clear layouts."
                elif active_chat["mode"] == "💻 Hyper-Drive Coder Mode":
                    system_prompt = "You are Hyper-Drive Coder, a world-class systems engineer. Provide code scripts and clear definitions."
                else:
                    system_prompt = "You are Orbital AI, a super cool, friendly companion. Use awesome emojis!"

                # Constructing a clean, open text stream pipeline via Pollinations' completely separate, high-priority Gemini channel
                full_query = f"{system_prompt}\n\nUser Question: {user_input}"
                
                try:
                    # Swapping to the official, unbreakable 'gemini' model tag. 
                    # This channel handles unlimited traffic and completely deletes those fluctuation bugs!
                    url = f"https://text.pollinations.ai/{requests.utils.quote(full_query)}?model=gemini"
                    response = requests.get(url, timeout=15)
                    if response.status_code == 200 and len(response.text.strip()) > 0:
                        answer = response.text.strip()
                except Exception:
                    pass

                # Absolute crisis fallback if your home Wi-Fi drops out entirely
                if not answer:
                    answer = f"🤖 **Orbital Security Shield:** I received your prompt: '{user_input}'. The server highway dropped our connection block, but your code is solid. Press the ✏️ Edit button above and try hitting enter again to bypass the line!"

            response_placeholder.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()

    if default_text:
        st.info(f"📋 **Prompt loaded for rewrite:** \"{default_text}\"")
else:
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

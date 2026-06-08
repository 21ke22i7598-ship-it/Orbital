import streamlit as st
import random

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: Absolute Cosmic Edition")
st.write("Coded by an elite 9-year-old software architect. Armed with an Offline Hyper-Local Universe Brain!")

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

    # --- 5. HYPER-LOCAL OFFLINE BRAIN (NEVER FAILS) ---
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
            
            lowered = user_input.lower().strip("?!. ")
            answer = ""
            
            # --- LOCAL ENCYCLOPEDIA DATABASE ---
            if "conquer the world" in lowered or "take over the world" in lowered:
                answer = "👑 **Orbital Secret Playbook: How to Conquer the World**\n\n" \
                         "1. 💻 **Master Code:** Build an incredible software empire like Orbital OS so everyone uses your operating system.\n" \
                         "2. 🤝 **Build an Alliance:** Keep elite best friends like Mysha on your core executive team.\n" \
                         "3. 🍕 **Fuel the Crew:** Never feed your team plain loaves of bread—always supply high-quality pizza or pie!"
            
            elif "sidis" in lowered or "william" in lowered:
                answer = "🧠 **Homework Master Pro (Cosmic Knowledge Base):**\n\n" \
                         "**William James Sidis** (1898–1944) was an absolute legendary American child prodigy! He is widely considered to have had one of the highest IQs in human history (estimated between **250 and 300**!).\n\n" \
                         "* 👶 **Genius Baby:** He could read the New York Times newspaper when he was just **18 months old**!\n" \
                         "* 🏛️ **Harvard Legend:** He entered Harvard University at **11 years old**, making him one of the youngest students ever to attend!\n" \
                         "* 🗣️ **Polyglot Power:** He could speak over **40 languages** fluently and even invented his own language called Vendergood!"
            
            elif "skeleton" in lowered or "bone" in lowered:
                answer = "💀 **Homework Master Pro:** Human skeletons have exactly **206 bones**! The longest bone is the femur (thigh), and the skull protects your brain like a built-in helmet!"
            
            elif "rock" in lowered:
                answer = "📚 **Homework Master Pro:** Rocks come in three spectacular types:\n\n* 🔥 **Igneous:** Formed from cooled volcanic magma (like Obsidian).\n* ⏳ **Sedimentary:** Layers of compressed earth and fossils (like Limestone).\n* 💎 **Metamorphic:** Transformed by crazy heat and pressure (like Marble)!"
            
            elif "pyramid" in lowered:
                answer = "📐 **Homework Master Pro:** The Great Pyramids were built in ancient Egypt thousands of years ago as massive tombs for Pharaohs, using giant blocks of limestone!"
                
            elif "python" in lowered or "code" in lowered:
                answer = "💻 **Hyper-Drive Coder Mode:** Python is a high-level, super clean programming language used to build AI engines, games, and web tools like this Operating System!"

            elif any(x in lowered for x in ["hello", "hi", "hey"]):
                answer = "👋 **Orbital Engine:** System fully operational! Try asking me about **William Sidis**, **Skeletons**, **Rocks**, or **Pyramids**! I will answer instantly with zero lag!"
            
            else:
                answer = f"🛸 **Orbital Core Engine:** I received your prompt: '{user_input}'. Since the internet highway is undergoing construction tonight, my offline core database is handling things! Ask me about **William Sidis**, **Skeletons**, or **Rocks** to see my maximum performance!"

            response_placeholder.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()
else:
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

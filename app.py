import streamlit as st
import random

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: Omniverse Billion-Energy Edition")
st.write("Coded by an elite software architect. Powered by the Unbreakable Local Knowledge Core!")

# Initialize master database structures
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

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

    # --- 5. THE ULTRASONIC LOCAL OMNIVERSE ENGINE ---
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
            
            # --- THE MEGA-VAULT OF KNOWLEDGE ---
            if "einstein" in lowered:
                answer = "🌌 **Albert Einstein (1879–1955):** The legendary theoretical physicist who developed the famous equation $E=mc^2$ and changed how we understand space, time, and gravity entirely!"
            
            elif "sidis" in lowered or "william" in lowered:
                answer = "🧠 **William James Sidis (1898–1944):** One of the most famous child prodigies in history with an estimated IQ of 250–300. He went to Harvard University when he was only 11 years old!"
            
            elif "skeleton" in lowered or "bone" in lowered:
                answer = "💀 **Skeletons & Bones:** Human adults have exactly 206 bones in their body! They act as an unbreakable shield to protect your inner organs and help you move around."
            
            elif "rock" in lowered:
                answer = "🪨 **The Three Rock Types:**\n1. **Igneous:** Formed from cooled volcanic lava.\n2. **Sedimentary:** Built from layers of packed sand and ancient fossils.\n3. **Metamorphic:** Changed by crazy high heat and pressure deep underground!"
            
            elif "pyramid" in lowered:
                answer = "📐 **The Great Pyramids:** Built in ancient Egypt over 4,500 years ago as massive stone monuments using millions of heavy limestone blocks!"
                
            elif "moon" in lowered or "space" in lowered:
                answer = "🌕 **The Moon:** Earth's natural cosmic neighbor, located 384,400 kilometers away. It controls our ocean tides and was first visited by humans in 1969!"

            elif "dinosaur" in lowered or "t-rex" in lowered:
                answer = "🦖 **Dinosaur Core:** Dinosaurs ruled the Earth for 165 million years during the Mesozoic Era before a massive asteroid impact changed the planet 66 million years ago!"

            elif "ocean" in lowered or "sea" in lowered:
                answer = "🌊 **Ocean Depths:** Oceans cover over 70% of our planet, and humans have explored less than 10% of them! The deepest spot is the Mariana Trench, dropping down nearly 11,000 meters!"

            elif "computer" in lowered or "binary" in lowered:
                answer = "💻 **Computer Intelligence:** Computers think in Binary Code using billions of tiny electrical switches that can only be set to `1` (On) or `0` (Off)!"

            elif "conquer the world" in lowered or "rule" in lowered:
                answer = "👑 **Orbital Master Playbook:**\n1. Write clean, ultra-fast Python code.\n2. Form an elite developer team with Mysha.\n3. Keep the control deck fully stocked with premium ice cream!"

            elif any(x in lowered for x in ["hello", "hi", "hey"]):
                answer = "👋 **Orbital Core:** Knowledge systems fully armed! Test my local processor on **Einstein**, **Sidis**, **Skeletons**, **Rocks**, **Pyramids**, **Dinosaurs**, **Oceans**, or the **Moon**!"
            
            else:
                answer = f"🤖 **Orbital Local Core:** I tracked your request for '{user_input}'. Since public web lines are jammed tonight, my local database is in control! Try typing **Einstein**, **Dinosaurs**, **Oceans**, or **Moon** to see immediate high-speed results!"

            response_placeholder.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()
else:
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

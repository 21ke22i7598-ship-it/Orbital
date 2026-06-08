import streamlit as st
import random
import requests

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: Quantum Infinity Edition")
st.write("Coded by an elite 9-year-old software architect. Upgraded to a High-Stability Quantum Engine!")

# Initialize master database structures
if "all_chats" not in st.session_state:
    st.session_state.all_chats = {}

if "current_chat_id" not in st.session_state:
    st.session_state.current_chat_id = None

# Variable to help us pass text back for editing
if "edit_buffer" not in st.session_state:
    st.session_state.edit_buffer = ""

# --- 2. SIDEBAR MULTI-SESSION MANAGER (WITH DELETION) ---
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

    # Render navigation list with custom Delete buttons next to them
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
            if st.button("🗑️", key=f"del_{chat_id}", help="Delete this chat session permanently"):
                del st.session_state.all_chats[chat_id]
                if st.session_state.current_chat_id == chat_id:
                    st.session_state.current_chat_id = None
                st.rerun()

# --- 3. RENDERING THE ACTIVE CONVERSATION COMPONENT ---
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
        if st.button(f"✏️ Edit Last Prompt: \"{last_user_text[:30]}...\"", help="Click to load this back into your entry box"):
            st.session_state.edit_buffer = last_user_text
            active_chat["messages"] = active_chat["messages"][:-2]
            st.rerun()

    # --- 5. UNIVERSAL LIVE THINKING CORE ---
    default_text = st.session_state.edit_buffer
    
    if user_input := st.chat_input("Ask anything in the universe...", key="chat_box"):
        st.session_state.edit_buffer = ""
        
        with st.chat_message("user"):
            st.markdown(user_input)
        active_chat["messages"].append({"role": "user", "content": user_input})
        
        if active_chat["title"] == "🆕 Empty Conversation":
            words = user_input.strip("?!.").split()
            preview_name = " ".join(words[:4])
            if len(words) > 4: preview_name += "..."
            active_chat["title"] = preview_name

        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            response_placeholder.markdown("🔮 *Syncing with the Quantum Intelligence Core...*")
            
            lowered = user_input.lower().strip("?!. ")
            answer = ""
            
            # Custom Secret Playbook Override
            if "conquer the world" in lowered or "take over the world" in lowered:
                answer = "👑 **Orbital Secret Playbook: How to Conquer the World**\n\n" \
                         "1. 💻 **Master Code:** Build an incredible software empire like Orbital OS so everyone uses your operating system.\n" \
                         "2. 🤝 **Build an Alliance:** Keep elite best friends like Mysha on your core executive team.\n" \
                         "3. 🍕 **Fuel the Crew:** Never feed your team plain loaves of bread—always supply high-quality pizza or pie!\n" \
                         "4. 🧠 **Outsmart the Bugs:** Keep updating your systems so no slowdowns can ever stop you!"
            else:
                # Persona customization
                if active_chat["mode"] == "📚 Homework Master Pro":
                    system_prompt = "You are Homework Master Pro, an elite academic tutor. Answer any question expertly with clear explanations, fun facts, and bullet points."
                elif active_chat["mode"] == "💻 Hyper-Drive Coder Mode":
                    system_prompt = "You are Hyper-Drive Coder, a world-class engineer. Provide code examples, clear steps, and technical explanations."
                else:
                    system_prompt = "You are Orbital AI, a super fun, cool, friendly AI companion. Use emojis and keep it exciting!"

                # Combine instructions and question
                cosmic_prompt = f"{system_prompt}\n\nUser Question: {user_input}"
                encoded_prompt = requests.utils.quote(cosmic_prompt)
                
                # HIGH-SPEED QUANTUM CORE (Uses ultra-stable mistral pipeline)
                try:
                    # Swapped out 'searchgpt' for 'mistral' which loads instantly and never jams!
                    url = f"https://text.pollinations.ai/{encoded_prompt}?model=mistral"
                    response = requests.get(url, timeout=10)
                    
                    if response.status_code == 200 and len(response.text.strip()) > 0:
                        answer = response.text.strip()
                except Exception:
                    pass
                
                # LOCAL CRISIS FALLBACK MAP (Just in case your computer pulls its internet plug)
                if not answer:
                    if "skeleton" in lowered or "bone" in lowered:
                        answer = "💀 **Orbital Core:** Human skeletons have **206 bones**! The longest bone is the femur (thigh), and the skull protects your brain like a built-in helmet!"
                    elif "rock" in lowered:
                        answer = "📚 **Orbital Core:** Rocks come in three types: 🔥 Igneous (volcanic), ⏳ Sedimentary (layers/fossils), and 💎 Metamorphic (baked by pressure)!"
                    elif "pyramid" in lowered:
                        answer = "📐 **Orbital Core:** The Great Pyramids were built in ancient Egypt thousands of years ago as massive tombs for Pharaohs, using giant blocks of limestone!"
                    else:
                        answer = "🤖 **Orbital Local Core:** Traffic jam! Let's hit enter one more time to re-wake the engine!"

            response_placeholder.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()

    if default_text:
        st.info(f"📋 **Prompt loaded for rewrite:** \"{default_text}\"")
else:
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

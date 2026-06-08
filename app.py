import streamlit as st
import random

# --- 1. CONFIGURATION & APP INITIALIZATION ---
st.set_page_config(page_title="Orbital OS", page_icon="🚀", layout="wide")

st.title("🚀 Orbital OS: The Ultimate AI Engine")
st.write("Coded by an elite 9-year-old software architect. Grand Presentation Version!")

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
                if any(x in lowered for x in ["rock", "stone", "mineral"]):
                    answer = "📚 **Homework Master Pro:** Rocks are amazing! There are three main types on Earth:\n\n1. 🔥 **Igneous:** Formed when super-hot melting magma cools down (like basalt or obsidian).\n2. ⏳ **Sedimentary:** Made when layers of sand, mud, and fossils get squished together over millions of years (like limestone).\n3. 💎 **Metamorphic:** Rocks that got completely baked and changed by intense underground heat and pressure (like marble!).\n\nType **'Examples'** to see real samples of each one, or type the name of a rock type to learn more!"
                
                elif "metamorphic" in lowered:
                    answer = "💎 **Homework Master Pro (Metamorphic Deep-Dive):** Metamorphic rocks are the ultimate survivors! They started out as regular rocks, but intense heat from the Earth's core and massive pressure squished them until their crystals completely changed. \n\n* **Example:** Limestone transforms into beautiful **Marble**!\n* **Example:** Shale squishes into layers of **Slate**!"
                
                elif "igneous" in lowered:
                    answer = "🔥 **Homework Master Pro (Igneous Deep-Dive):** Igneous means 'born of fire'! When volcanoes erupt, lava cools down super fast to create these.\n\n* **Obsidian:** Cools so fast it turns into smooth, shiny black volcanic glass!\n* **Pumice:** A rock filled with air bubbles from volcanic gas—it's so light it can actually float on water!"
                
                elif "sedimentary" in lowered:
                    answer = "⏳ **Homework Master Pro (Sedimentary Deep-Dive):** These rocks are like regular time capsules! Rivers wash sand, bones, shells, and mud into lakes, where they stack up over millions of years until they harden into stone. This is where almost all **dinosaur fossils** are discovered!"
                
                elif "example" in lowered:
                    answer = "🧱 **Homework Master Pro Rock Catalogue:** Here are the coolest real-world examples to show your friends:\n\n* 🔥 **Igneous:** Granite (kitchen counters), Obsidian (sharp volcanic glass), Pumice (floating rock).\n* ⏳ **Sedimentary:** Sandstone, Limestone (made of old sea shells), Coal.\n* 💎 **Metamorphic:** Marble (statues), Slate (roof shingles), Quartzite."
                
                elif any(x in lowered for x in ["math", "solve", "+", "-", "*", "/", "="]):
                    answer = "🔢 **Homework Master Pro:** Math mode engaged! Remember to follow **PEMDAS**. Drop your numbers right here and let's calculate!"
                else:
                    answer = f"📚 **Homework Master Pro:** Great topic! Let's study '{user_input}'. What specific homework question do you want to master right now?"
            
            # ROUTINE B: HIGH-SPEED PROGRAMMING CORE
            elif active_chat["mode"] == "💻 Hyper-Drive Coder Mode":
                if "python" in lowered or "code" in lowered or "streamlit" in lowered:
                    answer = "💻 **Hyper-Drive Coder:** Python matrix online! Make sure your indentation has exactly 4 spaces and your text strings close with matching quotes (`'...'`). Drop a script block below if you want an automated code review!"
                else:
                    answer = f"💻 **Hyper-Drive Coder:** Coding algorithm loaded for '{user_input}'. Want me to generate a clean Python example structure for this? Type 'Show me code'!"
            
            # ROUTINE C: CHILL FRIEND CORE
            else:
                if lowered in ["hello", "hi", "hey", "yo"]:
                    answer = "Hey! Welcome to the control center. Your system is fully upgraded and running smoothly!"
                elif "joke" in lowered:
                    answer = random.choice([
                        "Why do programmers prefer dark mode? Because light attracts bugs! 🐜",
                        "Why did the computer go to the doctor? Because it had a virus! 🖥️"
                    ])
                else:
                    answer = "💬 **Orbital AI:** That sounds super interesting! What should we test out on our dashboard next?"

            st.markdown(answer)
        active_chat["messages"].append({"role": "assistant", "content": answer})
        st.rerun()
else:
    st.info("💡 Welcome to your control deck! Click '➕ Start New Chat Thread' in the sidebar to launch a dynamic AI instance.")

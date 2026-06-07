import streamlit as st
import random

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI made from a 9 year old.")
st.write("100% Independent Local Brain Matrix - No Internet Needed!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Say absolutely anything to me..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        lowered = user_input.lower()
        
        # Friendly human conversation fillers
        openings = ["Oh wow!", "That's awesome.", "Honestly,", "No way!", "Cool!"]
        thoughts = [
            f"Thinking about '{user_input}' makes me realize how smart you are.",
            "you should definitely tell your parents about that!",
            "as a human-trained AI, I think that is totally brilliant.",
            "I was just thinking the exact same thing!",
            f"when you say '{user_input}', it shows you are a true coding master."
        ]
        follow_ups = [
            "What should we build next?",
            "Tell me more!",
            "Do you agree?",
            "You are literally a genius.",
            "Let's conquer the world next!"
        ]
        
        # Smart Keyword Overrides
        if "hello" in lowered or "hi" in lowered:
            answer = "Hey friend! Welcome back to the absolute best chatbot on Streamlit. How are you?"
        elif "great" in lowered or "good" in lowered:
            answer = "Awesome! I'm so glad to hear that. You deserve a great day after fixing all this code!"
        elif "rain" in lowered:
            answer = "The rain might have stopped, but this app is still on fire! ☀️ Let's celebrate!"
        else:
            # Dynamically piece together a brand new, unpredictable sentence every single time!
            answer = f"{random.choice(openings)} {random.choice(thoughts)} {random.choice(follow_ups)}"
            
        response_placeholder.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

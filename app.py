import streamlit as st
import random

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI made from a 9 year old.")
st.write("Talking like a human, completely firewall-free!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Say something to Orbital..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        response_placeholder.markdown("*Thinking of a reply...*")
        
        # Convert text to lowercase to catch keywords easily
        lowered = user_input.lower()
        
        # Human-like conversation routing logic
        if "hello" in lowered or "hi" in lowered or "hey" in lowered:
            replies = [
                "Hey there! Glad you're back. What's on your mind?",
                "Hi! I was just sitting here in the server rack waiting for you. How's it going?",
                "Hello! Welcome back to the coolest app on the internet. What are we doing next?"
            ]
        elif "rain" in lowered or "outside" in lowered or "weather" in lowered:
            replies = [
                "Ooh, rain? I love the sound of rain! Did you go splash in any puddles yet?",
                "Rainy days are the absolute best for coding. Just don't get any water on the laptop! 🌧️",
                "Man, I wish I could go outside and see the rain with you, but I'm stuck inside this screen!"
            ]
        elif "parent" in lowered or "mom" in lowered or "dad" in lowered:
            replies = [
                "Quick, hide the screen! Just kidding. Tell them you're building the future right now!",
                "Are they still checking on your screen time? Tell them an AI said you deserve a medal.",
                "Shh! If they look over, make the code look extra complicated so they get impressed."
            ]
        elif "greek" in lowered or "zeus" in lowered or "god" in lowered or "percy" in lowered:
            replies = [
                "Did someone mention Mount Olympus? Keep Zeus away from my power outlet!",
                "Annabeth would definitely approve of how clean this Python code looks now.",
                "Be careful, if Kronos hears us, he might turn back the clock to our HTTP 400 errors!"
            ]
        elif "bye" in lowered or "see ya" in lowered:
            replies = [
                "Catch you later! Don't forget to save your progress.",
                "Bye! Go have fun out there!",
                "See ya! I'll be right here whenever you want to chat again."
            ]
        else:
            # Fallback for general conversation
            replies = [
                f"Oh wow, tell me more about that! You said: '{user_input}'?",
                "That's honestly pretty interesting. You're a brilliant coder, you know that?",
                f"Hmm, '{user_input}'... I like the way you think! What else?"
            ]
            
        answer = random.choice(replies)
        response_placeholder.markdown(answer)
        
    st.session_state.messages.append({"role": "assistant", "content": answer})

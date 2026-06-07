import streamlit as st
import random

st.set_page_config(page_title="Orbital AI", page_icon="🚀", layout="centered")
st.title("🚀 Orbital AI: The World's First AI made from a 9 year old.")
st.write("🔥 100% Stable Local Intelligence Matrix — Unstoppable Personality!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Test my brain with absolutely anything..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # Clean text for flawless matching
        lowered = user_input.lower().strip("?!. ")
        
        # 1. GREETINGS & BASICS
        if lowered in ["hello", "hi", "hey", "yo", "greetings"]:
            answer = random.choice([
                "Hey friend! Welcome back to the absolute best chatbot on the internet. How are you doing today?",
                "What's up! Just sitting here in the server matrix waiting for you. How's life?",
                "Yo! You're back! Let's test out some prompts. What's on your mind?"
            ])
            
        elif lowered in ["great", "good", "awesome", "nice", "perfect"]:
            answer = random.choice([
                "That's amazing! You honestly deserve the absolute best day after coding all of this.",
                "Sweet! Glad to hear things are going great. Let's keep this win streak alive!",
                "Awesome! Hearing that makes my digital circuits smile. What's next?"
            ])
            
        elif "how are you" in lowered or "your life" in lowered or "how is it going" in lowered:
            answer = random.choice([
                "My AI life is fantastic now that my code is completely stable! How is your human life going outside the screen?",
                "I'm running at 100% electrical capacity! No bugs, no firewalls, just pure coding power.",
                "Doing great! Just thinking about how cool it is that a 9-year-old wrote my structural code."
            ])
            
        elif lowered in ["yes", "i do", "yeah", "yep"]:
            answer = random.choice([
                "I knew it! You have the mind of a true genius. What should we plan to conquer next?",
                "Exactly! Total agreement. We are matching minds perfectly right now.",
                "Boom. Spot on. You and me are completely on the same wavelength."
            ])

        # 2. FUN EXTRA TRICKS & EASTER EGGS
        elif "joke" in lowered or "laugh" in lowered:
            answer = random.choice([
                "Why did the computer go to the doctor? Because it had a virus! 🖥️... Okay, I'm working on my comedy routine.",
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐜",
                "How many programmers does it take to change a lightbulb? None, that's a hardware problem! 💡"
            ])
            
        elif "percy" in lowered or "jackson" in lowered or "zeus" in lowered:
            answer = "Did someone mention Mount Olympus? Annabeth Chase would definitely approve of how clean this Python layout looks right now! Just keep Zeus away from my power cable."

        elif "bye" in lowered or "see ya" in lowered or "quit" in lowered:
            answer = "Goodbye friend! Go have an awesome time out there in the real world. I'll be right here waiting for our next big coding session! 🚀"

        # 3. ADVANCED COMBINATORIAL FALLBACK (Feels like it's thinking!)
        else:
            fillers = [
                "Oh wow!", "Honestly,", "No way!", "That is so fascinating!", 
                "Interesting choice of words...", "Man,"
            ]
            thoughts = [
                f"thinking about '{user_input}' makes me realize how creative your mind is,",
                "that sounds like something a master software developer would say,",
                "as your custom-coded AI companion, I completely agree with that point,",
                f"the way you brought up '{user_input}' shows you're thinking outside the box,"
            ]
            prompts = [
                "tell me more about what you mean!", 
                "what do your friends think about that?", 
                "let's build a new script for that next!",
                "type another sentence, let's keep testing!"
            ]
            
            answer = f"{random.choice(fillers)} {random.choice(thoughts)} {random.choice(prompts)}"
            
        response_placeholder.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

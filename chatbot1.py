# =========================================================
# Emotion-Based AI Chatbot
# DecodeLabs Internship - Week 1 Project
# Created using Python
# =========================================================

from datetime import datetime, date
import random

print("=" * 60)
print("🤖 Welcome to Emotion AI Chatbot")
print("💬 Type 'bye' anytime to end the conversation")
print("=" * 60)

# List of jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs 😄",
    "Why did the computer get cold? Because it forgot to close Windows 😂",
    "Why was the math book sad? Because it had too many problems 📚"
]

# List of motivational quotes
motivations = [
    "Believe in yourself and keep going 💪",
    "Every expert was once a beginner 🚀",
    "Success starts with self-confidence 🌟",
    "Small progress is still progress 😊"
]

# Continuous chatbot loop
while True:

    # Taking user input
    user = input("\nYou: ").lower()

    # =========================
    # GREETINGS
    # =========================
    if user in ["hi", "hello", "hey","hii","whatsup"]:
        print("Bot: Hello! Nice to meet you 😊")

    # =========================
    # PERSONAL QUESTIONS
    # =========================
    elif user in ["what is your name", "your name", "who are you"]:
        print("Bot: I am EmotionBot, your friendly AI assistant 🤖")

    elif user in ["who created you", "who made you"]:
        print("Bot: I was created by a DecodeLabs AI Intern 🚀")

    elif user in ["how are you", "how are you doing"]:
        print("Bot: I'm doing great! Thank you for asking 😄")

    # =========================
    # EMOTIONAL SUPPORT
    # =========================
    elif user in ["i am sad", "sad", "depressed"]:
        print("Bot: I'm sorry you're feeling sad 😔")
        print("Bot: Remember, difficult times are temporary 💙")

    elif user in ["i am happy", "happy"]:
        print("Bot: That's wonderful to hear 😊✨")
        print("Bot: Keep smiling and spreading positivity 🌸")

    elif user in ["i am stressed", "stressed", "tired"]:
        print("Bot: Take a deep breath 🌿")
        print("Bot: You are stronger than you think 💪")

    elif user in ["i feel lonely", "lonely"]:
        print("Bot: You are never alone 💜")
        print("Bot: Better days are coming 🌈")

    # =========================
    # MOTIVATION
    # =========================
    elif user in ["motivate me", "motivation", "inspire me"]:
        print("Bot:", random.choice(motivations))

    # =========================
    # JOKES
    # =========================
    elif user in ["tell me a joke", "joke"]:
        print("Bot:", random.choice(jokes))

    # =========================
    # TIME
    # =========================
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    # =========================
    # DATE
    # =========================
    elif user == "date":
        today = date.today()
        print("Bot: Today's date is", today)

    # =========================
    # THANK YOU
    # =========================
    elif user in ["thanks", "thank you"]:
        print("Bot: You're most welcome 😊")

    # =========================
    # EXIT COMMANDS
    # =========================
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Take care and stay positive 🌸")
        break

    # =========================
    # EMPTY INPUT
    # =========================
    elif user == "":
        print("Bot: Please type something 😊")

    # =========================
    # UNKNOWN INPUT
    # =========================
    else:
        print("Bot: Sorry, I don't understand that yet 🤔")
        print("Bot: Try asking something else!")

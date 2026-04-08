import json
import datetime
import random
import re

# Load knowledge base
with open("knowledge_base.json", "r", encoding="utf-8") as file:
    knowledge = json.load(file)

# Intents
greetings = ["hi", "hello", "hey"]
farewells = ["bye", "exit", "quit"]
help_words = ["help", "support"]

# Responses
greet_responses = [
    "Hello! 😊",
    "Hi there! How can I assist you?",
    "Hey! What can I do for you?"
]

help_responses = [
    "I can answer questions about AI, Python, and tech topics.",
    "Try asking me about programming, AI, or internships."
]

fallback_responses = [
    "I’m not sure about that.",
    "Can you try asking in a different way?",
    "I don’t understand that yet."
]

# Logging (FIXED: utf-8 encoding)
def log_chat(user, bot):
    with open("chat_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{datetime.datetime.now()} | You: {user} | Bot: {bot}\n")

# Safe math handler
def handle_math(text):
    try:
        expression = re.findall(r"[0-9+\-*/().]+", text)
        if expression:
            result = eval(expression[0])
            return f"The answer is {result}"
    except:
        return None

def chatbot():
    print("🤖 Chatbot: Hello! Ask me anything (type 'exit' to quit).")

    while True:
        user_input = input("You: ").lower()

        # Exit
        if user_input in farewells:
            response = "Goodbye! 👋"
            print("🤖 Chatbot:", response)
            log_chat(user_input, response)
            break

        # Greeting
        elif any(word in user_input for word in greetings):
            response = random.choice(greet_responses)

        # Help
        elif any(word in user_input for word in help_words):
            response = random.choice(help_responses)

        # Math
        elif any(char.isdigit() for char in user_input):
            math_response = handle_math(user_input)
            if math_response:
                response = math_response
            else:
                response = random.choice(fallback_responses)

        # Knowledge base
        else:
            found = False
            for key in knowledge:
                if key in user_input:
                    response = knowledge[key]
                    found = True
                    break

            if not found:
                response = random.choice(fallback_responses)

        print("🤖 Chatbot:", response)
        log_chat(user_input, response)

if __name__ == "__main__":
    chatbot()
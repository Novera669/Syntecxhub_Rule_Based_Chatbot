#  Rule-Based Chatbot (Console Application)

This project is a **rule-based chatbot** that interacts with users using pattern matching, predefined intents, and a knowledge base.



##  Features

* Intent recognition (greetings, help, small talk)
* Rule-based responses using keyword matching
* Knowledge base for answering domain-specific questions
* Multiple responses for natural conversation
* Basic math expression handling (e.g., 2+2, 10*5)
* Conversation logging with timestamps
* Interactive console-based chat



##  How It Works

* The chatbot analyzes user input using keyword-based matching
* Identifies intent (greeting, help, etc.)
* Searches for answers in a JSON knowledge base
* Handles simple mathematical expressions
* Logs all conversations in a text file



##  Project Structure

* `chatbot.py` → Main chatbot logic
* `knowledge_base.json` → Stores predefined knowledge
* `chat_log.txt` → Saves conversation history



##  How to Run

1. Make sure Python is installed

2. Run the chatbot:

```bash
python chatbot.py
```



##  Example Usage

You: hi

Bot: Hello! 😊

You: what is python

Bot: Python is a powerful programming language used in AI, web development, and automation.

You: 5 + 3

Bot: The answer is 8



##  Technologies Used

* Python
* JSON (for knowledge base)
* File handling (for logging)
* Regular expressions (for math handling)



##  Highlights

* Demonstrates rule-based conversational AI
* Combines intent handling with knowledge retrieval
* Includes logging for tracking conversations
* Handles simple computations for added functionality



##  Future Improvements

* Add more intents and responses
* Improve natural language understanding
* Integrate external APIs for dynamic responses



##  Author

Developed as part of an AI Internship task, focusing on building an interactive rule-based chatbot system.

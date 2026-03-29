# context-aware-chatbot

An AI-powered chatbot that maintains conversation history, understands context across multiple turns and generates intelligent non-repetitive responses using LLM APIs.

## Features

- **Context Awareness**  
  Understands follow-up questions (e.g., “its advantages” refers to the previous topic)

- **Conversation Memory**  
  Maintains chat history using session-based storage

- **Token Optimization**  
  Uses a sliding window approach to manage context efficiently

- **Prompt Engineering**  
  - Reduces hallucinations  
  - Asks clarification when unsure  
  - Avoids repeating answers  

- **Interactive UI**  
  Built using Streamlit for a simple and clean interface

## Tech Stack

- **Python**
- **Streamlit** (Frontend UI)
- **OpenRouter API** (LLM access – free models)
- **Requests** (API calls)

## Project Structure

context-aware-chatbot/

│── app.py

│── requirements.txt

│── README.md


# Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/anugrahaanil-06/context-aware-chatbot.git
cd context-aware-chatbot

## 2. Install dependencies

pip install -r requirements.txt

# 3. API Setup

Get a free API key from https://openrouter.ai/

Replace in app.py:

API_KEY = "YOUR_OPENROUTER_API_KEY"

# 4. Run the application

streamlit run app.py

# Demo

User: Tell me about Python  
User: What are its advantages?

This demonstrates context awareness and memory.

# Key Concepts

- Context window handling (last N messages)
- Chat history management
- Prompt engineering (anti-hallucination, clarification)
- LLM API integration

#Demo Link

(Add your demo video link here)

**Author**

Anugraha AL  
https://github.com/anugrahaanil-06

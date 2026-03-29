import streamlit as st
import requests

API_KEY = "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"

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("Context-Aware Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

SYSTEM_PROMPT = """
You are a helpful AI assistant.

Rules:
- Use previous conversation context when answering
- Do not repeat the same answer
- If unsure, ask a clarification question
- Do not hallucinate; say \"I don't know\" if needed
"""

def build_prompt(user_input):
    history_text = ""
    for chat in st.session_state.chat_history[-5:]:
        history_text += f"User: {chat['user']}\nAssistant: {chat['bot']}\n"

    return f"{SYSTEM_PROMPT}\n{history_text}\nUser: {user_input}\nAssistant:"

def get_response(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo", 
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    return result['choices'][0]['message']['content']

user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    prompt = build_prompt(user_input)
    bot_response = get_response(prompt)

    st.session_state.chat_history.append({
        "user": user_input,
        "bot": bot_response
    })

for chat in st.session_state.chat_history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")

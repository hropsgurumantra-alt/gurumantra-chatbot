import streamlit as st
from google import genai

st.title("🤖 GuruMantra4U Chatbot")

client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = client.models.generate_content(
        model="gemini-1.5-flash-latest",
        contents=prompt,
    )

    reply = response.text

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)


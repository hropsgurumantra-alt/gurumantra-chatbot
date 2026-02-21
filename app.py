import streamlit as st
from google import genai

st.set_page_config(page_title="GuruMantra Career Assistant", page_icon="🎯")

# Show Logo
st.image("logo.png", width=200)

st.title("🎯 GuruMantra Career Assistant")
st.caption("Your Personal Career Growth Partner 🚀")

# Get API key
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("API key not found. Please add it in Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=api_key)

# Career system instruction
system_prompt = """
You are GuruMantra Career Assistant.
You help users with:
- Career guidance
- Interview preparation
- Resume building
- Communication skills
- Government exam preparation
- IT Support & Technical careers

Keep answers clear, motivating, and practical.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask about career, exams, interviews..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.write(prompt)

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=system_prompt + "\nUser: " + prompt,
        )
        reply = response.text
    except Exception as e:
        reply = f"Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)

st.title("🤝 Personalized Networking Assistant")
st.markdown("Generate smart networking conversation starters using AI.")

# ---------------------------
# Event Analyzer
# ---------------------------

st.header("📌 Event Analyzer")

event = st.text_area(
    "Event Description",
    placeholder="Example: AI for Healthcare and Machine Learning Conference"
)

interests = st.text_input(
    "Your Interests",
    placeholder="Machine Learning, Data Science"
)

if st.button("🔍 Analyze Event"):

    response = requests.post(
        f"{API_URL}/analyze-event",
        json={
            "event_description": event,
            "interests": interests
        }
    )

    data = response.json()

    st.success("Themes Detected")

    for theme in data["themes"]:
        st.write("✅", theme)

st.divider()

# ---------------------------
# Conversation Generator
# ---------------------------

st.header("💬 Conversation Generator")

topic = st.text_input(
    "Topic",
    placeholder="Artificial Intelligence"
)

if st.button("Generate Conversation"):

    response = requests.post(
        f"{API_URL}/generate-conversation",
        json={
            "topic": topic
        }
    )

    st.success("Conversation Generated")

    conversation = response.json()["conversation"]

    st.write(conversation)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Like"):

            requests.post(
                f"{API_URL}/feedback",
                json={
                    "conversation": conversation,
                    "feedback": "Like"
                }
            )

            st.success("Thanks for your feedback!")

    with col2:
        if st.button("👎 Dislike"):

            requests.post(
                f"{API_URL}/feedback",
                json={
                    "conversation": conversation,
                    "feedback": "Dislike"
                }
            )

            st.success("Feedback Saved!")

# ---------------------------
# Fact Checker
# ---------------------------

st.header("📚 Wikipedia Fact Checker")

fact = st.text_input(
    "Topic to Verify",
    placeholder="Artificial Intelligence"
)

if st.button("Fact Check"):

    response = requests.post(
        f"{API_URL}/fact-check",
        json={
            "topic": fact
        }
    )

    st.info(response.json()["summary"])

# ---------------------------
# Conversation History
# ---------------------------

st.divider()

st.header("📜 Conversation History")

try:
    response = requests.get(f"{API_URL}/history")
    history = response.json()

    if len(history) == 0:
        st.info("No conversations found.")

    else:
        for item in reversed(history):
            with st.expander(item["event"]):
                st.write(item["conversation"])

except Exception as e:
    st.error(f"Could not load history: {e}")
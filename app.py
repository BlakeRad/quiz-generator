import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load API key from .env (for local use)
load_dotenv()

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="🧠",
    layout="centered"
)

# ---- HEADER ----
st.title("🧠 AI Study Quiz Generator")
st.caption("Built with Python, Streamlit, and the Claude API")
st.write("Paste your study notes or a topic below and instantly generate a multiple choice quiz.")
st.divider()

# ---- API KEY HANDLING ----
# Loads from .env for local dev — visitors supply their own key
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    st.info("🔑 This app requires an Anthropic API key. Get one at [console.anthropic.com](https://console.anthropic.com)")
    api_key = st.text_input(
        "Enter your Anthropic API Key:",
        type="password",
        placeholder="sk-ant-..."
    )
    if not api_key:
        st.stop()

# ---- USER INPUTS ----
topic = st.text_area(
    "📝 Your notes or topic:",
    height=200,
    placeholder="e.g. Paste your biology notes here, or just type a topic like 'World War II causes'"
)

num_questions = st.slider(
    "Number of questions:",
    min_value=2,
    max_value=10,
    value=5
)

st.divider()

# ---- CLAUDE API CALL ----
def generate_quiz(topic: str, num_questions: int, api_key: str) -> str:
    """
    Sends the user's topic/notes to Claude and returns
    a formatted multiple choice quiz as a string.
    """
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are a study quiz generator. Based on the notes or topic below, 
create {num_questions} multiple choice questions to help someone study.

Format every question exactly like this — no exceptions:

**Question 1:** [Question text]

A) [Option]
B) [Option]  
C) [Option]
D) [Option]

✅ **Answer: [Correct letter and option]**

---

Notes/Topic:
{topic}

Generate {num_questions} questions now:"""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text


# ---- GENERATE BUTTON ----
if st.button("⚡ Generate Quiz", use_container_width=True):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic or some notes before generating.")
    else:
        with st.spinner("Generating your quiz with Claude..."):
            try:
                quiz = generate_quiz(topic, num_questions, api_key)
                st.success("✅ Quiz ready!")
                st.markdown(quiz)

                # Let users copy the quiz easily
                st.divider()
                with st.expander("📋 Copy raw quiz text"):
                    st.text(quiz)

            except anthropic.AuthenticationError:
                st.error("❌ Invalid API key. Double-check and try again.")
            except anthropic.RateLimitError:
                st.error("❌ Rate limit reached. Wait a moment and try again.")
            except Exception as e:
                st.error(f"❌ Something went wrong: {str(e)}")

# ---- FOOTER ----
st.divider()
st.caption("Built by Blake Radke · [GitHub](https://github.com/BlakeRad) · Powered by Claude API")
import streamlit as st
from chatbot import AIChatbot

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.logo = None  # optional

# ==========================================================
# LOAD CSS
# ==========================================================

with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================================
# MODELS
# ==========================================================

MODELS = [
    "Gemini",
    "Groq",
    "Mistral"
]

# ==========================================================
# SESSION STATE
# ==========================================================

if "bot" not in st.session_state:
    st.session_state.bot = AIChatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = MODELS[0]

bot = st.session_state.bot

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    # ------------------------------------------------------
    # Assistant Header
    # ------------------------------------------------------

    st.markdown("# 🤖 AI Career Assistant")

    st.caption("Your Personal AI Assistant")

    st.divider()

    # ------------------------------------------------------
    # New Chat
    # ------------------------------------------------------

    if st.button(
        "➕ New Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        bot.clear_chat()
        st.rerun()

    # ------------------------------------------------------
    # Clear Chat
    # ------------------------------------------------------

    if st.button(
        "🧹 Clear Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        bot.clear_chat()
        st.rerun()

    # ------------------------------------------------------
    # Clear Memory
    # ------------------------------------------------------

    if st.button(
        "🧠 Clear Memory",
        use_container_width=True
    ):
        bot.clear_memory()
        st.rerun()

    st.divider()

    # ------------------------------------------------------
    # Chat History
    # ------------------------------------------------------

    st.subheader("💬 Chat History")

    if len(st.session_state.messages) == 0:

        st.caption("No conversations yet.")

    else:

        for i, msg in enumerate(st.session_state.messages):

            if msg["role"] == "user":

                preview = msg["content"][:35]

                if len(msg["content"]) > 35:
                    preview += "..."

                st.caption(f"• {preview}")

    st.divider()

    # ------------------------------------------------------
    # User Memory
    # ------------------------------------------------------

    st.subheader("🧠 User Memory")

    memory = bot.show_memory()

    if memory:

        st.json(memory)

    else:

        st.info("No memory stored.")

    st.divider()

    # ------------------------------------------------------
    # Statistics
    # ------------------------------------------------------

    st.subheader("📊 Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Messages",
            len(st.session_state.messages)
        )

    with col2:
        st.metric(
            "Memory",
            len(memory)
        )

    st.divider()

    st.caption("👤 Developed by")

    st.markdown(
        "**Kanishk Singh**"
    )

# ==========================================================
# MAIN PAGE HEADER
# ==========================================================

left, right = st.columns([7, 2])

with left:

    st.title("🤖 AI Career Assistant")

    st.caption(
        "Programming • AI • Resume • Career Guidance"
    )

with right:

    selected_model = st.selectbox(
        "Model",
        MODELS,
        index=MODELS.index(
            st.session_state.selected_model
        )
    )

    st.session_state.selected_model = selected_model

st.divider()

# ==========================================================
# WELCOME SCREEN
# ==========================================================

if len(st.session_state.messages) == 0:

    st.markdown(
        """
# 👋 Welcome!

I'm your **AI Career Assistant**.

I can help you with:

- 🐍 Python
- 🤖 Artificial Intelligence
- 📊 Machine Learning
- 🌐 Web Development
- 💼 Resume Reviews
- 🎯 Career Guidance
- 🧠 Interview Preparation

Start chatting below.
"""
    )

# ==========================================================
# PART 2 STARTS FROM HERE
# ==========================================================

# ==========================================================
# CHAT HISTORY
# ==========================================================

for message in st.session_state.messages:

    avatar = "👤" if message["role"] == "user" else "🤖"

    with st.chat_message(
        message["role"],
        avatar=avatar
    ):

        st.markdown(message["content"])


# ==========================================================
# CHAT INPUT
# ==========================================================

user_prompt = st.chat_input(
    "💬 Message AI Career Assistant..."
)


# ==========================================================
# PROCESS USER MESSAGE
# ==========================================================

if user_prompt:

    # ----------------------------------
    # Save User Message
    # ----------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Show immediately

    with st.chat_message(
        "user",
        avatar="👤"
    ):
        st.markdown(user_prompt)

    # ----------------------------------
    # Generate AI Response
    # ----------------------------------

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        placeholder = st.empty()

        with st.spinner(
            f"{selected_model} is thinking..."
        ):

            try:

                response = bot.chat(
                    user_prompt,
                    st.session_state.selected_model
                )

            except Exception as e:

                response = f"⚠️ Error\n\n{e}"

        placeholder.markdown(response)

    # ----------------------------------
    # Save Assistant Response
    # ----------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Refresh sidebar memory automatically

    st.rerun()


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

left, right = st.columns([5, 2])

with left:

    st.caption(
        "AI Career Assistant v1.0"
    )

with right:

    st.caption(
        f"Powered by {selected_model}"
    )
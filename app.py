
import streamlit as st
from utils.file_reader import get_file_content
from utils.gemini_utils import ask_gemini
from utils.slm_utils import ask_slm
from utils.summarizer import split_text, summarize_chunks
from utils.translator import translate_to_hindi
from datetime import datetime

# 🌟 Page Config
st.set_page_config(
    page_title="🤖 Smart File Chatbot",
    page_icon="📂",
    layout="wide"
)

# 🎨 Custom Styling
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextInput > div > div > input {
        padding: 0.75rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 🌐 Session Init
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "file_summary" not in st.session_state:
    st.session_state.file_summary = ""

# 🎯 Title
st.markdown("""
<div style='text-align: center;'>
    <h1>🤖 Smart File Chatbot</h1>
    <p style='color: gray;'>Upload any file and intelligently ask questions with AI models.</p>
</div>
""", unsafe_allow_html=True)

# 📁 Upload File
uploaded_file = st.file_uploader("📂 Upload your file", type=["pdf", "txt", "docx", "csv"])

# 🤖 Model & Mode Choice
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    model_choice = st.selectbox("🧠 Choose a model", ["Gemini (LLM)", "SLM (Local Model)"])
with col2:
    chat_mode = st.radio("🗣️ Answer Style", ["Simple", "Detailed"], horizontal=True)
with col3:
    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []

# 💬 User Question
question = st.text_input("💬 Ask a question about the file:")
 
# 🧠 File Handling
if uploaded_file:
    file_content = get_file_content(uploaded_file)

    if len(file_content) > 50000:
        st.warning("⚠️ Large file detected. Summarizing...")
        chunks = split_text(file_content)
        file_content = summarize_chunks(chunks)

    # 🗋 Memory Summary on Upload
    if not st.session_state.file_summary:
        st.session_state.file_summary = file_content[:500] + "..."  # First 500 chars
        st.info("🧠 File Summary:\n\n" + st.session_state.file_summary)

    # 🗾️ Answering
    if question:
        with st.spinner("🤔 Thinking..."):
            formatted_question = question
            if chat_mode == "Detailed":
                formatted_question += "\nPlease provide a detailed explanation."

            if model_choice == "Gemini (LLM)":
                answer = ask_gemini(formatted_question, file_content)
            else:
                answer = ask_slm(formatted_question, file_content)

        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.chat_history.append((f"You [{timestamp}]", question))
        st.session_state.chat_history.append((f"Bot [{timestamp}]", answer))

# 📜 Chat History
if st.session_state.chat_history:
    st.markdown("---")
    st.subheader("🗜️ Chat History")

    for sender, msg in st.session_state.chat_history:
        if "You" in sender:
            with st.chat_message("user"):
                st.markdown(f"**{sender}:** {msg}")
        else:
            with st.chat_message("assistant"):
                st.markdown(f"**{sender}:** {msg}")

    # 📅 Download Chat History
    chat_log = "\n\n".join([f"{s}: {m}" for s, m in st.session_state.chat_history])
    st.download_button("📄 Download Chat History", chat_log, file_name="chat_history.txt")

    # 🌐 Translate Last Bot Answer
    last_speaker, last_message = st.session_state.chat_history[-1]
    if "Bot" in last_speaker and st.button("🌐 Translate Last Answer to Hindi"):
        hindi_translation = translate_to_hindi(last_message)
        st.markdown("🌐 **Translated Answer (Hindi):**")
        st.success(hindi_translation)


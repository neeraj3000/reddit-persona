# Fix event loop for Windows
import sys
import asyncio

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import streamlit as st
from reddit_utils import extract_username, get_user_data
from persona_chain import chain
import os

# Combine Reddit posts and comments into 1 string
def build_reddit_text(posts, comments):
    combined = ""
    for p in posts:
        combined += f"[POST] {p['title']}\n{p['body']}\nURL: {p['url']}\n\n"
    for c in comments:
        combined += f"[COMMENT] {c['body']}\nURL: {c['url']}\n\n"
    return combined[:17000]

# Save result to a file
def write_to_file(persona_text, username):
    filename = f"user_persona_{username}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
    return filename

# Streamlit UI Setup
st.set_page_config("Reddit Persona Builder", layout="centered")
st.title("🧠 Reddit Persona Generator (LangChain + Groq Powered)")

url = st.text_input("Paste Reddit Profile URL")

if st.button("Generate Persona"):
    username = extract_username(url)
    
    if not username:
        st.error("❌ Invalid Reddit profile URL!")
    else:
        with st.spinner("🔍 Fetching Reddit data..."):
            posts, comments = get_user_data(username)

        if not posts and not comments:
            st.warning("⚠️ No content found for this user.")
        else:
            with st.spinner("🤖 Analyzing with LLM..."):
                try:
                    reddit_text = build_reddit_text(posts, comments)
                    result = chain.invoke(reddit_text)

                    # Assume result is a markdown-formatted string
                    if isinstance(result, dict) and "structured" in result:
                        persona_text = result["structured"]
                    elif isinstance(result, str):
                        persona_text = result
                    else:
                        st.error("❌ Unexpected output format from LLM.")
                        st.stop()

                except Exception as e:
                    st.error(f"❌ LLM error: {e}")
                    st.stop()

            st.success("✅ Persona generated successfully!")
            st.markdown(persona_text)

            # Download button
            filename = write_to_file(persona_text, username)
            with open(filename, "rb") as f:
                st.download_button(
                    "📥 Download Persona!",
                    data=f,
                    file_name=filename,
                    mime="text/plain"
                )

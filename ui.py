import streamlit as st
import requests

st.set_page_config(page_title="Research Summarizer", layout="centered")

st.title("Research Article Summarizer")
st.write("Enter any article URL and get a clean summary, insights, and quiz questions.")

url = st.text_input("Article URL", placeholder="https://www.bbc.com/news/...")

if st.button("Summarize"):
    if not url:
        st.error("Please enter a URL.")
    else:
        with st.spinner("Summarizing..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/summarize",
                    json={"url": url}
                )
                
                if response.status_code != 200:
                    st.error(f"Error {response.status_code}: {response.text}")
                else:
                    data = response.json()

                    st.subheader("📝 Summary")
                    for bullet in data["summary"]:
                        st.write(f"- {bullet}")

                    st.subheader("💡 Key Insights")
                    for bullet in data["key_insights"]:
                        st.write(f"- {bullet}")

                    st.subheader("🧒 Explained Like I'm 5")
                    st.write(data["simplified"])

                    st.subheader("🔍 Citations")
                    for c in data["citations"]:
                        st.write(f"- {c}")

                    st.subheader("❓ Quiz Yourself")
                    for q in data["quiz"]:
                        st.write(f"- {q}")

            except Exception as e:
                st.error(f"Something went wrong: {e}")

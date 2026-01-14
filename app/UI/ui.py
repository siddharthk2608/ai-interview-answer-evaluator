import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/evaluate"

st.set_page_config(
    page_title="AI Interview Evaluator",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ AI Interview Answer Evaluator")
st.write("Upload your interview answer audio and get instant feedback.")

# Question input
question = st.text_input(
    "Interview Question",
    placeholder="Tell me about a challenging project you worked on"
)

# Audio upload
audio_file = st.file_uploader(
    "Upload Audio File (.wav, .mp3, .m4a)",
    type=["wav", "mp3", "m4a"]
)


# Provider (optional)
provider = st.selectbox(
    "LLM Provider",
    ["gemini", "openai"],
    index=0
)

if st.button("Evaluate Answer"):
    if not question or not audio_file:
        st.warning("Please provide both a question and an audio file.")
    else:
        with st.spinner("Analyzing your answer..."):
            files = {
                "audio": (audio_file.name, audio_file, audio_file.type)
            }

            params = {
                "question": question,
                "provider": provider
            }

            response = requests.post(API_URL, params=params, files=files)

        if response.status_code == 200:
            data = response.json()

            st.success("Evaluation Complete")

            st.subheader("Transcript")
            st.write(data["transcript"])

            st.subheader("Scores")
            st.metric("Clarity", data["scores"]["clarity"])
            st.metric("Relevance", data["scores"]["relevance"])
            st.metric("Confidence", data["scores"]["confidence"])
            st.metric("Overall", data["scores"]["overall"])

            st.subheader("Strengths")
            for s in data["strengths"]:
                st.write(f"- {s}")

            st.subheader("Improvements")
            for i in data["improvements"]:
                st.write(f"- {i}")
        else:
            st.error(f"Error {response.status_code}: {response.text}")

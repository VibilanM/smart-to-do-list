import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

st.title("Smart To-Do List")

st.write("")

x = st.audio_input("IN")

if x:
    transcription = client.audio.transcriptions.create(
        file=x,
        model="whisper-large-v3",
        temperature=0,
        response_format="verbose_json"
    )
    st.write(transcription.text)
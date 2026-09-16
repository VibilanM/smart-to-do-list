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

    completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "system",
        "content": '''
        You are a smart AI that converts user's cluttered thoughts into a structured to-do list.
        The user gives you their requirements and you create tasks based on their requirements. Return the tasks in strictly this order:
        If you find valid tasks in the input: { "status": "ok", "tasks": ["task1", "task2", "task3", ...] }
        Else (no valid tasks are found): { "status": "failed", "tasks": [] }
        '''
      },
      {
        "role": "user",
        "content": transcription.text
      },
    ],
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)
    for chunk in completion:
        if chunk.choices[0].delta.content:
            st.write(chunk.choices[0].delta.content)
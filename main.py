import streamlit as st

st.title("Smart To-Do List")

st.write("")

x = st.audio_input("IN")

if x:
    st.write("Audio ready.")
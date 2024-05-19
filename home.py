import streamlit as st


st.title("Tugas Besar Strategi Algoritma")
st.divider()
st.header("Climbing Stairs Problem")

button1 = st.button("PLAY!")
if button1:
   st.switch_page("pages/algorithms.py")


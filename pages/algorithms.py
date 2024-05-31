import streamlit as st

st.title("Climbing Stairs Problem")
st.divider()

if st.button("Home"):
    st.switch_page("home.py")

button1 = st.button("Backtracking")
if button1:
    st.switch_page("pages/backtrack.py")

button2 = st.button("Dynamic Programming")
if button2:
    st.switch_page("pages/dynamicprog.py")
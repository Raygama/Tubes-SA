import streamlit as st

def climbingStairs(i, n):
    if i > n:
        return 0
    if i == n:
        return 1
    return climbingStairs(i + 1, n) + climbingStairs(i + 2, n)

def countClimbStairs(n):
    return climbingStairs(0, n)

st.title("Climbing Stairs Problem")
st.divider()

if st.button("Back"):
    st.switch_page("pages/algorithms.py")

if st.button("Home"):
    st.switch_page("home.py")

stairs = st.slider("Number of Stairs: ",1 , 15)
run = st.button("Run Algorithm")
if run:
    if stairs:
        st.write("The number of ways to climb the stairs is: ", countClimbStairs(stairs))
    else:
        st.write("Please enter a number of stairs to climb")

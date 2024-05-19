import streamlit as st

def climbingStairs(n):
    if n == 0:
        return 0
    stair = [0] * (n + 1)
    stair[1] = 1
    stair[2] = 2

    for i in range(3, n+1):
        stair[i] = stair[i - 1] + stair[i - 2]
    
    return stair[n]

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
        st.write("The number of ways to climb the stairs is: ", climbingStairs(stairs))
    else:
        st.write("Please enter a number of stairs to climb")
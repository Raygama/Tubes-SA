import streamlit as st
import pandas as pd
import time

def climbingStairs(n):
    if n == 0:
        return 0
    stair = [0] * (n + 1)
    stair[1] = 1
    stair[2] = 2

    for i in range(3, n + 1):
        # Display "After step i"
        step_placeholder = st.empty()
        step_placeholder.write(f"After step {i}:")

        # Display table for steps up to i
        table_placeholder = st.empty()
        table_data = {"Step": list(range(i + 1)), "Number of ways": stair[0:i + 1]}
        table_df = pd.DataFrame(table_data).set_index("Step").T
        table_placeholder.write(table_df)

        time.sleep(2)

        # Clear previous step display
        step_placeholder.empty()
        table_placeholder.empty()

        stair[i] = stair[i - 1] + stair[i - 2]

    st.write("The number of ways to climb the stairs is: ", stair[n])

    # Display final table
    st.write(f"After step {n}:")
    final_table_data = {"Step": list(range(n + 1)), "Number of ways": stair}
    final_table_df = pd.DataFrame(final_table_data).set_index("Step").T
    st.write(final_table_df)

    return stair[n]

st.title("Climbing Stairs Problem - Dynamic Programming Visualization")
st.divider()

if st.button("Back"):
    st.switch_page("pages/algorithms.py")

if st.button("Home"):
    st.switch_page("home.py")

stairs = st.slider("Number of Stairs: ", 1, 15)

run = st.button("Run Algorithm")
if run:
    if stairs:
        climbingStairs(stairs)
    else:
        st.write("Please enter a number of stairs to climb")

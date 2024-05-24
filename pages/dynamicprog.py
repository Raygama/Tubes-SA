import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def draw_stairs(combo, n, step_width=1, color='blue'):
    x = []
    y = []
    current_position = 0
    
    for step in combo:
        if step == '1':
            current_position += 1
        elif step == '2':
            current_position += 2
        x.append(current_position)
        y.append(current_position)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(x, y, color=color, width=0.5)
    ax.set_xlim(1, n)
    ax.set_ylim(0, n + 1)
    ax.set_xticks(range(1, n + 1))
    ax.set_xticklabels([str(i) for i in range(1, n + 1)])
    ax.set_yticks(range(n + 1))
    ax.set_yticklabels([str(i) for i in range(n + 1)])
    ax.set_title(f"Stairs with {n} steps")
    ax.set_xlabel("Step number")
    ax.set_ylabel("Step")
    ax.grid(True)
    
    return fig

def visualize_combinations(combinations, n):
    figs = []
    for combo in combinations:
        fig = draw_stairs(combo.split(), n)
        figs.append(fig)
    return figs

def climbingStairs(n):
    if n == 0:
        return 0, []
    if n == 1:
        return 1, ["1"]
    if n == 2:
        return 2, ["1 1", "2"]

    stair = [0] * (n + 1)
    stair[1] = 1
    stair[2] = 2

    for i in range(3, n + 1):
        stair[i] = stair[i - 1] + stair[i - 2]

    # Display final table
    st.write(f"After step {n}:")
    final_table_data = {"Step": list(range(n + 1)), "Number of ways": stair}
    final_table_df = pd.DataFrame(final_table_data).set_index("Step").T
    st.write(final_table_df)

    # Generate all combinations of steps
    def get_combinations(steps):
        if steps == 0:
            return [""]
        elif steps == 1:
            return ["1"]
        elif steps == 2:
            return ["1 1", "2"]
        else:
            one_step_before = get_combinations(steps - 1)
            two_steps_before = get_combinations(steps - 2)
            
            current_combinations = []
            for combo in one_step_before:
                current_combinations.append(combo + " 1")
            for combo in two_steps_before:
                current_combinations.append(combo + " 2")
            
            return current_combinations

    combinations = get_combinations(n)
    
    return stair[n], combinations

st.title("Climbing Stairs Problem - Dynamic Programming Visualization")
st.divider()
if st.button("Back"):
    st.switch_page("pages/algorithms.py")

if st.button("Home"):
    st.experimental_rerun("home.py")

stairs = st.slider("Number of Stairs: ", 1, 15)

run = st.button("Run Algorithm")
if run:
    if stairs:
        ways, combinations = climbingStairs(stairs)
        st.write(f"The number of ways to climb the stairs is: {ways}")
        
        figs = visualize_combinations(combinations, stairs)
        for i, (fig, combo) in enumerate(zip(figs, combinations)):
            st.write(f"Visualization {i+1}: {combo}")
            st.pyplot(fig)
    else:
        st.write("Please enter a number of stairs to climb")

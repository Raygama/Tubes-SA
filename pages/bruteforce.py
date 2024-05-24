import streamlit as st
import graphviz
import time
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk menggambar pohon rekursif menggunakan Graphviz
def draw_recursive_tree(graph, i, n, parent=None, counter=None):
    if counter is None:
        counter = {'value': 0}
    
    if i > n:
        node_label = f"{i} (X)"
        graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle', color='red')
        if parent is not None:
            graph.edge(parent, f"{i}_{counter['value']}")
        counter['value'] += 1
        return 0
    
    if i == n:
        node_label = f"{i} (1)"
        graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle', style='filled', color='lightblue')
        if parent is not None:
            graph.edge(parent, f"{i}_{counter['value']}")
        counter['value'] += 1
        return 1

    node_label = f"{i}"
    graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle')
    if parent is not None:
        graph.edge(parent, f"{i}_{counter['value']}")
    
    current_node = f"{i}_{counter['value']}"
    counter['value'] += 1

    time.sleep(1)
    st.graphviz_chart(graph)
    
    left_result = draw_recursive_tree(graph, i + 1, n, current_node, counter)
    right_result = draw_recursive_tree(graph, i + 2, n, current_node, counter)

    return left_result + right_result

# Fungsi untuk menggambar tangga dengan langkah-langkah tertentu
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

# Fungsi untuk memvisualisasikan kombinasi langkah dari tangga
def visualize_combinations(combinations, n):
    figs = []
    for combo in combinations:
        fig = draw_stairs(combo.split(), n)
        figs.append(fig)
    return figs

# Fungsi untuk menemukan semua cara untuk mendaki tangga
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

# Fungsi utama Streamlit
st.title("Climbing Stairs Problem - Brute Force Visualization")
st.divider()

if st.button("Back"):
    st.switch_page("pages/algorithms.py")

if st.button("Home"):
    st.switch_page("home.py")

stairs = st.slider("Number of Stairs: ", 1, 15)
run = st.button("Run Algorithm")
if run:
    if stairs:
        st.write("Visualisasi Pohon Rekursif:")
        
        graph = graphviz.Digraph()
        total_ways = draw_recursive_tree(graph, 0, stairs)
        st.write(f"The number of ways to climb the stairs is: {total_ways}")
        
        st.write("Visualisasi Tangga:")
        ways, combinations = climbingStairs(stairs)
        st.write(f"The number of ways to climb the stairs is: {ways}")
        
        figs = visualize_combinations(combinations, stairs)
        for i, (fig, combo) in enumerate(zip(figs, combinations)):
            st.write(f"Visualization {i+1}: {combo}")
            st.pyplot(fig)
    else:
        st.write("Please enter a number of stairs to climb")

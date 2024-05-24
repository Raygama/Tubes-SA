import streamlit as st
import graphviz
import time

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
        st.graphviz_chart(graph)  # Update chart after adding node
        time.sleep(0.5)  # Sleep for visualization
        return 0
    
    if i == n:
        node_label = f"{i} (1)"
        graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle', style='filled', color='lightblue')
        if parent is not None:
            graph.edge(parent, f"{i}_{counter['value']}")
        counter['value'] += 1
        st.graphviz_chart(graph)  # Update chart after adding node
        time.sleep(0.5)  # Sleep for visualization
        return 1

    node_label = f"{i}"
    graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle')
    if parent is not None:
        graph.edge(parent, f"{i}_{counter['value']}")
    
    current_node = f"{i}_{counter['value']}"
    counter['value'] += 1

    st.graphviz_chart(graph)  # Update chart after adding node
    time.sleep(0.5)  # Sleep for visualization
    
    left_result = draw_recursive_tree(graph, i + 1, n, current_node, counter)
    right_result = draw_recursive_tree(graph, i + 2, n, current_node, counter)

    return left_result + right_result

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
    else:
        st.write("Please enter a number of stairs to climb")

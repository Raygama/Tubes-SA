import streamlit as st  
import graphviz 
import time  
import pandas as pd  
import matplotlib.pyplot as plt 

# Fungsi buat gambar pohon rekursif Graphviz dan ALGORITMA climbing stairs
def draw_recursive_tree(graph, i, n, parent=None, counter=None, path=None, best_path=None):
    if counter is None:
        counter = {'value': 0}  # Inisialisasi counter
    if path is None:
        path = []  # Inisialisasi path 
    if best_path is None:
        best_path = {'value': []}  # Inisialisasi best_path
    
    path.append(i)  # Tambahin langkah sekarang ke path

    if i > n:
        # Kalau langkah lebih dari jumlah tangga, node gak layak
        node_label = f"Tangga {i} (X)\nTidak Layak"
        graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle', color='red')
        if parent is not None:
            graph.edge(parent, f"{i}_{counter['value']}")
        counter['value'] += 1
        st.graphviz_chart(graph)  # Update chart setelah tambahin node
        time.sleep(0.5)  # Sleep buat visualisasi
        path.pop()
        return 0
    
    if i == n:
        # Kalau langkah tepat di jumlah tangga, node layak
        node_label = f"Tangga {i} (V)\nLayak"
        graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle', style='filled', color='lightblue')
        if parent is not None:
            graph.edge(parent, f"{i}_{counter['value']}")
        counter['value'] += 1
        st.graphviz_chart(graph)  # Update chart setelah tambahin node
        time.sleep(0.5)  # Sleep buat visualisasi

        # Update best_path kalo path sekarang lebih pendek
        if not best_path['value'] or len(path) < len(best_path['value']):
            best_path['value'] = list(path)
        
        path.pop()
        return 1

    # Kalau belum di tangga terakhir, tambahin node normal
    node_label = f"Tangga {i}"
    graph.node(f"{i}_{counter['value']}", label=node_label, shape='circle')
    if parent is not None:
        graph.edge(parent, f"{i}_{counter['value']}")
    
    current_node = f"{i}_{counter['value']}"
    counter['value'] += 1

    # Clear chart sebelum tambahin node baru
    st.graphviz_chart(graphviz.Digraph())
    
    # Tambahin pohon baru
    st.graphviz_chart(graph)
    time.sleep(0.5)  # Sleep buat visualisasi
    
    # Rekursi ke langkah berikutnya
    left_result = draw_recursive_tree(graph, i + 1, n, current_node, counter, path, best_path)
    right_result = draw_recursive_tree(graph, i + 2, n, current_node, counter, path, best_path)

    path.pop()
    return left_result + right_result

# Fungsi buat gambar tangga visualisasi
def draw_stairs(combo, n, step_width=1, color='blue'):
    x = []  # Buat nyimpen posisi x
    y = []  # Buat nyimpen posisi y
    current_position = 0  # Mulai dari posisi 0
    
    # Iterasi tiap langkah di combo
    for step in combo:
        if step == '1':  # Kalau langkahnya 1, maju 1 langkah
            current_position += 1
        elif step == '2':  # Kalau langkahnya 2, maju 2 langkah
            current_position += 2
        x.append(current_position)  # Tambahin posisi x sekarang
        y.append(current_position)  # Tambahin posisi y sekarang
    
    # Setup plotnya
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

# Fungsi visualisasi semua kombinasi langkah
def visualize_combinations(combinations, n):
    figs = []  
    for combo in combinations:
        fig = draw_stairs(combo.split(), n)  # Gambar tangga
        figs.append(fig)  
    return figs 

# dapetin semua combinasi
def get_combinations(steps):
    if steps == 0:
        return [""]  # Kalau 0 langkah, balikin list kosong
    elif steps == 1:
        return ["1"]  # Kalau 1 langkah, balikin list dengan "1"
    elif steps == 2:
        return ["1 1", "2"]  # Kalau 2 langkah, balikin list dengan "1 1" dan "2"
    else:
        one_step_before = get_combinations(steps - 1)  # Dapetin kombinasi langkah untuk steps-1
        two_steps_before = get_combinations(steps - 2)  # Dapetin kombinasi langkah untuk steps-2
            
        current_combinations = []  # List buat nyimpen kombinasi sekarang
        for combo in one_step_before:
            current_combinations.append(combo + " 1")  # Tambahin "1" ke tiap kombinasi sebelumnya
        for combo in two_steps_before:
            current_combinations.append(combo + " 2")  # Tambahin "2" ke tiap kombinasi sebelumnya
            
        return current_combinations  # Balikin list kombinasi

# Fungsi utama Streamlit
st.title("Climbing Stairs Problem - Backtrack Visualization")
st.divider()  # Tambahin pembatas

# Tombol buat balik ke halaman algoritma
if st.button("Back"):
    st.switch_page("pages/algorithms.py")  # Pindah ke halaman algorithms.py

# Tombol buat balik ke halaman utama
if st.button("Home"):
    st.switch_page("home.py")  # Pindah ke halaman home.py

# Slider buat milih jumlah tangga
stairs = st.slider("Number of Stairs: ", 1, 15)  # Bikin slider dari 1 sampai 15
run = st.button("Run Algorithm")  # Tombol buat jalanin algoritma

if run:
    if stairs:
        st.write("Visualisasi Pohon Rekursif:")
        
        graph = graphviz.Digraph()  # Buat graph baru
        best_path = {'value': []}  # Inisialisasi best_path
        total_ways = draw_recursive_tree(graph, 0, stairs, best_path=best_path)  # Gambar pohon rekursif
        st.write(f"The number of ways to climb the stairs is: {total_ways}")  # Tampilkan hasil jumlah cara
        st.write(f"Langkah terbaik untuk mencapai tangga ke-{stairs} adalah: {best_path['value']}")  # Tampilkan jalur terbaik
        
        st.write("Visualisasi Tangga:")
        combinations = get_combinations(stairs)  # Jalankan algoritma climbingStairs
        
        figs = visualize_combinations(combinations, stairs)  # Visualisasi semua kombinasi
        for i, (fig, combo) in enumerate(zip(figs, combinations)):
            st.write(f"Visualization {i+1}: {combo}")  # Tampilkan teks visualisasi
            st.pyplot(fig)  # Tampilkan plot
    else:
        st.write("Please enter a number of stairs to climb")  # Tampilkan pesan kalau belum pilih jumlah tangga

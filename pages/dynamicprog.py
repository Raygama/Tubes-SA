import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np  
import time

# Fungsi buat gambar tangga dari kombinasi langkah
def draw_stairs(combo, n, step_width=1, color='blue', title_suffix=""):
    x = []  # Buat nyimpen posisi x
    y = []  # Buat nyimpen posisi y
    current_position = 0  # Mulai dari posisi 0
    
    for step in combo:
        if step == '1':  
            current_position += 1
        elif step == '2':  
            current_position += 2
        x.append(current_position)
        y.append(current_position)  
    
    # Visualisasi
    fig, ax = plt.subplots(figsize=(10, 4))  
    ax.bar(x, y, color=color, width=0.5)  
    ax.set_xlim(1, n) 
    ax.set_ylim(0, n + 1) 
    ax.set_xticks(range(1, n + 1))  
    ax.set_xticklabels([str(i) for i in range(1, n + 1)])  
    ax.set_yticks(range(n + 1)) 
    ax.set_yticklabels([str(i) for i in range(n + 1)]) 
    ax.set_title(f"Stairs with {n} steps {title_suffix}")  
    ax.set_xlabel("Step number") 
    ax.set_ylabel("Step") 
    ax.grid(True)  
    
    return fig  # return figure plotnya

# Fungsi buat visualisasi semua kombinasi langkah
def visualize_combinations(combinations, n, best_path):
    figs = []  # List 
    for combo in combinations:
        title_suffix = "(Best Path)" if combo == best_path else ""  # Tambahin label kalau ini jalur terbaik
        fig = draw_stairs(combo.split(), n, title_suffix=title_suffix)  # Gambar tangga
        figs.append(fig)  
    return figs  # return list figure

# Fungsi ALGORITMA CLIMBING STAIRS buat hitung cara naik tangga
def climbingStairs(n):
    if n == 0:
        return 0, []  # Kalau 0 tangga, balikin 0 dan list kosong
    if n == 1:
        return 1, ["1"]  # Kalau 1 tangga, cuma ada 1 cara
    if n == 2:
        return 2, ["1 1", "2"]  # Kalau 2 tangga, ada 2 cara
    
    stair = [0] * (n + 1)  # List buat nyimpen cara tiap tangga
    stair[1] = 1  # Tangga 1 ada 1 cara
    stair[2] = 2  # Tangga 2 ada 2 cara
    
    # Placeholder untuk tabel
    tabel_sementara = st.empty()

    # Iterasi dari tangga 3 sampai n
    for i in range(3, n + 1):
        stair[i] = stair[i - 1] + stair[i - 2]  # Jumlah cara tangga i adalah jumlah cara tangga stair[i-1] + stair[i-2]
        
        # Update tabel hasil sementara
        data = {"Step": list(range(i + 1)), "Number of ways": stair[:i + 1]}  # Data buat tabel
        tabel_df = pd.DataFrame(data).set_index("Step").T  # Bikin DataFrame dan set index
        tabel_sementara.write(tabel_df)  # Update tabel di Streamlit
        time.sleep(0.5)  # Sleep buat visualisasi
    
    # Fungsi buat dapetin semua kombinasi langkah
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

    combinations = get_combinations(n)  # Dapetin semua kombinasi langkah untuk n

    # Cari jalur terbaik
    best_path = min(combinations, key=lambda x: len(x.split()))  # Cari kombinasi dengan langkah paling sedikit

    return stair[n], combinations, best_path  # Balikin jumlah cara, semua kombinasi, dan jalur terbaik

# Set judul halaman Streamlit
st.title("Climbing Stairs Problem - Dynamic Programming Visualization")
st.divider() 

# Tombol buat balik ke halaman algoritma
if st.button("Back"):
    st.switch_page("pages/algorithms.py") 

# Tombol buat balik ke halaman utama
if st.button("Home"):
    st.switch_page("home.py")  

# Slider buat milih jumlah tangga
stairs = st.slider("Number of Stairs: ", 1, 15)  

# Tombol buat jalanin algoritma
run = st.button("Run Algorithm")
if run:
    if stairs:
        ways, combinations, best_path = climbingStairs(stairs)  
        st.write(f"The number of ways to climb the stairs is: {ways}")  # Tampilkan hasil jumlah cara
        st.write(f"Langkah terbaik untuk mencapai tangga ke-{stairs} adalah: {best_path}")  # Tampilkan jalur terbaik

        figs = visualize_combinations(combinations, stairs, best_path)  # Visualisasi semua kombinasi
        for i, (fig, combo) in enumerate(zip(figs, combinations)):
            st.write(f"Visualization {i+1}: {combo}")  # Tampilkan teks visualisasi
            st.pyplot(fig)  # Tampilkan plot
    else:
        st.write("Please enter a number of stairs to climb")  # Tampilkan pesan kalau belum pilih jumlah tangga

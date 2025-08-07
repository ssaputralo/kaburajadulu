import streamlit as st
from collections import Counter
import json
import os

# File untuk menyimpan histori
HISTORY_FILE = "history.json"

# Fungsi untuk memuat histori dari file
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan histori ke file
def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file)

# Load histori dari file ke session_state
if "history" not in st.session_state:
    st.session_state.history = load_history()

# Sidebar Navigation
with st.sidebar:
    st.title("Home")
    
    # Navigasi halaman
    st.page_link("home.py", label="Home")
    st.page_link("pages/foreignlanguages.py", label="Foreign Languages")
    st.page_link("pages/studyabroad.py", label="Study Abroad")
    st.page_link("pages/workabroad.py", label="Work Abroad")
    st.page_link("pages/lifeabroad.py", label="Life Abroad")

    st.markdown("---")
    st.markdown("**Let's connect!**")
    st.markdown("[➤ Twitter](https://twitter.com)")
    st.markdown("[in LinkedIn](https://linkedin.com)")
    st.markdown("[Lab](https://gptlab.streamlit.app/lab)")

# Main content
st.title("#KaburAjaDulu")
st.write("Ini merupakan platform untuk membantu kamu dalam mempersiapkan diri dalam melanjutkan pendidikan, bekerja, atau menetap di luar negeri.")
st.write("Kami menyediakan berbagai informasi dan sumber daya yang dapat membantu kamu dalam mencapai tujuan tersebut.")

st.write("Kamu rencana mau ke negara mana nih?")

# Input negara tujuan
negara_tujuan = st.text_input("Masukkan negara tujuan:")

# Tambahkan input ke histori
if negara_tujuan:
    st.session_state.history.append(negara_tujuan)
    save_history(st.session_state.history)

# Hitung frekuensi negara tujuan
histori_counter = Counter(st.session_state.history)

# Tampilkan histori
st.write("### Histori negara tujuan:")
filter_option = st.selectbox("Urutkan berdasarkan:", ["Tidak diurutkan", "Jumlah Terkecil", "Jumlah Terbesar"])

# Konversi ke tabel
histori_table = [{"Negara": negara, "Jumlah": count} for negara, count in histori_counter.items()]

# Filter data
if filter_option == "Jumlah Terkecil":
    histori_table = sorted(histori_table, key=lambda x: x["Jumlah"])
elif filter_option == "Jumlah Terbesar":
    histori_table = sorted(histori_table, key=lambda x: x["Jumlah"], reverse=True)

st.table(histori_table)
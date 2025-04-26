import streamlit as st

with st.sidebar:
    st.title("Sidebar")
    st.write("This is the sidebar content.")
    st.button("Click me!")

st.title("#KaburAjaDulu")
st.write("Ini merupakan platform untuk membantu kamu dalam mempersiapkan diri dalam melanjutkan pendidikan, bekerja, atau menetap di luar negeri.")
st.write("Kami menyediakan berbagai informasi dan sumber daya yang dapat membantu kamu dalam mencapai tujuan tersebut.")

st.write("Kamu rencana mau ke negara mana nih?")
st.selectbox("Pilih negara:", ["Jerman", "Belanda", "Swedia", "Finlandia", "Norwegia"])
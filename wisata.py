import streamlit as st

# Judul aplikasi
st.title("Sistem Rekomendasi Wisata Sederhana")

# Input pilihan budget
budget = st.selectbox(
    "Pilih Budget Anda:",
    ["< 50 ribu", "50 - 100 ribu", "> 100 ribu"]
)

# Input pilihan jenis wisata
jenis_wisata = st.selectbox(
    "Pilih Jenis Wisata:",
    ["Wisata Air", "Wisata Alam", "Wisata Edukasi"]
)

# Tombol rekomendasi
if st.button("Dapatkan Rekomendasi"):
    if budget == "< 50 ribu" and jenis_wisata == "Wisata Air":
        hasil = "Umbul Ponggok"
    elif budget == "< 50 ribu" and jenis_wisata == "Wisata Alam":
        hasil = "Bukit Cinta"
    elif budget == "50 - 100 ribu" and jenis_wisata == "Wisata Air":
        hasil = "Umbul Manten"
    elif budget == "50 - 100 ribu" and jenis_wisata == "Wisata Alam":
        hasil = "Gunung Merapi Park"
    elif budget == "> 100 ribu" and jenis_wisata == "Wisata Edukasi":
        hasil = "Museum Sangiran"
    else:
        hasil = "Taman Wisata Kota"

    st.success(f"Rekomendasi wisata untuk Anda: {hasil}")

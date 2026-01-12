import streamlit as st
import base64
import os
import time

def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

local_css("views/css/landing.css")

img_base64 = get_base64("image/background.png") 
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">Reservasi Layanan &<br>Data Klien Annaira</h1>
        <p class="hero-subtitle">
            Setiap perjalanan bunda dan si kecil begitu berharga. <br>
            Melalui website ini, Annaira ingin memahami kebutuhan bunda dan bayi dengan 
            lebih baik agar sesi nantinya dapat berjalan dengan nyaman dan sesuai kebutuhan.<br>
            Jadwalkan momen spesial bunda<br>dan si kecil bersama Annaira 🤍
        </p>
    </div>
""", unsafe_allow_html=True)

col_spacer, col_button, col_rest = st.columns([0.13, 1, 1])

with col_button:
    if st.button("Atur Jadwal Sesi"):
        time.sleep(0.5)
        st.switch_page("views/home.py")

st.markdown('<div class="hero-footer-left">annaira.homespa</div>', unsafe_allow_html=True)
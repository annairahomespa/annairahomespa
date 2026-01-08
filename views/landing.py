import streamlit as st
import base64

# Fungsi untuk load gambar lokal sebagai background
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# GANTI 'views/header.jpg' dengan path file gambar kain Bunda yang tanpa tulisan
img_base64 = get_base64("image/background.png") 

st.markdown(f"""
    <style>
    /* 1. Reset Total Layout */
    [data-testid="stMainViewBlockContainer"] {{
        padding: 0 !important;
        max-width: 100% !important;
    }}
    
    header {{visibility: hidden;}} /* Sembunyikan header default streamlit */

    /* 2. Full Screen Background */
    .stApp {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    /* 3. Styling Teks Agar Persis Gambar */
    .hero-container {{
        padding: 60px;
        max-width: 800px;
        text-align: left; /* Rata kiri sesuai gambar Bunda */
        margin-left: 5%; /* Geser sedikit dari kiri */
    }}

    .hero-title {{
        font-family: 'DM Serif Display', serif; /* Font elegan mirip gambar */
        color: #604F3B;
        font-size: 4.5rem;
        line-height: 1.1;
        margin-bottom: 20px;
        font-weight: 400;
    }}

    .hero-subtitle {{
        font-family: 'Nunito', sans-serif;
        color: #604F3B;
        font-size: 1.2rem;
        line-height: 1.6;
        max-width: 600px;
        margin-bottom: 40px;
        opacity: 0.9;
    }}

    /* 4. Tombol Reservasi Mewah */
    .stButton button {{
        background-color: #604F3B !important;
        color: #FCFCFC !important;
        border-radius: 0px !important; /* Kotak tajam/elegan sesuai desain premium */
        border: none !important;
        padding: 20px 40px !important;
        font-size: 1rem !important;
        letter-spacing: 2px !important;
        text-transform: uppercase;
        transition: 0.5s;
    }}

    .stButton button:hover {{
        background-color: #4A3D2E !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }}
    
    /* Footer kecil di bawah */
    .hero-footer {{
        position: absolute;
        bottom: 30px;
        width: 90%;
        display: flex;
        justify-content: space-between;
        color: #604F3B;
        font-size: 0.8rem;
        opacity: 0.7;
    }}
    </style>

    <div class="hero-container">
        <h1 class="hero-title">Reservasi Layanan &<br>Data Klien Annaira</h1>
        <p class="hero-subtitle">
            Setiap perjalanan bunda dan si kecil begitu berharga. <br>
            Melalui website ini, Annaira ingin memahami kebutuhan bunda dan bayi dengan 
            lebih baik agar sesi nantinya dapat berjalan dengan nyaman dan sesuai kebutuhan.
        </p>
    </div>
""", unsafe_allow_html=True)

# Letakkan tombol di bawah teks
col1, col2 = st.columns([1, 2])
with col1:
    if st.button("Mulai Reservasi"):
        st.switch_page("views/home.py")

st.markdown("""
    <div class="hero-footer">
        <span>Jadwalkan momen spesial bunda dan si kecil bersama Annaira 🤍</span>
        <span>annaira.homespa</span>
    </div>
""", unsafe_allow_html=True)
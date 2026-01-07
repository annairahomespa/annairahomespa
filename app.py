import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Annaira Home Spa", layout="wide")

# Inisialisasi Halaman
home_page = st.Page("views/home.py", title="Home", icon="🏠", default=True)
admin_page = st.Page("views/admin.py", title="Admin Dashboard", icon="📊")

# Navigasi
pg = st.navigation([home_page])

pg.run()
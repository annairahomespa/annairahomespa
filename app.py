import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Annaira Home Spa", layout="wide")

# Inisialisasi Halaman
home_page = st.Page("views/home.py", title="Home", icon="🏠")
admin_page = st.Page("views/admin.py", title="Admin Dashboard", icon="📊")
landing_page = st.Page("views/landing.py", title="Landing Page", icon="🏠", default=True)

# Navigasi
pg = st.navigation([landing_page, home_page, admin_page])

pg.run()
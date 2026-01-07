import streamlit as st

# Pengaturan halaman
st.set_page_config(page_title="Annaira Home Spa", layout="wide")

# Inisialisasi Halaman
home_page = st.Page("views/home.py", title="Home", icon="🏠", default=True)
new_page = st.Page("views/form_baru.py", title="Daftar Baru", icon="🆕")
old_page = st.Page("views/form_lama.py", title="Klien Lama", icon="💆")
admin_page = st.Page("views/admin.py", title="Admin Dashboard", icon="📊")

# Navigasi
pg = st.navigation({
    "Utama": [home_page],
    "Layanan": [new_page, old_page],
    "Internal": [admin_page]
})

pg.run()
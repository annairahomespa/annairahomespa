import streamlit as st
from datetime import datetime
import urllib.parse

DATA_CLIENT = [
    {
        "nama_bunda": "Bunda Alika",
        "usia_bunda": 28,
        "nama_anak": "Rafa",
        "tgl_lahir": "2023-05-10",
        "alamat": "Jl. Ahmad Yani No. 12, Amuntai",
        "patokan": "Dekat Masjid Raya",
        "instagram": "@alika_mom"
    },
    {
        "nama_bunda": "Bunda Sarah",
        "usia_bunda": 31,
        "nama_anak": "Zizi",
        "tgl_lahir": "2022-10-15",
        "alamat": "Komp. Perumahan Tanjung Indah Blok C",
        "patokan": "Pagar warna hijau",
        "instagram": "@sarah_parenting"
    }
]

st.write("Selamat datang, Bunda/Ayah.\n\n" \
"Terimakasih telah menghubungi Annaira 🩶\n\n" \
"Silahkan isi formulir berikut dengan data yang lengkap dan sesuai kondisi")

st.subheader("🗓️ Detail Reservasi")
col1, col2 = st.columns(2)

with col1:
    tgl_res = st.date_input("Tanggal Reservasi", value=datetime.now(), format="DD-MM-YYYY")

    kota = st.selectbox("Pilih Kota Layanan:", ["-- Pilih Kota Layanan --", "Amuntai", "Tanjung", "Lainnya"])
    
    kota_lainnya = ""
    if kota == "Lainnya":
        kota_lainnya = st.text_input("Sebutkan Nama Kota/Kecamatan:", placeholder="Contoh: Kalua")
            
with col2:
    jam_operasional = []
    for jam in range(8, 18):
        jam_operasional.append(f"{jam:02d}:00")
        jam_operasional.append(f"{jam:02d}:15")
        jam_operasional.append(f"{jam:02d}:30")
    
    jam_res = st.selectbox("Jam Reservasi", jam_operasional)

    kategori_layanan = st.selectbox("Pilih Layanan:", [
        "-- Pilih Kategori --",
        "Baby Treatment: usia 0-12 bulan",
        "Toddler Treatment: usia 1-3 tahun",
        "Kid Treatment: usia 3-6 tahun",
        "Mom Treatment",
        "Mom & Baby (Special Package)",
        "Mom Treatment (Konsultasi Menyusui)"
    ])

    sub_opsi = []
    
    if "Baby Treatment" in kategori_layanan:
        sub_opsi = [
            "Baby Massage (Rp 65.000)",
            "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 80.000)",
            "Immune Booster Massage: Kekebalan Tubuh (Rp 80.000)",
            "Tuina Massage: Nafsu Makan (Rp 80.000)",
            "Combine Massage: Terapi, Tuina, Imun Booster (Rp 100.000)"
        ]
    elif "Toddler Treatment" in kategori_layanan:
        sub_opsi = [
            "Toddler Massage (Rp 75.000)",
            "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 90.000)",
            "Immune Booster Massage: Kekebalan Tubuh (Rp 90.000)",
            "Tuina Massage: Nafsu Makan (Rp 90.000)",
            "Combine Massage: Terapi, Tuina, Imun Booster (Rp 110.000)"
        ]
    elif "Kid Treatment" in kategori_layanan:
        sub_opsi = [
            "Kid Massage (Rp 85.000)",
            "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 100.000)",
            "Immune Booster Massage: Kekebalan Tubuh (Rp 100.000)",
            "Tuina Massage: Nafsu Makan (Rp 100.000)",
            "Combine Massage: Terapi, Tuina, Imun Booster (Rp 120.000)"
        ]
    elif "Mom Treatment" == kategori_layanan:
        sub_opsi = [
            "Breast Care/Pijat Payudara (Sumbatan, Granjelan, Bengkak) (Rp 100.000)",
            "Oxytocin Massage/Pijat Punggung (Melancarkan Aliran ASI) (Rp 100.000)",
            "Lactation Massage/Pijat Payudara & Punggung (Rp 150.000)"
        ]
    elif "Konsultasi Menyusui" in kategori_layanan:
        sub_opsi = [
            "Konsultasi Menyusui Online via Chat (Rp 70.000)",
            "Konsultasi Menyusui Online via VC/Call (Rp 100.000)",
            "Konsultasi Menyusui Homevisit (Rp 130.000)",
            "Konsultasi Menyusui & Breast Care (Rp 200.000)",
            "Konsultasi Menyusui & Oxytocin Massage (Rp 200.000)",
            "Konsultasi Menyusui & Lactation Massage (Rp 260.000)"
        ]

    # Munculkan selectbox kedua untuk detail layanan
    layanan_final = st.selectbox("Pilih Detail Treatment:", sub_opsi)

st.divider()

status_client = st.radio("Status Client:", ["Client Baru", "Client Lama"], horizontal=True)

# Variabel penampung data autofill
val_nama_bunda = ""
val_usia_bunda = 25 
val_nama_anak = ""
val_tgl_anak = datetime(2023, 1, 1)
val_alamat = ""
val_patokan = ""
val_ig = ""

if status_client == "Client Lama":
    daftar_nama = [c["nama_bunda"] for c in DATA_CLIENT]
    search_nama = st.selectbox("Cari Nama Bunda/Ayah:", [""] + daftar_nama)
    
    if search_nama != "":
        user_data = next(item for item in DATA_CLIENT if item["nama_bunda"] == search_nama)
        val_nama_bunda = user_data["nama_bunda"]
        val_usia_bunda = user_data["usia_bunda"]
        val_nama_anak = user_data["nama_anak"]
        val_tgl_anak = datetime.strptime(user_data["tgl_lahir"], "%Y-%m-%d")
        val_alamat = user_data["alamat"]
        val_patokan = user_data["patokan"]
        val_ig = user_data["instagram"]

st.divider()

with st.form("form_biodata"):
    st.subheader("👨‍👩‍👧 Data Orang Tua & Anak")
    nama_bunda = st.text_input("Nama Lengkap Bunda/Ayah", value=val_nama_bunda)
    usia_bunda = st.number_input("Usia Bunda", min_value=15, max_value=60, value=val_usia_bunda)
    
    col3, col4 = st.columns(2)
    with col3:
        nama_anak = st.text_input("Nama Lengkap Anak", value=val_nama_anak)
        tgl_lahir_anak = st.date_input("Tanggal Lahir Anak", value=val_tgl_anak, format="DD-MM-YYYY")
    with col4:
        usia_anak_saat_ini = st.text_input("Usia Anak Saat Ini", placeholder="Contoh: 15 bulan")
        ig = st.text_input("Akun Instagram", value=val_ig)

    st.subheader("🩺 Kondisi Khusus / Keluhan")
    kondisi = st.radio(
        "Kondisi Saat Ini:",
        ["Tidak Ada", "Alergi Minyak", "Sedang Demam", "Batuk Pilek", "Kolik/Kembung", 
         "Diare", "Sembelit", "Payudara Bengkak", "Sumbatan ASI", "Yang lain:"]
    )
    keluhan_lain = st.text_input("Jika pilih 'Yang lain', sebutkan di sini:", placeholder="Kosongkan jika tidak ada")

    st.subheader("🏠 Alamat Lengkap")
    alamat = st.text_area("Alamat Rumah (Isi Lengkap)", value=val_alamat)
    patokan = st.text_input("Catatan Tambahan Alamat (Patokan Lokasi)", value=val_patokan)

    # Tombol submit form
    submitted = st.form_submit_button("Siapkan Pesan WhatsApp")

    if submitted:
        if not nama_bunda or not alamat:
            st.error("Nama dan Alamat harus diisi!")
        else:
            # Penentuan Nilai Final
            fix_kota = kota_lainnya if kota == "Lainnya" else kota
            fix_kondisi = keluhan_lain if kondisi == "Yang lain:" else kondisi
            
            # Format Pesan WhatsApp
            text_wa = (
                f"*RESERVASI ANNAIRA HOME SPA*\n"
                f"--------------------------------\n"
                f"📅 *Tanggal:* {tgl_res.strftime('%d-%m-%Y')} | ⏰ *Jam:* {jam_res}\n"
                f"📍 *Kota:* {fix_kota}\n"
                f"💆‍♀️ *Layanan:* {kategori_layanan}\n\n"
                f"✨ *Detail:* {layanan_final}\n\n"
                f"*Data Client:*\n"
                f"👤 Bunda/Ayah: {nama_bunda} ({usia_bunda} thn)\n"
                f"👶 Anak: {nama_anak}\n"
                f"🎂 Tgl Lahir Anak: {tgl_lahir_anak.strftime('%d-%m-%Y')}\n"
                f"📏 Usia Anak: {usia_anak_saat_ini}\n"
                f"📱 Instagram: {ig}\n\n"
                f"*Keluhan/Kondisi:* {fix_kondisi}\n\n"
                f"*Alamat Lengkap:*\n"
                f"{alamat}\n"
                f"📍 Patokan: {patokan}"
            )
            
            # Link WhatsApp (Ganti nomor di sini)
            encoded_text = urllib.parse.quote(text_wa)
            url_wa = f"https://wa.me/6282255514392?text={encoded_text}"
            
            st.success("✅ Data reservasi telah siap!")
            st.link_button("🚀 Kirim ke WhatsApp Sekarang", url_wa)
            st.balloons()
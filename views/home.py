import streamlit as st
from datetime import datetime
from datetime import date
import urllib.parse
import os

def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("views/css/home.css")

DATA_CLIENT = [
    {
        "nama_bunda": "Bunda Alika",
        "usia_bunda": 28,
        "nama_anak": "Rafa",
        "tgl_lahir": "2023-05-10",
        "alamat": "Jl. Ahmad Yani No. 12, Amuntai",
        "alamat pengasuh": "",
        "patokan": "Dekat Masjid Raya",
        "instagram": "@alika_mom"
    },
    {
        "nama_bunda": "Bunda Sarah",
        "usia_bunda": 31,
        "nama_anak": "Zizi",
        "tgl_lahir": "2022-10-15",
        "alamat": "Komp. Perumahan Tanjung Indah Blok C",
        "alamat pengasuh": "Sungai Malang RT 4",
        "patokan": "Pagar warna hijau",
        "instagram": "@sarah_parenting"
    }
]

LAYANAN_DATA = {
    "Baby Treatment: usia 0-12 bulan": [
        "Baby Massage (Rp 65.000)",
        "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 80.000)",
        "Immune Booster Massage: Kekebalan Tubuh (Rp 80.000)",
        "Tuina Massage: Nafsu Makan (Rp 80.000)",
        "Combine Massage: Terapi, Tuina, Imun Booster (Rp 100.000)"
    ],
    "Toddler Treatment: usia 1-3 tahun": [
        "Toddler Massage (Rp 75.000)",
        "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 90.000)",
        "Immune Booster Massage: Kekebalan Tubuh (Rp 90.000)",
        "Tuina Massage: Nafsu Makan (Rp 90.000)",
        "Combine Massage: Terapi, Tuina, Imun Booster (Rp 110.000)"
    ],
    "Kid Treatment: usia 3-6 tahun": [
        "Kid Massage (Rp 85.000)",
        "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 100.000)",
        "Immune Booster Massage: Kekebalan Tubuh (Rp 100.000)",
        "Tuina Massage: Nafsu Makan (Rp 100.000)",
        "Combine Massage: Terapi, Tuina, Imun Booster (Rp 120.000)"
    ],
    "Mom Treatment": [
        "Oxytocin Massage/Pijat Punggung (Melancarkan Aliran ASI): 45 menit (Rp 100.000)",
        "Breast Care/Pijat Payudara (Sumbatan, Granjelan, Bengkak): 45-60 menit (Rp 120.000)",
        "Lactation Massage/Pijat Payudara & Punggung (Melancarkan & Meningkatkan Produksi ASI): 70 menit (Rp 150.000)"
    ],
    "Konsultasi Menyusui": [
        "Online via Chat (Rp 70.000)",
        "Online via VC/Call 60 menit (Rp 100.000)",
        "Homevisit 60 menit (Rp 130.000)",
        "Konsultasi & Oxytocin Massage 100 menit (Rp 220.000)",
        "Konsultasi & Breast Care 110 menit (Rp 240.000)",
        "Konsultasi & Lactation Massage 120 menit (Rp 260.000)"
    ],
     "Mom & Baby (Special Package)": [
        "Happy Package: Pijat Laktasi 1x & Pijat Bayi 1x (Rp 205.000)",
        "Calm Package: Pijat Laktasi 1x & Pijat Bayi Terapi 1x (Rp 220.000)",
        "Love Package: Pijat Laktasi 2x & Pijat Bayi 2x (Rp 400.000)",
        "Mindfull Package: Pijat Laktasi 2x & Pijat Bayi Terapi 2x (Rp 420.000)"
    ]
}

def get_jam_operasional():
    return [f"{jam:02d}:{menit:02d}" for jam in range(8, 19) for menit in [0, 15, 30, 45]]

st.header("Annaira Home Spa")
st.write("Selamat datang, Bunda/Ayah. Terimakasih telah menghubungi Annaira 🤗\n\n"
         "Silahkan isi formulir berikut dengan data yang lengkap dan sesuai kondisi yaa")

with st.container(key="card_reservasi"):
    st.subheader("Detail Reservasi")
    col1, col2 = st.columns(2)

    with col1:
        tgl_res = st.date_input("Tanggal Reservasi", value=datetime.now(), format="DD-MM-YYYY")
        
        kota_opsi = ["-- Pilih Kota Layanan --", "Amuntai", "Tanjung", "Lainnya"]
        kota = st.selectbox("Pilih Kota Layanan:", kota_opsi)
        
        kota_final = kota
        if kota == "Lainnya":
            kota_final = st.text_input("Sebutkan Nama Kota/Kecamatan:", placeholder="Contoh: Kalua")

    with col2:
        jam_operasional = st.selectbox("Jam Reservasi", get_jam_operasional())
        
        kategori_layanan = st.selectbox("Pilih Kategori Layanan:", ["-- Pilih Kategori --"] + list(LAYANAN_DATA.keys()))

        layanan_final = None
        if kategori_layanan != "-- Pilih Kategori --":
            layanan_final = st.radio("Pilih Detail Treatment:", LAYANAN_DATA[kategori_layanan])

import streamlit as st
from datetime import datetime
 
default_data = {
    "nama_bunda": "",
    "usia_bunda": 25,
    "nama_anak": "",
    "tgl_lahir": datetime(2023, 1, 1),
    "alamat": "",
    "alamat pengasuh": "",
    "patokan": "",
    "instagram": ""
}

st.markdown("### **Status Client:**")
status_client = st.radio("", ["**Client Baru**", "**Client Lama**"], horizontal=True, label_visibility="collapsed")

def handle_client_lama_search(data_client):
    query = st.text_input("🔍 Cari Nama Bunda/Ayah:", placeholder="Ketik nama untuk mencari...")
    
    if not query:
        st.caption("Masukkan minimal 1 huruf untuk mencari data.")
        return None

    daftar_nama = sorted([c["nama_bunda"] for c in data_client])
    hasil_filter = [n for n in daftar_nama if query.lower() in n.lower()]

    if not hasil_filter:
        st.warning("⚠️ Nama tidak ditemukan. Coba ejaan lain atau daftar sebagai Client Baru.")
        return None

    st.info(f"Ditemukan {len(hasil_filter)} nama yang cocok:")
    selected_nama = st.radio(
        "Pilih salah satu:",
        options=hasil_filter,
        index=None,
        key="radio_client_lama"
    )
    
    # Cari objek data lengkap berdasarkan nama yang dipilih
    if selected_nama:
        return next((item for item in data_client if item["nama_bunda"] == selected_nama), None)
    
    return None

def update_default_with_client_data(default_dict, client_data):
    if client_data:
        default_dict.update(client_data)
        
        if isinstance(default_dict.get("tgl_lahir"), str):
            try:
                default_dict["tgl_lahir"] = datetime.strptime(default_dict["tgl_lahir"], "%Y-%m-%d")
            except ValueError:
                default_dict["tgl_lahir"] = datetime.now()
    return default_dict

if status_client == "**Client Lama**":
    client_terpilih = handle_client_lama_search(DATA_CLIENT)
    
    if client_terpilih:
        default_data = update_default_with_client_data(default_data, client_terpilih)
        st.success(f"Data {client_terpilih['nama_bunda']} berhasil dimuat!")

with st.form("form_biodata"):
    st.subheader("Data Orang Tua & Anak")
    
    if status_client == "**Client Baru**":
        nama_bunda = st.text_input("Nama Lengkap Bunda/Ayah", value=default_data["nama_bunda"], placeholder="Tulis di sini...")
        usia_bunda = st.number_input("Usia Bunda", 12, 80, value=default_data["usia_bunda"], placeholder="Tulis di sini...")
    
        col3, col4 = st.columns(2)
        with col3:
            nama_anak = st.text_input("Nama Lengkap Anak", value=default_data["nama_anak"], placeholder="Tulis di sini...")
            usia_anak_saat_ini = st.text_input("Usia Anak Saat Ini", placeholder="Tulis di sini...")
        
        with col4:
            tgl_anak = default_data.get("tgl_lahir", datetime.now())
            tgl_lahir_anak = st.date_input("Tanggal Lahir Anak", value=tgl_anak, format="DD-MM-YYYY")
            ig = st.text_input("Akun Instagram", value=default_data["instagram"], placeholder="Tulis di sini...")
    
        info_opsi = ["-- Pilih Opsi --", "Instagram", "Tiktok", "Whatsapp", "Twitter", "Rekomendasi Teman", "Mencari Sendiri di Social Media"]
        info_sumber = st.selectbox("Bunda/Ayah tau annaira dari mana?", info_opsi)
    
    else:
        nama_bunda = st.text_input("Nama Lengkap Bunda/Ayah", value=default_data["nama_bunda"], placeholder="Tulis di sini...")
        nama_anak = st.text_input("Nama Lengkap Anak", value=default_data["nama_anak"], placeholder="Tulis di sini...")
        usia_anak_saat_ini = st.text_input("Usia Anak Saat Ini", placeholder="Tulis di sini...")

    st.subheader("Kondisi Khusus / Keluhan")
    opsi_kondisi = [
        "Alergi Minyak", "Sedang Demam", "Batuk Pilek", 
        "Kolik/Kembung", "Diare", "Sembelit", "Payudara Bengkak", 
        "Sumbatan ASI"
    ]
    col1, col2 = st.columns(2)
    pilihan_user = []

    for i, opsi in enumerate(opsi_kondisi):
        with col1 if i % 2 == 0 else col2:
            if st.checkbox(opsi, key=opsi):
                pilihan_user.append(opsi)

    input_lain = st.text_input("Sebutkan keluhan lain:", placeholder="Tulis di sini...")
    if input_lain:
        pilihan_user.append(input_lain)
    fix_kondisi = ", ".join(pilihan_user) if pilihan_user else "Tidak Ada Kondisi Khusus/Keluhan"

    st.subheader("Alamat Lengkap")
    alamat = st.text_area("Alamat Rumah", value=default_data["alamat"], placeholder="Tulis di sini...")
    alamat_pengasuh = st.text_area("Alamat Pengasuh (Jika Ada)", value=default_data["alamat pengasuh"], placeholder="Tulis di sini...")
    patokan = st.text_input("Catatan Patokan Lokasi", value=default_data["patokan"], placeholder="Tulis di sini...")

    def tambah_data(baris_list, label, nilai):
        if nilai and str(nilai).strip() not in ["", "0", "None", "-- Pilih Kategori --"]:
            baris_list.append(f"• {label}: {nilai}")

    def get_informed_consent():
        st.subheader("Informed Consent")
        st.write("Silakan centang persetujuan di bawah ini:")
        
        # Menggunakan dictionary untuk checkbox agar lebih ringkas
        labels = {
            "ic1": "Saya memberikan izin dokumentasi foto/video selama perawatan untuk edukasi internal Annaira.",
            "ic2": "Saya memberikan izin dokumentasi foto/video untuk media promosi (Instagram, Tiktok, Brosur).",
            "ic3": "Saya memberikan izin dokumentasi foto/video (dengan catatan wajah ditutup).",
            "ic4": "Saya TIDAK memberikan izin dokumentasi foto/video.",
        }
        
        checks = {key: st.checkbox(val) for key, val in labels.items()}
        ic5 = st.checkbox("Saya menyetujui syarat & ketentuan layanan Annaira Homespa.")

        # Mapping hasil teks
        consent_list = []
        if checks["ic1"]: consent_list.append("Saya memberikan izin dokumentasi foto/video selama perawatan untuk edukasi internal Annaira.")
        if checks["ic2"]: consent_list.append("Saya memberikan izin dokumentasi foto/video untuk media promosi (Instagram, Tiktok, Brosur).")
        if checks["ic3"]: consent_list.append("Saya memberikan izin dokumentasi foto/video (dengan catatan wajah ditutup).")
        if checks["ic4"]: consent_list.append("Saya TIDAK memberikan izin dokumentasi foto/video.")

        ringkasan = "\n   - ".join(consent_list) if consent_list else "Tidak ada poin dipilih"
        return ringkasan, ic5

    def render_laktasi_form():
        st.divider()
        st.subheader("Data Tambahan Konsultasi Laktasi")
        st.info("Mohon lengkapi riwayat medis berikut.")
        
        col1, col2 = st.columns(2)
        with col1:
            data = {
                "WA Bunda": st.text_input("Nomor HP Bunda (WhatsApp)"),
                "Tgl Lahir Bunda": st.date_input("Tanggal Lahir Bunda", value=date(1990, 1, 1), min_value=date(1945, 1, 1), max_value=date.today(), format="DD-MM-YYYY"),
                "Pekerjaan": st.text_input("Pekerjaan Bunda"),
                "Anak Ke": st.number_input("Ananda merupakan anak ke berapa?", min_value=1, step=1)
            }
        with col2:
            data.update({
                "Tempat Lahir Anak": st.text_input("Tempat Lahir Anak"),
                "Jenis Kelamin Anak": st.selectbox("Jenis Kelamin Anak", ["Laki-laki", "Perempuan"]),
                "Usia Nifas": st.text_input("Usia Nifas (bila nifas)"),
                "Usia Kehamilan": st.text_input("Usia Kehamilan (jika hamil)")
            })

        st.markdown("---")
        st.subheader("Riwayat & Kebiasaan")
        data["riwayat menyusui sebelumnya"] = st.text_area("Ceritakan riwayat menyusui sebelumnya")
        data["Riwayat kehamilan dan persalinan saat ini"] = st.text_area("Riwayat kehamilan dan persalinan saat ini")
        data["Jenis Persalinan"] = st.selectbox("Jenis Persalinan", ["Persalinan Normal", "Operasi SC"])
        data["Tempat Persalinan"] = st.text_input("Tempat Persalinan (RS/Klinik/Rumah)")
        data["Usia Kehamilan"] = st.text_input("Usia Kehamilan (saat melahirkan)")
        data["Bunda dan Bayi melakukan IMD segera setelah persalinan"] = st.text_input("Apakah Bunda dan Bayi melakukan IMD segera setelah persalinan? Jika iya, berapa lama IMD dilakukan?")
        data["Setelah persalinan Bayi rawat gabung dengan Bunda"] = st.radio("Apakah setelah persalinan Bayi rawat gabung dengan Bunda?", ["Iya", "Tidak"])
        data["Kondisi kesehatan bayi setelah dilahirkan"] = st.text_area("Bagaimana kondisi kesehatan bayi setelah dilahirkan?")

        st.markdown("---")
        st.subheader("Kebiasaan & Nutrisi Bayi")
        data["Bayi pernah menggunakan dot"] = st.text_area("Apakah bayi pernah menggunakan dot?, sejak kapan dan ceritakan kronologisnya")
        data["Bayi mengkonsumsi ASI atau nutrisi lain"] = st.text_area("Apakah bayi mengkonsumsi ASI saja atau ada penambahan nutrisi lain?")
        data["Rincian BB"] = st.text_area("Rincian BB (berat badan) bayi tiap bulannya (Lahir - Sekarang)")

        st.markdown("---")
        st.subheader("Manajemen Laktasi Bunda")
        data["Kebiasaan Bunda dan hasilnya dalam proses memompa ASI"] = st.text_area("Bagaimana kebiasaan Bunda dan hasilnya dalam proses memompa ASI?")
        data["Bunda mengkonsumsi ASI booster?"] = st.text_area("Apakah Bunda mengkonsumsi ASI booster? Merk apa saja?")
        data["Bunda pernah melakukan konsultasi laktasi"] = st.radio("Apakah sebelumnya Bunda pernah melakukan konsultasi laktasi?", ["Pernah", "Belum Pernah"])
        data["Masalah menyusui Bunda yang belum terjabarkan"] = st.text_area("Ceritakan masalah menyusui Bunda yang belum terjabarkan")
        
        st.markdown("---")
        st.subheader("Riwayat Kondisi Kesehatan")
        options_medis = ["Persalinan Lama", "Sectio Caesarea", "Hipertensi", "Diabetes Melitus", "Penyakit Tiroid", "Obesitas", "PCOS", "Tidak Semua"]
        riwayat_medis = [opt for opt in options_medis if st.checkbox(opt)]
        data["Riwayat Kondisi Kesehatan"] = ", ".join(riwayat_medis) if riwayat_medis else "Tidak Ada"

        st.markdown("---")
        st.subheader("Dukungan & Harapan")
        data["Dukungan suami/keluarga agar Bunda sukses menyusui"] = st.text_area("Bagaimana dukungan suami/keluarga agar Bunda sukses menyusui?")
        data["Harapan Bunda dari konsultasi ini"] = st.text_area("Apa harapan Bunda dari konsultasi ini?")

        return data

    # --- 3. MAIN LOGIC ---
    detail_konsultasi_wa = ""

    if "Konsultasi Menyusui" in kategori_layanan:
        # Render form dan ambil datanya
        data_laktasi = render_laktasi_form()
        ringkasan_consent, ic5 = get_informed_consent()

        # Susun Pesan WA
        baris = ["*DATA TAMBAHAN KONSULTASI LAKTASI*"]
        for label, nilai in data_laktasi.items():
            tambah_data(baris, label, nilai)
        
        baris.append(f"\n*Izin Dokumentasi:*\n   - {ringkasan_consent}\n   - Setuju S&K layanan Annaira Homespa: {'YA' if ic5 else 'TIDAK'}\n")
        detail_konsultasi_wa = "\n".join(baris)

    elif "Mom Treatment" in kategori_layanan:
        st.divider()
        st.subheader("Data Tambahan Mom Treatment")
        
        nifas = st.text_input("Usia Nifas (bila nifas)")
        hamil = st.text_input("Usia Kehamilan (jika hamil)")
        persalinan = st.selectbox("Rencana Persalinan", ["Persalinan Normal", "Operasi SC"])

        baris = ["*Data Tambahan Mom Treatment*"]
        tambah_data(baris, "Usia Nifas (bila nifas)", nifas)
        tambah_data(baris, "Usia Kehamilan (jika hamil)", hamil)
        tambah_data(baris, "Rencana Persalinan", persalinan)
        detail_konsultasi_wa = "\n".join(baris)

    elif "Mom & Baby (Special Package)" in kategori_layanan:
        st.divider()
        st.subheader("Data Tambahan Mom & Baby")
        
        nifas = st.text_input("Usia Nifas (bila nifas)")
        hamil = st.text_input("Usia Kehamilan (jika hamil)")
        persalinan = st.selectbox("Jenis Persalinan", ["Persalinan Normal", "Operasi SC"])
        jam_operasional = st.selectbox("Jam Rencana Pertemuan Kedua", get_jam_operasional())
        rencana_tgl = st.date_input("Rencana Pertemuan Kedua", format="DD-MM-YYYY")
        ringkasan_consent, ic5 = get_informed_consent()

        baris = ["*DATA TAMBAHAN MOM & BABY*"]
        tambah_data(baris, "Usia Nifas (bila nifas)", nifas)
        tambah_data(baris, "Usia Kehamilan (jika hamil)", hamil)
        tambah_data(baris, "Jenis Persalinan", persalinan)
        tambah_data(baris, "Rencana Tgl Ke-2", rencana_tgl)
        tambah_data(baris, "Jam Rencana Pertemuan Ke-2", jam_operasional)
        baris.append(f"\n*Izin Dokumentasi:*\n   - {ringkasan_consent}\n   - Setuju S&K layanan Annaira Homespa: {'YA' if ic5 else 'TIDAK'}\n")
        detail_konsultasi_wa = "\n".join(baris)

    else:
        detail_konsultasi_wa = "Terima Kasih 🩶"

    # Tombol submit (masih dalam scope st.form utama)
    submitted = st.form_submit_button("Preview Pesanan Bunda") 
    st.write(
    f'<span style="opacity: {0.7};">Jika ada perubahan data diatas, tekan tombol preview lagi ya untuk update data nya!</span>', 
    unsafe_allow_html=True
)

if submitted:
    errors = []
    if not nama_bunda or not alamat:
        errors.append("Nama Lengkap dan Alamat Rumah wajib diisi.")
    
    if kategori_layanan == "-- Pilih Kategori --":
        errors.append("Pilih Kategori Layanan terlebih dahulu.")
    elif layanan_final in ["-- Pilih Kategori --", "No options to select"]:
        errors.append("Detail Treatment belum dipilih.")
        
    if kota == "-- Pilih Kota Layanan --":
        errors.append("Pilih Kota Layanan Anda.")
    elif kota == "Lainnya" and not kota_final:
        errors.append("Sebutkan nama Kota/Kecamatan Anda.")

    # Validasi Khusus Konsultasi (Harus Setuju S&K)
    is_konsultasi = any(x in kategori_layanan for x in ["Konsultasi Menyusui", "Mom & Baby"])
    if is_konsultasi and not ic5:
        errors.append("Anda harus menyetujui Syarat & Ketentuan (Informed Consent).")

    # Jika ada error, tampilkan semua sekaligus
    if errors:
        for err in errors:
            st.error(f"❌ {err}")
        st.stop()

    # 2. Pengolahan Data Final
    fix_kota = kota_final if kota == "Lainnya" else kota
    
    # Logic data tambahan berdasarkan status client
    info_tambahan = ""
    if status_client != "**Client Lama**":
        info_tambahan = (
            f"• Bunda/Ayah: {nama_bunda} ({usia_bunda} thn)\n"
            f"• Tgl Lahir Anak: {tgl_lahir_anak.strftime('%d-%m-%Y')}\n"
            f"• Instagram: {ig}\n"
            f"• Info tau Annaira: {info_sumber}\n\n"
        )
    
    info_alamat_pengasuh =""
    if alamat_pengasuh and alamat_pengasuh.strip():
        info_alamat_pengasuh = (
             f"• Alamat Pengasuh: {alamat_pengasuh.strip()}\n"
        )
        
    text_wa = (
        f"*RESERVASI ANNAIRA HOME SPA*\n"
        f"--------------------------------\n"
        f"*JADWAL & LAYANAN*\n"
        f"• Tanggal: {tgl_res.strftime('%d-%m-%Y')}\n"
        f"• Jam: {jam_operasional}\n"
        f"• Kota: {fix_kota}\n"
        f"• Layanan: {kategori_layanan}\n"
        f"• Detail Layanan: {layanan_final}\n\n"
        
        f"*DATA CLIENT*\n"
        f"• Bunda/Ayah: {nama_bunda}\n"
        f"• Anak: {nama_anak} ({usia_anak_saat_ini})\n"
        f"{info_tambahan}\n"
        
        f"*KONDISI & ALAMAT*\n"
        f"• Keluhan: {fix_kondisi}\n"
        f"• Alamat: {alamat}\n"
        f"{info_alamat_pengasuh}\n"
        f"• Patokan: {patokan}\n\n"
        
        f"{detail_konsultasi_wa}"
    )

    # 1. Encode URL
    encoded_text = urllib.parse.quote(text_wa)
    url_wa = f"https://wa.me/6282255514392?text={encoded_text}"

    # 2. Tampilkan Preview untuk meyakinkan pengguna
    with st.expander("🔍 Lihat Ringkasan Pesan", expanded=True):
        st.code(text_wa, language=None)

    # 3. Tombol Kirim yang mencolok (Paling Aman untuk Mobile)
    st.link_button("Konfirmasi Via Whatsapp ", url_wa, type="primary", use_container_width=True)

    # 4. Trigger otomatis (Opsional, letakkan di paling bawah)
    st.components.v1.html(f"""
        <script>
            window.parent.location.href = "{url_wa}";
        </script>
    """, height=0)
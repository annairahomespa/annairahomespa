import streamlit as st
from datetime import datetime
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

st.write("Selamat datang, Bunda/Ayah. Terimakasih telah menghubungi Annaira 🩶\n\n" \
"Silahkan isi formulir berikut dengan data yang lengkap dan sesuai kondisi yaa")

with st.container(key="card_reservasi"):
    st.subheader("Detail Reservasi")
    col1, col2 = st.columns(2)

    with col1:
        tgl_res = st.date_input("Tanggal Reservasi", value=datetime.now(), format="DD-MM-YYYY")

        kota = st.selectbox("Pilih Kota Layanan:", ["-- Pilih Kota Layanan --", "Amuntai", "Tanjung", "Lainnya"])
        
        kota_lainnya = ""
        if kota == "Lainnya":
            kota_lainnya = st.text_input("Sebutkan Nama Kota/Kecamatan:", placeholder="Contoh: Kalua")
                
    with col2:
        jam_operasional = []
        for jam in range(8, 19):
            jam_operasional.append(f"{jam:02d}:00")
            jam_operasional.append(f"{jam:02d}:15")
            jam_operasional.append(f"{jam:02d}:30")
            jam_operasional.append(f"{jam:02d}:45")
        
        jam_res = st.selectbox("Jam Reservasi", jam_operasional)

        kategori_layanan = st.selectbox("Pilih Layanan:", [
            "-- Pilih Kategori --",
            "Baby Treatment: usia 0-12 bulan",
            "Toddler Treatment: usia 1-3 tahun",
            "Kid Treatment: usia 3-6 tahun",
            "Mom Treatment",
            "Mom & Baby (Special Package)",
            "Konsultasi Menyusui"
        ])

        sub_opsi = []
        
        if "Baby Treatment: usia 0-12 bulan" in kategori_layanan:
            sub_opsi = [
                "Baby Massage (Rp 65.000)",
                "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 80.000)",
                "Immune Booster Massage: Kekebalan Tubuh (Rp 80.000)",
                "Tuina Massage: Nafsu Makan (Rp 80.000)",
                "Combine Massage: Terapi, Tuina, Imun Booster (Rp 100.000)"
            ]
        elif "Toddler Treatment: usia 1-3 tahun" in kategori_layanan:
            sub_opsi = [
                "Toddler Massage (Rp 75.000)",
                "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 90.000)",
                "Immune Booster Massage: Kekebalan Tubuh (Rp 90.000)",
                "Tuina Massage: Nafsu Makan (Rp 90.000)",
                "Combine Massage: Terapi, Tuina, Imun Booster (Rp 110.000)"
            ]
        elif "Kid Treatment: usia 3-6 tahun" in kategori_layanan:
            sub_opsi = [
                "Kid Massage (Rp 85.000)",
                "Therapy Massage: Batuk, Pilek, Kolik, Sembelit, Diare (Rp 100.000)",
                "Immune Booster Massage: Kekebalan Tubuh (Rp 100.000)",
                "Tuina Massage: Nafsu Makan (Rp 100.000)",
                "Combine Massage: Terapi, Tuina, Imun Booster (Rp 120.000)"
            ]
        elif "Mom Treatment" in kategori_layanan:
            sub_opsi = [
                "Breast Care/Pijat Payudara (Sumbatan, Granjelan, Bengkak) (Rp 100.000)",
                "Oxytocin Massage/Pijat Punggung (Melancarkan Aliran ASI) (Rp 100.000)",
                "Lactation Massage/Pijat Payudara & Punggung (Melancarkan & Meningkatkan Produksi ASI) (Rp 150.000)"
            ]
        elif "Mom & Baby (Special Package)" in kategori_layanan:
            sub_opsi = [
                "Happy Package: Pijat Laktasi 1x & Pijat Bayi 1x (Rp 205.000)",
                "Calm Package: Pijat Laktasi 1x & Pijat Bayi Terapi 1x (Rp 220.000)",
                "Love Package: Pijat Laktasi 2x & Pijat Bayi 2x (Rp 400.000)",
                "Mindfull Package: Pijat Laktasi 2x & Pijat Bayi Terapi 2x (Rp 420.000)"
            ]
        elif "Konsultasi Menyusui" in kategori_layanan:
            sub_opsi = [
                "-- Pilih Kategori --",
                "Konsultasi Menyusui Online via Chat (Rp 70.000)",
                "Konsultasi Menyusui Online via VC/Call 60 menit (Rp 100.000)",
                "Konsultasi Menyusui Homevisit 60 menit (Rp 130.000)",
                "Konsultasi Menyusui & Oxytocin Massage 100 menit (Rp 220.000)",
                "Konsultasi Menyusui & Breast Care 110 menit (Rp 240.000)",
                "Konsultasi Menyusui & Lactation Massage 120 menit (Rp 260.000)"
            ]

        # Munculkan selectbox kedua untuk detail layanan
        if kategori_layanan != "-- Pilih Kategori --":
            layanan_final = st.radio("Pilih Detail Treatment:", sub_opsi)
        else:
            layanan_final = "-- Pilih Kategori --"

st.markdown("### **Status Client:**")
status_client = st.radio("",["**Client Baru**", "**Client Lama**"], horizontal=True, label_visibility="collapsed")

# Variabel penampung data autofill
val_nama_bunda = ""
val_usia_bunda = 25 
val_nama_anak = ""
val_tgl_anak = datetime(2023, 1, 1)
val_alamat = ""
val_alamat_pengasuh =""
val_patokan = ""
val_ig = ""

if status_client == "**Client Lama**":
    daftar_nama = sorted([c["nama_bunda"] for c in DATA_CLIENT])
    search_nama = st.selectbox(
        "Cari Nama Bunda/Ayah (Ketik untuk mencari):", 
        options=[""] + daftar_nama,
        index=0
    )
    
    if search_nama != "":
        user_data = next(item for item in DATA_CLIENT if item["nama_bunda"] == search_nama)
        val_nama_bunda = user_data["nama_bunda"]
        val_usia_bunda = user_data["usia_bunda"]
        val_nama_anak = user_data["nama_anak"]
        val_tgl_anak = datetime.strptime(user_data["tgl_lahir"], "%Y-%m-%d")
        val_alamat = user_data["alamat"]
        val_alamat_pengasuh = user_data["alamat pengasuh"]
        val_patokan = user_data["patokan"]
        val_ig = user_data["instagram"]

with st.form("form_biodata"):
    st.subheader("Data Orang Tua & Anak")
    nama_bunda = st.text_input("Nama Lengkap Bunda/Ayah", value=val_nama_bunda)
    usia_bunda = st.number_input("Usia Bunda", min_value=12, max_value=80, value=val_usia_bunda)
    
    col3, col4 = st.columns(2)
    with col3:
        nama_anak = st.text_input("Nama Lengkap Anak", value=val_nama_anak)
        ig = st.text_input("Akun Instagram", value=val_ig, placeholder="annaira.homespa")
    with col4:
        if status_client != "**Client Lama**":
            tgl_lahir_anak = st.date_input("Tanggal Lahir Anak", value=val_tgl_anak, format="DD-MM-YYYY")
        usia_anak_saat_ini = st.text_input("Usia Anak Saat Ini")
    
    if status_client != "**Client Lama**":
        info = st.text_input("Bunda/Ayah tau annaira dari mana?")

    st.subheader("Kondisi Khusus / Keluhan")
    kondisi = st.radio(
        "Kondisi Saat Ini:",
        ["Tidak Ada", "Alergi Minyak", "Sedang Demam", "Batuk Pilek", "Kolik/Kembung", 
         "Diare", "Sembelit", "Payudara Bengkak", "Sumbatan ASI", "Yang lain:"]
    )
    keluhan_lain = st.text_input("Jika pilih 'Yang lain', sebutkan di sini:", placeholder="Kosongkan jika tidak ada")

    st.subheader("Alamat Lengkap")
    alamat = st.text_area("Alamat Rumah (Isi Lengkap)", value=val_alamat, placeholder="Jl Annaira RT.7 No.44 Tirto Utomo")
    alamat_pengasuh = st.text_area("Alamat Pengasuh (Jika Ada)", value=val_alamat_pengasuh)
    patokan = st.text_input("Catatan Tambahan Alamat (Patokan Lokasi)", value=val_patokan, placeholder="Samping Mesjid Al Karomah")

    def tambah_data(baris_list, label, nilai):
        if nilai and str(nilai).strip() not in ["", "0", "None", "-- Pilih Kategori --"]:
            baris_list.append(f"• {label}: {nilai}")

    def get_informed_consent():
        st.subheader("✅ Informed Consent")
        st.write("Silakan centang persetujuan di bawah ini:")
        
        ic1 = st.checkbox("Saya memberikan izin dokumentasi foto/video selama perawatan untuk edukasi internal Annaira.")
        ic2 = st.checkbox("Saya memberikan izin dokumentasi foto/video untuk media promosi (Instagram, Tiktok, Brosur).")
        ic3 = st.checkbox("Saya memberikan izin dokumentasi foto/video (dengan catatan wajah ditutup).")
        ic4 = st.checkbox("Saya tidak memberikan izin dokumentasi foto/video.")
        ic5 = st.checkbox("Saya menyetujui syarat & ketentuan layanan Annaira Homespa.")

        consent_list = []
        if ic1: consent_list.append("Izin Edukasi Internal")
        if ic2: consent_list.append("Izin Media Promosi")
        if ic3: consent_list.append("Izin Dokumentasi (Wajah Ditutup)")
        if ic4: consent_list.append("TIDAK MEMBERIKAN IZIN DOKUMENTASI")
        
        ringkasan = "\n   - ".join(consent_list) if consent_list else "Tidak ada poin dokumentasi yang dipilih"
        return ringkasan, ic5

    detail_konsultasi_wa = ""

    if "Konsultasi Menyusui" in kategori_layanan:
        st.divider()
        st.subheader("Data Tambahan Konsultasi Laktasi")
        st.info("Mohon lengkapi riwayat medis berikut untuk memaksimalkan sesi konsultasi.")
        
        c1, c2 = st.columns(2)
        with c1:
            wa_bunda = st.text_input("Nomor HP Bunda (WhatsApp)")
            tgl_lahir_bunda = st.date_input("Tanggal Lahir Bunda", format="DD-MM-YYYY")
            pekerjaan = st.text_input("Pekerjaan Bunda")
            anak_ke = st.number_input("Ananda merupakan anak ke berapa?", min_value=1, step=1)
        with c2:
            tempat_lahir_anak = st.text_input("Tempat Lahir Anak")
            jk_anak = st.selectbox("Jenis Kelamin Anak", ["Laki-laki", "Perempuan"])
            usia_nifas = st.text_input("Usia Nifas (bila nifas)")
            usia_hamil = st.text_input("Usia Kehamilan (jika hamil)")

        st.markdown("---")
        st.subheader("Riwayat Kehamilan & Persalinan")
        riwayat_sebelumnya = st.text_area("Ceritakan riwayat menyusui anak sebelumnya")
        riwayat_sekarang = st.text_area("Riwayat kehamilan dan persalinan saat ini")
        
        c3, c4 = st.columns(2)
        with c3:
            jenis_persalinan = st.selectbox("Jenis Persalinan saat ini", ["Persalinan Normal", "Operasi SC (Sesar)"])
            usia_kehamilan_lahir = st.text_input("Usia Kehamilan (saat melahirkan)")
        with c4:
            tempat_persalinan = st.text_input("Tempat Persalinan (RS/Klinik/Rumah)")

        imd_detail = st.text_input("Apakah Bunda dan Bayi melakukan IMD segera setelah persalinan? Jika iya, berapa lama IMD dilakukan?")
        rawat_gabung = st.radio("Apakah setelah persalinan Bayi rawat gabung dengan Bunda?", ["Iya", "Tidak"])
        kondisi_bayi = st.text_area("Bagaimana kondisi kesehatan bayi setelah dilahirkan?")
        
        st.markdown("---")
        st.subheader("Kebiasaan & Nutrisi Bayi")
        dot_detail = st.text_area("Apakah bayi pernah menggunakan dot?, sejak kapan dan ceritakan kronologisnya")
        asi_saja = st.text_area("Apakah bayi mengkonsumsi ASI saja atau ada penambahan nutrisi lain?")
        bb_bayi = st.text_area("Rincian BB (berat badan) bayi tiap bulannya (Lahir - Sekarang)")
        
        st.markdown("---")
        st.subheader("Manajemen Laktasi Bunda")
        kebiasaan_pompa = st.text_area("Bagaimana kebiasaan Bunda dan hasilnya dalam proses memompa ASI?")
        asi_booster = st.text_area("Apakah Bunda mengkonsumsi ASI booster? Merk apa saja?")
        konsul_sebelumnya = st.radio("Apakah sebelumnya Bunda pernah melakukan konsultasi laktasi?", ["Pernah", "Belum Pernah"])
        masalah_lain = st.text_area("Ceritakan masalah menyusui Bunda yang belum terjabarkan")

        options_medis = ["Persalinan Lama", "Sectio Caesarea", "Hipertensi", "Diabetes Melitus", "Penyakit Tiroid", "Obesitas", "Pcos", "Tidak Semua"]
        st.subheader("Riwayat kondisi kesehatan:")
        hasil_pilihan = {opt: st.checkbox(opt) for opt in options_medis}
        
        st.markdown("---")
        st.subheader("Dukungan & Harapan")
        dukungan = st.text_area("Bagaimana dukungan suami/keluarga agar Bunda sukses menyusui?")
        harapan = st.text_area("Apa harapan Bunda dari konsultasi/pijat ini?")

        ringkasan_consent, ic5 = get_informed_consent()

        # --- PROSES RINGKASAN DATA ---
        baris_data = ["*📋 DATA TAMBAHAN KONSULTASI LAKTASI*"]
        
        tambah_data(baris_data, "WA Bunda", wa_bunda)
        tambah_data(baris_data, "Pekerjaan", pekerjaan)
        tambah_data(baris_data, "Anak Ke", anak_ke)
        tambah_data(baris_data, "Jenis Kelamin Anak", jk_anak)
        tambah_data(baris_data, "Usia Nifas", usia_nifas)
        tambah_data(baris_data, "Usia Kehamilan", usia_hamil)
        
        tambah_data(baris_data, "Riwayat Menyusui Sblmnya", riwayat_sebelumnya)
        tambah_data(baris_data, "Riwayat Kehamilan Saat Ini", riwayat_sekarang)
        tambah_data(baris_data, "Jenis Persalinan", jenis_persalinan)
        tambah_data(baris_data, "IMD", imd_detail)
        tambah_data(baris_data, "Rawat Gabung", rawat_gabung)
        
        tambah_data(baris_data, "Nutrisi ASI Saja", asi_saja)
        tambah_data(baris_data, "BB Bayi", bb_bayi)
        tambah_data(baris_data, "Masalah Lain", masalah_lain)

        # Masukkan Riwayat Medis dari Checkbox
        riwayat_terpilih = [k for k, v in hasil_pilihan.items() if v]
        if riwayat_terpilih:
            tambah_data(baris_data, "Riwayat Medis", ", ".join(riwayat_terpilih))

        tambah_data(baris_data, "Dukungan Keluarga", dukungan)
        tambah_data(baris_data, "Harapan", harapan)

        baris_data.append(f"\n*Izin Dokumentasi:*\n   - {ringkasan_consent}")
        baris_data.append(f"• Setuju S&K: {'YA' if ic5 else 'TIDAK'}")

        detail_konsultasi_wa = "\n".join(baris_data)

    elif "Mom & Baby (Special Package)" in kategori_layanan:
        st.divider()
        st.subheader("Data Tambahan Mom & Baby")
        usia_nifas = st.text_input("Usia Nifas (bila nifas)")
        usia_kehamilan = st.text_input("Usia Kehamilan (jika hamil)")
        rencana_persalinan = st.selectbox("Rencana Persalinan", ["Persalinan Normal", "Operasi SC (Sesar)"])

        c1, c2 = st.columns(2)
        with c1:
            rencana_pertemuan_2 = st.date_input("Rencana Tanggal Pertemuan Kedua", format="DD-MM-YYYY")
        with c2:
            jam_pertemuan_2 = st.selectbox("Jam Rencana Pertemuan Kedua", jam_operasional)

        # Panggil Fungsi Consent
        ringkasan_consent, ic5 = get_informed_consent()

        baris_data = ["*📋 DATA TAMBAHAN MOM & BABY (Special Package)*"]
        tambah_data(baris_data, "Usia Nifas", usia_nifas)
        tambah_data(baris_data, "Usia Kehamilan", usia_kehamilan)
        tambah_data(baris_data, "Rencana Persalinan", rencana_persalinan)
        tambah_data(baris_data, "Tanggal Pertemuan Kedua", rencana_pertemuan_2)
        tambah_data(baris_data, "Jam Pertemuan Kedua", jam_pertemuan_2)
        
        baris_data.append(f"\n*Izin Dokumentasi:*\n   - {ringkasan_consent}")
        baris_data.append(f"• Setuju S&K: {'YA' if ic5 else 'TIDAK'}")

        detail_konsultasi_wa = "\n".join(baris_data)

    else:
        detail_konsultasi_wa = "Terima Kasih 🩶"

    # Tombol submit form
    submitted = st.form_submit_button("Siapkan Pesan WhatsApp")

    if submitted:
        # 1. CEK VALIDASI DASAR (Nama, Alamat, Kategori Utama)
        if not nama_bunda:
            st.error("❌ Mohon lengkapi Nama, Alamat, dan Pilih Layanan!")
        elif not alamat:
            st.error("❌ Mohon lengkapi Alamat")
        elif kategori_layanan == "-- Pilih Kategori --":
             st.error("❌ Mohon Pilih Layanan yang anda butuhkan!")
        
        # 2. CEK VALIDASI KOTA (Jika pilih 'Lainnya' tapi teks kosong)
        elif kota == "Lainnya" and not kota_lainnya:
            st.error("❌ Mohon sebutkan nama Kota/Kecamatan Anda!")
        elif kota == "-- Pilih Kota Layanan --":
            st.error("❌ Mohon pilih Kota Layanan Anda!")

        # 3. CEK VALIDASI DETAIL TREATMENT (Agar tidak terkirim "-- Pilih Detail Treatment --")
        elif layanan_final == "-- Pilih Detail Treatment --" or layanan_final == "No options to select":
            st.error("❌ Mohon pilih Detail Treatment yang diinginkan!")

        # 4. CEK VALIDASI INFORMED CONSENT (Syarat No. 4 untuk Konsultasi)
        elif "Konsultasi Menyusui" in kategori_layanan or "Mom & Baby (Special Package)" in kategori_layanan and not ic5: # Sesuaikan ic5 adalah checkbox S&K Bunda
            st.error("❌ Untuk layanan konsultasi, Anda harus menyetujui Syarat & Ketentuan layanan Annaira Homespa (Informed Consent).")

        # 5. JIKA SEMUA SUDAH OK
        else:
            st.success("✅ Data lengkap! Sedang menyiapkan pesan WhatsApp...")
            
            # Penentuan data final
            fix_kota = kota_lainnya if kota == "Lainnya" else kota
            fix_kondisi = keluhan_lain if kondisi == "Yang lain:" else kondisi

            if status_client == "**Client Lama**":
                display_tgl_anak = ""
                display_info =""
            else:
                display_tgl_anak = f"Tgl Lahir Anak: {tgl_lahir_anak.strftime('%d-%m-%Y')}\n"
                display_info = f"Info: {info}\n\n"
                
            text_wa = (
                f"*RESERVASI ANNAIRA HOME SPA*\n"
                f"--------------------------------\n"
                f"*Tanggal:* {tgl_res.strftime('%d-%m-%Y')}\n"
                f"*Jam:* {jam_res}\n"
                f"*Kota:* {fix_kota}\n"
                f"*Layanan:* {kategori_layanan}\n"
                f"*Detail:* {layanan_final}\n\n"
                f"*Data Client:*\n"
                f"Bunda/Ayah: {nama_bunda} ({usia_bunda} thn)\n"
                f"Anak: {nama_anak}\n"
                f"{display_tgl_anak}"
                f"Usia Anak: {usia_anak_saat_ini}\n"
                f"Instagram: {ig}\n\n"
                f"{display_info}"
                f"*Keluhan/Kondisi:* {fix_kondisi}\n\n"
                f"*Alamat Lengkap:*\n"
                f"{alamat}\n"
                f"{alamat_pengasuh}\n"
                f"Patokan: {patokan}\n"
                f"{detail_konsultasi_wa}"
            )
            
            encoded_text = urllib.parse.quote(text_wa)
            url_wa = f"https://wa.me/6282255514392?text={encoded_text}"
            
            st.markdown(f'<meta http-equiv="refresh" content="0;url={url_wa}">', unsafe_allow_html=True)
            st.write(f"Mengarahkan ke WhatsApp... Jika tidak otomatis, [klik di sini]({url_wa})")
            st.stop()
            st.balloons()
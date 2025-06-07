import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Set page configuration
st.set_page_config(
    page_title="Aplikasi Sanber Campus",
    page_icon=":school:",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Selamat Data di Aplikasi Sanber Campus")

with st.sidebar:
    st.subheader("Input teks")
    user_input = st.text_input("Masukkan nama Anda:")
    isian = st.text_area("Tulis pesan Anda di sini:", height=100)
    umur = st.number_input("Masukkan umur Anda:", min_value=0, max_value=100, value=25)

tab_1, tab_2 = st.tabs(["Tab Umum", "Tab Visual"])

st.header("Ini ada contoh penggunaan kolom", divider=True)
with tab_1:
    col_1, col_2 = st.columns([2,1])

    wadah = st.container()

    with col_1:
        st.header("Aplikasi ini dibuat untuk memenuhi tugas akhir Sanbercode")
        with st.container(border=True):
            st.subheader("Ini adalah subjudul")
            st.text("Ini adalah teks biasa yang menjelaskan aplikasi ini.")
            st.markdown("**Ini adalah teks tebal** dan _ini adalah teks miring_.")
            st.markdown("#### Ini adalah judul dengan ukuran lebih kecil")
            st.subheader("Ini adalah subjudul kedua")
        st.write("Ini adalah contoh kode python menggunakan markdown:")
        st.markdown("""
        ```javascript
        function helloWorld() {
            console.log("Hello, World!");
        }
        ```
        """)
        st.subheader("Ini adalah contoh penggunaan LateX")
        st.latex(r"""
        \int_{a}^{b} x^2 \, dx = \frac{b^3}{3} - \frac{a^3}{3}
        """)

        if st.button("Klik untuk melihat pesan"):
            wadah.success("Anda telah mengklik tombol di bawah!")
            st.balloons()
    with col_2:
        st.subheader("Ini adalah contoh penggunaan write", divider=True)
        data_dict = {
            "Nama": "John Doe",
            "Umur": 25,
            "Kota": "Jakarta",
            "Hobi": ["Membaca", "Bersepeda", "Bermain Musik"]
        }

        st.write("Data Pengguna:")
        st.write(data_dict)

        st.subheader("Ini adalah contoh penggunaan blok kode")
        st.code("""
        def greet(name):
            return f"Hello, {name}! Welcome to Sanber Campus. Let's learn together!"
        print(greet("Sanber Campus"))
        """, language='python')

        st.header("Ini adalah input pengguna", divider=True)
        st.subheader("tombol")
        if st.button("Klik Saya"):
            st.write("Tombol telah diklik!")
            st.balloons()
        else:
            st.write("Tombol belum diklik.")

with tab_2:
    st.header("Ini adalah contoh Data Terstruktur dan Media", divider=True)
    st.subheader("Tabel Data Pengguna")

    data = {
        'Nama Produk': [f'Produk {chr(65+i)}' for i in range(10)],
        'Harga (Rp)': np.random.randint(10000, 100000, 10),
        'Stok': np.random.randint(0, 100, 10),
        'Terjual': np.random.randint(0, 50, 10)
    }

    df_produk = pd.DataFrame(data)
    st.subheader("Tabel Produk dalam DataFrame")
    st.dataframe(df_produk)

    st.subheader("Tabel Produk dalam Format Tabel")
    st.table(df_produk)

    with st.expander("Image, Audio, dan Video"):
        st.write("Ini adalah contoh penggunaan gambar, audio, dan video dalam Streamlit.")
        st.write("Anda dapat menambahkan gambar, audio, dan video untuk memperkaya konten aplikasi Anda.")

        st.subheader("Gambar Produk")
        image_url = "C:\\Users\\Thio perdana\\Downloads\\7.png"
        st.image(image_url, caption="Image from URL", width=600)

        st.subheader("Contoh Audio dan Video")
        import scipy.io.wavfile as wav
        try:
            st.subheader("Audio dari File (Dummy):")
            # Membuat file WAV dummy sederhana (nada sinus)
            sample_rate = 44100  # Hz
            duration = 3  # detik
            frequency = 440  # Hz (Nada A)
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            note = np.sin(frequency * t * 2 * np.pi)
            # Normalisasi ke 16-bit PCM
            audio_data = (note * 32767 / np.max(np.abs(note))).astype(np.int16)
            wav.write("dummy_audio.wav", sample_rate, audio_data)

            st.audio("dummy_audio.wav", format="audio/wav")
            st.caption("Audio dummy nada sinus (A4) selama 3 detik.")

            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ", start_time=0)

        except Exception as e:
            st.error(f"Tidak bisa membuat atau memutar audio dummy: {e}")
            st.info("Untuk mencoba st.audio dengan file Anda sendiri, letakkan file audio (misal .mp3 atau .wav) di direktori yang sama dan ganti nama filenya.")

    st.header("Ini adalah contoh penggunaan grafik", divider=True)

    # Data contoh
    x = np.linspace(0, 10, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    # 1. Plot Matplotlib Sederhana
    st.subheader("Plot Garis Matplotlib Sederhana")
    fig_mpl, ax_mpl = plt.subplots() # Membuat figure dan axes
    ax_mpl.plot(x, y_sin, label="Sin(x)")
    ax_mpl.plot(x, y_cos, label="Cos(x)", linestyle="--")
    ax_mpl.set_xlabel("X-axis")
    ax_mpl.set_ylabel("Y-axis")
    ax_mpl.set_title("Grafik Sinus dan Cosinus")
    ax_mpl.legend()


    st.pyplot(fig_mpl) # Menampilkan plot di Streamlit

    # Membersihkan figure saat ini agar tidak memengaruhi plot Seaborn berikutnya
    plt.clf()

    # 2. Plot Seaborn Sederhana (Bar Chart)
    st.subheader("Bar Chart Seaborn Sederhana")
    # Data untuk bar chart
    kategori = ['A', 'B', 'C', 'D', 'E']
    nilai = np.random.randint(10, 100, size=len(kategori))
    df_bar = pd.DataFrame({'Kategori': kategori, 'Nilai': nilai})

    fig_sns, ax_sns = plt.subplots() # Membuat figure dan axes baru
    sns.barplot(x='Kategori', y='Nilai', data=df_bar, ax=ax_sns, palette="viridis")
    ax_sns.set_title("Contoh Bar Chart dengan Seaborn")
    st.pyplot(fig_sns) # Menampilkan plot di Streamlit

    plt.clf()

    # menampilkan plot menggunakan plotly
    st.subheader("Plot Interaktif dengan Plotly")
    import plotly.graph_objects as go

    # Membuat data untuk plot interaktif
    fig_plotly = go.Figure()
    fig_plotly.add_trace(go.Scatter(x=x, y=y_sin, mode='lines', name='Sin(x)'))
    fig_plotly.add_trace(go.Scatter(x=x, y=y_cos, mode='lines', name='Cos(x)', line=dict(dash='dash')))
    fig_plotly.update_layout(
        title="Grafik Interaktif Sinus dan Cosinus",
        xaxis_title="X-axis",
        yaxis_title="Y-axis"
    )

    st.plotly_chart(fig_plotly, use_container_width=True)

    st.subheader("Contoh visual bawaan streamlit")
    st.line_chart(df_produk['Harga (Rp)'])
    st.subheader("Contoh visual bawaan streamlit dengan data acak")
    st.area_chart(np.random.randn(100, 3), use_container_width=True)
    st.subheader("Contoh visual bawaan streamlit dengan data acak")
    st.bar_chart(np.random.randint(1, 100, size=(10, 3)), use_container_width=True)
    st.write(np.random.randint(1, 100, size=(10, 3)))

    st.header("Ini adalah contoh penggunaan map")


    map_data = pd.DataFrame({
        'nama_kota': ['Jakarta', 'Surabaya', 'Medan', 'Makassar', 'Bandung'],
        'lat': [-6.2088, -7.2575, 3.5952, -5.1477, -6.9175],
        'lon': [106.8456, 112.7521, 98.6722, 119.4169, 107.6191],
        'populasi_dummy': np.random.randint(1000000, 10000000, 5) # Data tambahan untuk ukuran titik (opsional)
    })

    st.write("Peta Kota di Indonesia")
    st.map(map_data, zoom=12)
    st.write("Data Kota:")
    st.dataframe(map_data)
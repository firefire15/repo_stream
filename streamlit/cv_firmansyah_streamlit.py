import streamlit as st

st.set_page_config(
    page_title="Curriculum Vitae",
    page_icon=":school:",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    image_url = "C:\\Users\\USER\\PycharmProjects\\cv_firmansyah\\streamlit\\pas photo.jpg"
    st.image(image_url, caption="", width=250)
    st.text("Sebagai seorang profesional lulusan Universitas Telkom dan Universitas Kristen Maranatha yang telah berpengalaman di bidang Teknologi informasi khususnya pada Software Engineer dengan spesialisai Backend Engineer dan analisis data sejak tahun 2016. Telah bekerja pada beberapa perusahaan baik nasional maupun multinasional yang memiliki beberapa kemampuan seperti pemrograman python, Java, Hibernate serta beberapa database seperti MySQL dan MongoDB. ")


st.title("FIRMANSYAH")
st.subheader("Software Engineering")
st.markdown("#### Riwayat Pendidikan")
st.markdown('##### **TEKNIK INFORMATIKA - UNIVERSITAS KRISTEN MARANATHA (S-1)**')
st.markdown('###### Agustus 2014 – Februari 2016')
st.markdown('##### **SISTEM INFORMASI - UNIVERSITAS TELKOM (D-3)**')
st.markdown('###### Agustus 2010 – September 2013')
st.markdown('##### **SMAN 2 CIMAHI**')
st.markdown('###### 2007–2010')

st.markdown("#### Riwayat Pekerjaan")
st.markdown('##### **Kemakmuran LLC - Software Engineer**')
st.markdown('###### 2024–sekarang')
st.markdown('1.	Melakukan monitoring dan bug fixing dari program algotrading yang dijalankan')
st.markdown('2.	Melakukan pengujian, evaluasi dan analisis data dari hasil trading dengan instrument finansial tertentu')
st.markdown('3.	Melakukan dokumentasi program.')
st.write("---")
st.markdown(' **PT Makmur Algo Indotama - Software Engineer**')
st.markdown('Januari 2020 – April 2024')
st.markdown('1.	Membuat sebuah sistem Algotrading di Bursa Saham luar negeri dan Direct Market Access (DMA) untuk transaksi jual-beli saham di Bursa Efek Indonesia serta melakukan audi dengan pihak ketiga.')
st.markdown('2.	Melakukan pengujian, evaluasi, dan analisis data dengan instrument finansial tertentu.')
st.markdown('3.	Melakukan dokumentasi program ')
st.write("---")
st.markdown('**PT Ebdesk Technology - Backend Programmer**')
st.markdown('April 2016 – Desember 2019')
st.markdown('**1.	Project Intelligence Socio Robot**')
st.markdown('a.	Membuat sebuah endpoint untuk kepentingan frontend')
st.markdown('b.	Membuat engine untuk mengolah data dan statistic robot di media social')
st.markdown('**2.	Project Quest Intelligence Stock Analysis**')
st.markdown('a.	Membuat sebuah endpoint untuk kepentingan frontend')
st.markdown('b.	Membuat engine untuk menglah data saham dan analisis sentimen.')
st.markdown('c.	Menganalisis, membuat strategi algo, serta melakukan pengujian strategi (backtesting) terhadap saham-saham di Indonesia.')
st.write("---")

st.markdown("#### Sertifikasi")
st.markdown('SAP Fundamental EDUGATES® International Limited - Auckland Aotearoa New Zealand 2013')
#import library
import streamlit as st
import pandas as pd
import webbrowser as wb
from sklearn.naive_bayes import GaussianNB
from PIL import Image

#header website
st.write("""
# Web Klasifikasi Topik Tugas Akhir Mahasiswa DSI UNAND
Aplikasi Berbasis Web untuk Mengklasifikasikan **Topik Tugas Akhir** Mahasiswa Departemen Sistem Informasi UNAND 
"""
)
#image website
img = Image.open('topik.png')
st.image(img, width=1000)

#sidebar
st.sidebar.header('Inputkan Nilai Anda')
#inputan data tester
def input_user():
    sda = st.sidebar.slider('Nilai Struktur Data & Algoritma', 2.0, 4.0, 2.5)
    gis = st.sidebar.slider('Nilai Sistem Informasi Geografis', 2.0, 4.0, 2.5)
    ptb = st.sidebar.slider('Nilai Pemograman Teknologi Bergerak', 2.0, 4.0, 2.5)
    pweb = st.sidebar.slider('Nilai Pemograman Web', 2.0, 4.0, 2.5)
    sim = st.sidebar.slider('Nilai Sistem Informasi Manajemen', 2.0, 4.0, 2.5)
    erp = st.sidebar.slider('Nilai Enterprise Resource Planning', 2.0, 4.0, 2.5)
    bi = st.sidebar.slider('Nilai Business Intelligence', 2.0, 4.0, 2.5)
    apm = st.sidebar.slider('Nilai Aplikasi Pembelajaran Mesin', 2.0, 4.0, 2.5)
    data = {'SDA' : sda,
            'GIS' : gis,
            'PTB' : ptb,
            'PWEB' : pweb,
            'SIM' : sim,
            'ERP' : erp,
            'BI' : bi,
            'APM' : apm}
    fitur = pd.DataFrame(data, index=[0])
    return fitur
df = input_user()

#show inputan user
st.subheader('Nilai Inputan')
st.write(df)

#open data train
dataset=pd.read_csv('dataset.csv')

#declare feature and targer (train&test)
x = dataset.values[:,0:8]
y = dataset.values[:,8]

#NBC
model = GaussianNB()
model.fit(x,y)

#predict
prediksi = model.predict(df)
prediksi_proba = model.predict_proba(df)

#showpredict
st.subheader('Rekomendasi Topik Tugas Akhir')
st.write(prediksi)

#dosen
if (prediksi=="Business Intelligence"):
    st.subheader('Rekomendasi Dosen Pembimbing')
    st.write("""Hasdi Putra, MT """)
    st.write("""Rahmatika Pratama Santi, MT""")
    st.write("""Dwi Welly Sukma Nirad, MT """)
    st.write("""Febby Apri Wenando, M.Eng """)
elif (prediksi=="Sistem Informasi Geografis"):
    st.subheader('Rekomendasi Dosen Pembimbing')
    st.write("""Haris Suryamen, M.Sc""")
    st.write("""Ullya Mega Wahyuni, M.Kom""")
    st.write("""Hafizah Hanim, M.Kom""")
    st.write("""Fajril Akbar, M.Sc""")
elif (prediksi=="Enterprise Architecture"):
    st.subheader('Rekomendasi Dosen Pembimbing')
    st.write("""Prof. Surya Afnarius. Ph.D""")
    st.write("""Husnil Kamil, MT """)
    st.write("""Aina Hubby Aziira, M.Eng """)
    st.write("""Adi Arga Arifnur, M.Kom """)
else :
    st.subheader('Rekomendasi Dosen Pembimbing')
    st.write("""Ricky Akbar, M.Kom """)
    st.write("""Jefril Rahmadoni, M.Kom """)
    st.write("""Afriyanti Dwi Kartika, MT""")
    
#topik terkait
url = 'http://scholar.unand.ac.id/'
st.subheader('Referensi terkait Rekomedasi Tugas Akhir yang diberikan dapat dilihat di')

if st.button('Klik Disini'):
    wb.open_new_tab(url)










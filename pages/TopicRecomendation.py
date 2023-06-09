import streamlit as st
import pandas as pd
import webbrowser as wb
from sklearn.naive_bayes import GaussianNB
from PIL import Image

st.header('Referensi Judul Rekomedasi Tugas Akhir')

dataea=pd.read_csv('ea.csv')
databi=pd.read_csv('bi.csv')
dataerp=pd.read_csv('erp.csv')
datasig=pd.read_csv('sig.csv')


st.subheader('Business Intelligence')
databi
st.subheader('Sistem Informasi Geografis')
datasig
st.subheader('Enterprise Architecture')
dataea
st.subheader('Enterprise Resource Planning')
dataerp

#referensi
url = 'http://scholar.unand.ac.id/'
st.subheader('Referensi terkait Rekomedasi Tugas Akhir lainnya dapat dilihat di')

if st.button('Klik Disini'):
    wb.open_new_tab(url)
    

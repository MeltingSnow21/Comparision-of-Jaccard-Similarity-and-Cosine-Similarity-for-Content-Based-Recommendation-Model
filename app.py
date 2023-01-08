# import library yang dibutuhkan 

from pathlib import Path
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit as st 
from time import sleep
from streamlit_option_menu import option_menu
import nltk
nltk.download('wordnet')
nltk.download('stopwords')

import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('stopwords')
from sklearn.feature_extraction import text


from openpyxl import load_workbook #library untuk menampilkan dokumen
import pandas as pd #import pandas 
from nltk.tokenize import word_tokenize #import library nltk - tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #import library sastrawi untuk

import re




# membaca hasil akhir dan data evaluasi
df_rekomendasi = pd.read_csv('hasilakhir.csv', delimiter=',')
df_rekomendasi.head()
indices = pd.Series(df_rekomendasi.index, index=df_rekomendasi['Judul']).drop_duplicates()

def Validator(x):
    if x in indices:
        return True
    else:
        return False

def Rekomen_Cos (title) :
    if title in indices:    
        x = df_rekomendasi[df_rekomendasi['Judul'] == title]['Cossine Rekomend'].values[0]
        x = re.findall(r'\d+', x)
        x = res = [eval(i) for i in x]
        df2=df_rekomendasi[df_rekomendasi.index.isin(x)]
        y = df2['Judul']
        return y
    else : return ("Tidak ada  berita seperti itu")
    
def Rekomen_Jac (title) :
    if title in indices:    
        x = df_rekomendasi[df_rekomendasi['Judul'] == title]['Jaccard Recommned'].values[0]
        x = re.findall(r'\d+', x)
        x = res = [eval(i) for i in x]
        df2=df_rekomendasi[df_rekomendasi.index.isin(x)]
        y = df2['Judul']
        return y
    else : return ("Tidak ada  berita seperti itu")


  
# aset animasi
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_bpqri9y8.json")
lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_r71cen62.json")


#setup halaman
st.set_page_config(layout="wide", page_icon=":turtle:", page_title="Yukibara", initial_sidebar_state="auto")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#setup sidebar
with st.sidebar : 
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Tentang Kami", "Rekomendasi", "Pembahasan"],
        
    )
    
# halaman tentang kami
if selected == "Tentang Kami" :

    #header
    st.subheader("Natural Language Processing - Kelompok 1")
    st.title("""Perbandingan Lematisasi dan Stemming menggunakan Bag of Words Pada Model Rekomendasi Film :turtle: """)
    st.write(
            "Projek ini diselesaikan menggunakan 1000 dataset film dari website IMDB yang diperoleh dari [Kaggle](https://www.kaggle.com/datasets). "
        )
    st.write("Segala bentuk dokumentasi pada pengerjaannya diunggah pada Github terlampir")


    st.write("##")
    st.info(":rocket: Kunjungi Github Pada [Tautan Berikut](https://github.com/MeltingSnow21/Comparision-of-Lematization-and-Stemming-in-Bahasa-for-Film-Recommndation-System--Based-By-Content)")
    with st.spinner('Wait for it...'):
        sleep(2)
    with st.container():
        st.write("---")
        st.header("Tentang Kelompok")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write(
                """
                Tugas besar ini diselesaikan oleh :\n
                    - Randi Baraku      (119140061)          
                    - Rifan Firmansyah  (111111111)     
                    - Michele Jireh     (111111111)         
                    - Kak Radha         (111111111)             
                    - Viranti           (111111111)               
                    - Shopia Nouriska   (111111111)       
                    - Rian A Waskito    (119140030)    
                    - Putu AK Yudha     (119140098) 
                    - Samuel J Pardede  (11914010)  
                """
            )
           
        with right_column:
            st_lottie(lottie_coding2, height=300, key="coding")


#halaman pembahasan
if selected == "Pembahasan" :

    #header
    st.subheader("Berikut ini merupakan hasil dari penelitian yang kami lakukan")
    st.title("""Perbandingan Metode Teks Pre-Processing menggunakan Stemming dan Lematisasi:turtle: """)
    st.write("---")
    st.write("##")
    st.subheader("Hasil")
    st.write("Menggunakan metode Mean Absolute Error (MAE), Berikut ini merupakan hasil dari evaluasi 50 data film yang digunakan")
    
    y2 = df_rekomendasi[['MAE_Cos','MAE_Jac']].copy()

    with st.spinner('Wait for it...'):
        sleep(2)
    

    #grafik satu
    st.line_chart(y2)
    st.write("Dari visualisasi di atas tampak bahwa hasil yang diberikan oleh metode Lematisasi dan metode Stemming hampir sama, namun pada beberapa nomor sampel nilai MAE yang diberikan berbeda")

    st.write("---")

    #grafik dua
    st.write("Untuk lebih jelasnya, kita dapat melihat perbantingan hasil dari kedua pengujian tersebut sebagai berikut")
    st.bar_chart(y2)
    
    st.write("---")
    st.write("##")
    st.subheader("Hasil")
    st.write("Sample No 10, 32, dan 36 memberikan hasil yang berbeda, berikut ini adalah hasil dari pengujian tersebut")

    #grafik perbandingan
    yx = y2.loc[[10,32,36]]
    a , b = st.columns(2)
    with  a  :
        st.write("Hasil Stemming sampel")
        st.bar_chart(yx['MAE_Cos'])
    with  b  :
        st.write("Hasil Lematisasi sampel")
        st.bar_chart(yx['MAE_Jac'])
    st.write("""Perbedaan dari ketiga sampel diatas ke tiga-tiganya memberikan hasil bahwa nilai error yang diberikan oleh Hasil Stemming lebih kecil dari Hasil Lematisasi""")

    #Hasil akhir
    st.write("---")
    st.subheader("Hasil Akhir")
    st.write("Nilai rata-rata MAE dari kedua metode tersebut adalah sebagai berikut")
    x = y2['MAE_Cos'].mean()
    st.info (f"MAE Lematisasi : {x}")    
    x = y2['MAE_Jac'].mean()
    st.info (f"MAE Stemming : {x}")
    
    #Kesimpulan
    st.write("---")
    st.subheader("Kesimpulan")
    
    st.write("""Dengan menggunakan 50 data pengujian, diperoleh perbedaan antara hasil MAE Lematisasi dan MAE Stemming
             sebesar 0.2, Dengan nilai MAE Lematisasi lebih besar ketimbang MAE Stemming. Perbedaan ini
             menyimpulkan bahwa menggunakan metode Bag of Word, hasil dari Stemming memberikan hasil yang lebih baik
             ketimbang Lematisasi.
             """)

    st.subheader("Saran")
    st.write(""""Hasil dari penelitian sangat bergantung dari dataset yang digunakan, untuk memperoleh selisih yang lebih besar
             dan signifikan, disarankan menggunakan volume data yang lebih besar dalam evaluasi.""")
        
#halaman rekomendasi
elif  selected == "Rekomendasi" :

    # header
    st.subheader("Model rekoemendasi film")
    st.title("""Rekomendasi Film Menggunakan Stemming dan Lematisasi :turtle: """)
    st.write(
            "Masukan judul film yang ingin direkomendasikan : "
        )
    title = st.text_input('Input Judul film', 'Life of Brian')
    st.write('Film yang ingin direkomendasikan saat ini adalah', title)

    #tombol
    Tombol = st.button("Rekomendasikan")
    if Tombol :
        
        A = Validator(title)
        with st.spinner('Wait for it...'):
            sleep(2)
        if A : 
            with st.container():
                st.write("---")
                left_column, right_column = st.columns(2)
                with left_column:
                    st.subheader("Rekomendasi Berdasarkan Cosine Similarity")
                    st.write("##")
                    A = Rekomen_Cos(title)
                    st.write(A)
                    
                with right_column:
                    st.subheader("Rekomendasi Berdasarkan Jaccard Similarity")
                    st.write("##")
                    A = Rekomen_Jac(title)
                    st.write(A)
        
        else :
            with st.container():
                st.write("---")
                left_column, right_column = st.columns(2)
                with left_column:
                    st.header("Film tidak ditemukan")
                    st.write("##")
                    st.write(
                        """
                        Sangat disayangkan karena keterbatasan database, film yang anda cari tidak ditemukan.
                        Berikut kami rekomendasikan judul film yang dapat anda cari untuk melihat perbandingan antara lematisasi dan stemming.
                        Anda dapat mencari:
            
                        - The Lord of the Rings: The Fellowship of the Ring
                        - Avengers: Endgame
                        - Rear Window

                        """
                    )
                with right_column:
                    st_lottie(lottie_coding, height=300, key="coding")
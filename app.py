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

global x1,x2,x3



# membaca hasil akhir dan data evaluasi
df_rekomendasi = pd.read_csv('hasilakhir.csv', delimiter=',')
df_rekomendasi.head()
indices = pd.Series(df_rekomendasi.index, index=df_rekomendasi['Judul']).drop_duplicates()

def Validator(x):
    if x in indices:
        return True
    else:
        return False

def Hasil_aktual (title, A) :
    if title in indices:    
        x = df_rekomendasi[df_rekomendasi['Judul'] == title]['Aktual'].values[0]
        y1 = df_rekomendasi[df_rekomendasi['Judul'] == title]['MAE_Cos'].values[0]
        y2 = df_rekomendasi[df_rekomendasi['Judul'] == title]['MAE_Jac'].values[0]
        y3 = df_rekomendasi[df_rekomendasi['Judul'] == title]['MAE_Cos2'].values[0]
        y4 = df_rekomendasi[df_rekomendasi['Judul'] == title]['MAE_Jac2'].values[0]
        
        
        x = re.findall(r'\d+', x)
        x = res = [eval(i) for i in x]
        if A :
            return x, y1, y2, y3, y4
        else :
            df2=df_rekomendasi[df_rekomendasi.index.isin(x)]
            y = df2['Judul']
            return y
    else : return ("Tidak ada  berita seperti itu")
    
def Rekomen_Cos (title, A) :
    if title in indices:    
        x = df_rekomendasi[df_rekomendasi['Judul'] == title]['Cossine Rekomend'].values[0]
        x = re.findall(r'\d+', x)
        x = res = [eval(i) for i in x]
        
        if A :
            return x
        
        else : 
            df2=df_rekomendasi[df_rekomendasi.index.isin(x)]
            y = df2['Judul']
            return y
    else : return ("Tidak ada  berita seperti itu")
    
def Rekomen_Jac (title, A) :
    if title in indices:    
        x = df_rekomendasi[df_rekomendasi['Judul'] == title]['Jaccard Recommned'].values[0]
        x = re.findall(r'\d+', x)
        x = res = [eval(i) for i in x]
        if A :
            return x
       
        else :
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

lottie_coding3 = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_pkibk91l.json")
lottie_coding2 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tfb3estd.json")
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
    st.subheader("Projek Tugas Akhir")
    st.title("""Perbandingan Metode jaccard Similarity dengan Cosine Similarity dengan TF-IDF untuk Model Rekomendasi Berita :turtle: """)
    st.write(
            "Projek ini diselesaikan menggunakan 50 berita yang diperoleh dari PT Radar Lampung Onine [berikut](https://docs.google.com/spreadsheets/d/1PFN00mO25bN1xK_kHNO3XQYLNtRepg2GeX3wQPf55MI/edit#gid=436355456). "
        )
    st.write("Segala bentuk dokumentasi pada pengerjaannya diunggah pada Github terlampir")


    st.write("##")
    st.info(":rocket: Kunjungi Github Pada [Tautan Berikut](https://github.com/MeltingSnow21/Comparision-of-Jaccard-Similarity-and-Cosine-Similarity-for-Content-Based-Recommendation-Model)")
    with st.spinner('Wait for it...'):
        sleep(1)
    with st.container():
        st.write("---")
        st.header("Tentang Penulis")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write(
                """
                Diajukan sebagai syarat menyelesaikan jenjang strata Satu (S-1) di Program Studi
                Teknik Informatika, Jurusan Teknologi, Produksi dan Industri,
                Institut Teknologi Sumatera
                
                Oleh
                
               - Nama          : randi baraku
               - NIM           : 119140061
               - Program Studi : Teknik Informatika
               - Angkatan      : 2019           
                """
            )
           
        with right_column:
            st_lottie(lottie_coding2, height=300, key="coding")
    
    with st.container():
        st.write("---")
        st.header("Tentang Projek")

        left_column, right_column = st.columns(2)
        with left_column : st_lottie(lottie_coding3, height=300, key="coding2")
        
        with right_column : 
            st.write(
                
                """
                Website ini diselesiakan untuk membantu dalam memvisualisasikan hasi dari tugas akhir.
                Batasan dari website ini yaitu; hanya dapat menampilkan judul dari hasil rekomendasi,
                memberikan visualisasi berupa grafik perbandingan antara kedua hasil,
                serta memberikan pembahasan singkat beserta kesimpuland dari projek yang diselesaikan.
                
                website ini tidak dapat mengakomodir pencarian untuk topik maupun sepenggal key word, hanya dapat mencari
                judul secara keseluruhan untuk melihat perbandingan hasil kedua metode.
                
                
                """
                
                
            )          

#halaman pembahasan
if selected == "Pembahasan" :

    #header
    st.subheader("Berikut ini merupakan pembahasan dari hasil penelitian yang telah dilakukan")
    st.title("""Perbandingan Metode Cosine Similarity dengan TIF-IDF dan Jaccard Similarity :turtle: """)
    st.write("---")
    st.write("##")
    st.subheader("Hasil MAE")
    st.write("Menggunakan metode Mean Absolute Error (MAE), Berikut ini merupakan hasil dari evaluasi 50 berita yang digunakan")
    
    y2 = df_rekomendasi[['MAE_Cos','MAE_Jac']].copy()

    with st.spinner('Wait for it...'):
        sleep(2)
    

    #grafik satu
    st.line_chart(y2)
    st.write("Dari visualisasi di atas tampak bahwa hasil yang diberikan oleh metode Cosine dan metode Jaccard hampir sama, namun pada beberapa nomor sampel nilai MAE yang diberikan berbeda")

    st.write("Untuk lebih jelasnya, kita dapat melihat perbantingan hasil dari kedua pengujian tersebut sebagai berikut")
    st.bar_chart(y2)

    st.write("---")
    st.write("##")
    st.subheader("Hasil RMSE")
    st.write("Menggunakan metode Root Mean Square Error (RMSE), Berikut ini merupakan hasil dari evaluasi 50 data berita yang digunakan")
    
    y2 = df_rekomendasi[['MAE_Cos2','MAE_Jac2']].copy()

    with st.spinner('Wait for it...'):
        sleep(2)
    
    #grafik satu
    st.line_chart(y2)
    st.write("Dari visualisasi di atas tampak bahwa hasil yang diberikan oleh metode Cosine dan metode Jaccard hampir sama, namun pada beberapa nomor sampel nilai MAE yang diberikan berbeda")

    st.write("Untuk lebih jelasnya, kita dapat melihat perbantingan hasil dari kedua pengujian tersebut sebagai berikut")
    st.bar_chart(y2)


    st.write("---")

    st.write("##")
    st.subheader("Perbandingan Sampel")
    st.write("Sample No 2, 3, 9, 13, 25, 30, 31, 32, 33, 48, dan 49 memberikan hasil yang berbeda, berikut ini adalah hasil dari pengujian tersebut")


    #grafik perbandingan
    y2 = df_rekomendasi[['MAE_Cos','MAE_Jac']].copy()
    yx = y2.loc[[2, 3, 9, 13, 25, 30, 31, 32, 33, 48, 49]]
    a , b = st.columns(2)
    with  a  :
        st.write("Hasil Cosine sampel")
        st.bar_chart(yx['MAE_Cos'])
    with  b  :
        st.write("Hasil Jaccard sampel")
        st.bar_chart(yx['MAE_Jac'])
    st.write("""Perbedaan dari ketiga sampel diatas ke tiga-tiganya memberikan hasil bahwa nilai error yang diberikan oleh Hasil Stemming lebih kecil dari Hasil Lematisasi""")

    #Hasil akhir
    st.write("---")
    st.subheader("Hasil Akhir")
    st.write("Nilai rata-rata MAE dari kedua metode tersebut adalah sebagai berikut")
    y2 = df_rekomendasi[['MAE_Cos','MAE_Jac']].copy()
    x = y2['MAE_Cos'].mean()
    st.info (f"MAE Cosine : {x}")    
    x = y2['MAE_Jac'].mean()
    st.info (f"MAE jaccard : {x}")
    
    st.write("Nilai rata-rata RMSE dari kedua metode tersebut adalah sebagai berikut")
    y2 = df_rekomendasi[['MAE_Cos2','MAE_Jac2']].copy()
    x = y2['MAE_Cos2'].mean()
    st.info (f"RMSE Cosine : {x}")    
    x = y2['MAE_Jac2'].mean()
    st.info (f"RMSE Jaccard : {x}")
    
    #Kesimpulan
    st.write("---")
    st.subheader("Kesimpulan")
    
    st.write("""Dengan menggunakan 50 data pengujian, diperoleh perbedaan antara hasil MAE Cosine dan MAE jaccard
             sebesar 0.12, dan perbedaan antara hasil RMSE Lematisasi dan RMSE Stemming sebesar 0.6. Baik hasil MAE maupun RMSE keduanya 
             memberikan hasil bahwa nilai kesalahan Jaccard lebih tinggi dari Cosine.  Perbedaan ini menyimpulkan bahwa dengan menggunakan
             Content Base Recomendation, metode Cosine merupakan metode terbaik jika dibandingkan Jaccard untuk dataset
             berita deskriptif.
             """)

    st.subheader("Saran")
    st.write("""Hasil dari penelitian sangat bergantung dari dataset yang digunakan, untuk memperoleh selisih yang lebih besar
             dan signifikan, disarankan menggunakan volume data yang lebih besar dalam evaluasi.""")
        
#halaman rekomendasi
elif  selected == "Rekomendasi" :

    # header
    st.subheader("Model rekoemendasi Berita")
    st.title("""Perbandingan Metode Jaccard Similarity dengan Cosine Similarity dengan TF-IDF untuk Model Rekomendasi Berita :turtle: """)
    st.write(
            "Masukan judul berita yang ingin direkomendasikan : "
        )
    title = st.text_input('Input Judul Berita', 'Panggil Pejabat Polri Tanpa Ajudan, Begini Penjelasan Jokowi ke Awak Media')
    st.write('Film yang ingin direkomendasikan saat ini adalah', title)

    #tombol
    Tombol = st.button("Rekomendasikan")
    if Tombol :
        
        A = Validator(title)
        with st.spinner('Wait for it...'):
            sleep(1)
        if A : 
            with st.container():
                st.write("---")
                left_column, right_column = st.columns(2)
                with left_column:
                    st.subheader("Rekomendasi Berdasarkan Cosine Similarity")
                    st.write("##")
                    A = Rekomen_Cos(title, False)
                    st.write(A)
                    
                with right_column:
                    st.subheader("Rekomendasi Berdasarkan Jaccard Similarity")
                    st.write("##")
                    A = Rekomen_Jac(title, False)
                    st.write(A)
            with st.container():
                
                st.subheader ("Hasil Sebenarnya")
                A = Rekomen_Cos(title, False)
                st.write(A)
            with st.container():
                st.write("---")
                st.subheader("Perbandingan Hasil")

                x1 = Rekomen_Cos(title, True)
                x2 = Rekomen_Jac(title, True)
                x3, y1, y2, y3, y4 = Hasil_aktual(title, True)
                
                if isinstance(x1, list): 
                    x1.sort()

                if isinstance(x2, list):
                    x2.sort()
                
                if isinstance(x3, list):
                    x3.sort()
                
 
                chart_data = pd.DataFrame(
                    list(zip(x1, x2, x3)),
                    columns=["Cosine", "Jaccard", "Aktual"])
                st.area_chart(chart_data)             
            
            with st.container():
                st.write("---")
                st.subheader("Perbandingan Nilai Kesalahan")
                st.write("Nilai kesalahan dari Cosine divisualisasikan pada index 0 dan Jaccard pada index 1")
                a , b = st.columns(2)

                with  a  :
                    data = {'MAE': [y1, y2]}
                    st.write("Mae dari Kedua Metode")
                    st.bar_chart(data)
                    
                with  b  :
                    data = {'MAE Kuadrat': [y3, y4]}
                    st.write("Mae Kuadrat dari Kedua Metode")
                    st.bar_chart(data)
                        
                
                    

        else :
            with st.container():
                st.write("---")
                left_column, right_column = st.columns(2)
                with left_column:
                    st.header("Berita tidak ditemukan")
                    st.write("##")
                    st.write(
                        """
                        Sangat disayangkan karena keterbatasan database, berita yang anda cari tidak ditemukan.
                        kami juga tidak dapat mengakomodir sepenggal kata kunci karena 
                        hal tersebut di luar dari batasan penelitian.
                    
                        
                        """
                    )
                with right_column:
                    st_lottie(lottie_coding, height=300, key="coding")
                st.write(
                        """ 
                        Berikut kami rekomendasikan judul berita yang dapat anda cari untuk melihat perbandingan antara Cossine dan jaccard.
                        Anda dapat mencari:
            
                        - Pertumbuhan Angkatan Kerja dan Lowongan Kerja Tak Berimbang, Disnakertrans Mesuji Lirik Alumni SMA dan SMK
                        - UBL Riset Bersama Diskominfotiksan Pemkab Pesawaran
                        - Test Drive Hyundai Stargazer, Intip Kenyamanan dan Fitur Canggihnya!
                        """ )
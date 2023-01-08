

## SESI TA 1

import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import nltk
nltk.download('stopwords')
from sklearn.feature_extraction import text
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


from openpyxl import load_workbook #library untuk menampilkan dokumen
import pandas as pd #import pandas 
from nltk.tokenize import word_tokenize #import library nltk - tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #import library sastrawi untuk

import re

# membaca hasil akhir dan data evaluasi

df_rekomendasi = pd.read_csv('hasilakhir.csv', delimiter=',')
df_rekomendasi.head()
indices = pd.Series(df_rekomendasi.index, index=df_rekomendasi['Judul']).drop_duplicates()

def Rekomen_Cos (title) :
    if title in indices:
        x = df_rekomendasi[df_rekomendasi['Judul'] == title]['Cossine Rekomend'].values[0]
        x = re.findall(r'\d+', x)
        df2=df_rekomendasi[df_rekomendasi.index.isin(x)]
        x = df2['Judul']
        return x.tolist()
    else : return ("Tidak ada  berita seperti itu")

def Rekomen_Jac (title) :
    if title in indices:    
        y = df_rekomendasi[df_rekomendasi['Judul'] == title]['Jaccard Recommned'].values[0]
        y = re.findall(r'\d+', y)
        df2=df_rekomendasi[df_rekomendasi.index.isin(y)]
        y = df2['Judul']
        return y.tolist()
    else : return ("Tidak ada berita seperti itu")



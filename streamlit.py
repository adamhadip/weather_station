import streamlit as st
import pandas as pd
import joblib
import requests
# import psycopg2
col1, col2 = st.columns(2)
col2.error("""
Adam Hadi Pratama 
1101202001
Data Enthusiast
Universitas Telkom
""")
# POSTGRES_USER = "postgres"
# POSTGRES_PASSWORD = "adamdvimprez7"
# POSTGRES_SERVER = "localhost"
# POSTGRES_PORT = "5432"
# POSTGRES_DB = "weather_station"

# conn = psycopg2.connect(
#     host=POSTGRES_SERVER,
#     port=POSTGRES_PORT,
#     dbname=POSTGRES_DB,
#     user=POSTGRES_USER,
#     password=POSTGRES_PASSWORD
# )

st.title('Weather Station')
st.header('Mau prediksi cuaca hari ini?')
hujan = st.number_input('Masukin Derasnya Hujan:')
kelembabpan = st.number_input('Masukin kelembabpan:')
tekanan_udara = st.number_input('Masukin tekanan udara:')
temperature = st.number_input('Masukin temperature:')
tingkat_cahaya = st.number_input('Masukin tingkat cahaya:')


if st.button('Predict'):
    data = {
        'hujan': hujan, 
        'kelembabpan' : kelembabpan, 
        'tekanan_udara':tekanan_udara,
        'temperature':temperature,
        'tingkat_cahaya' : tingkat_cahaya
    }
    
    with st.spinner("Mengirim data ke server ..."):
        keterangan = requests.post('http://localhost:5000/predict/', json=data).json()
    
    
    st.header('Hasil Prediksi :')
    if keterangan == '[0]' :
        st.write('Cuaca Hari ini Cerah')
    elif keterangan <= '[1]': 
        st.write('Cuaca Hari ini gerimis')
    else: 
        st.write('Cuaca Hari ini Hujan Deras')
    # cun = conn.cursor()
    # sql = """INSERT INTO weather (hujan,kelembabpan,tekanan_udara,temperature,tingkat_cahaya,keterangan) VALUES (%s,%s,%s,%s,%s,%s)"""
    # cun.execute(sql,(hujan,kelembabpan,tekanan_udara,temperature,tingkat_cahaya,keterangan))
    # conn.commit()
    # cun.close()
import streamlit as st
import pandas as pd
import joblib


# load the pre-trained model and scaler
model = joblib.load('model.pkl')

def predict_weather(hujan, kelembabpan, tekanan_udara, temperature, tingkat_cahaya):
    # create a dataframe with the user input
    input_data = pd.DataFrame([[hujan, kelembabpan, tekanan_udara, temperature, tingkat_cahaya]], 
                              columns=['hujan','kelembabpan','tekanan_udara','temeprature','tingkat_cahaya'])
    # make predictions
    prediction = model.predict(input_data)
    return prediction[0]

st.title('Weather Station')
st.header('Mau prediksi cuaca hari ini?')
hujan = st.number_input('Masukin Derasnya Hujan:')
kelembabpan = st.number_input('Masukin kelembabpan:')
tekanan_udara = st.number_input('Masukin tekanan udara:')
temperature = st.number_input('Masukin temperature:')
tingkat_cahaya = st.number_input('Masukin tingkat cahaya:')

if st.button('Predict'):
    prediction = predict_weather(hujan, kelembabpan, tekanan_udara, temperature, tingkat_cahaya)
    if prediction == 0:
        st.write('Cuaca Cerah')
    elif prediction <= 1:
        st.write('Cuaca Gerimis')
    else: 
        st.write('Hujan Deras')

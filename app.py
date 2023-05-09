from fastapi import FastAPI, Body
from pydantic import BaseModel
import uvicorn
import pandas as pd
import joblib 
import yaml 
import psycopg2
import asyncpg

with open('/weather_station/config/config.yaml','r') as file:
    config = yaml.safe_load(file)

model = joblib.load('/weather_station/model.pkl')

POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "adamdvimprez7"
POSTGRES_SERVER = "localhost"
POSTGRES_PORT = "5432"
POSTGRES_DB = "wst"

conn = psycopg2.connect(
    host=POSTGRES_SERVER,
    port=POSTGRES_PORT,
    dbname=POSTGRES_DB,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)
class api_data(BaseModel):
    hujan : int
    kelembabpan : int
    tekanan_udara : float
    temperature : int
    tingkat_cahaya : int
    
app = FastAPI()

@app.get('/')
async def home():
    return 'Hello, Fast Api Berhasillll....'

@app.post('/predict/')
async def predict (data:api_data):
    try:
        print(data)
        data = pd.DataFrame(data).set_index(0).T.reset_index(drop=True)
        data.columns = config['predictors']
    
        y_pred = model.predict(data)
        print(y_pred)
        return str(y_pred) 
    except Exception as e:
        return 'Your data is not going anywhere'
if __name__ == '__main__':
    uvicorn.run("app:app", host= "localhost", port=5000,reload=True)

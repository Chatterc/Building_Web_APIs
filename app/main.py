from fastapi import FastAPI
from .score import predict_sentiment
from .models import request_body

app = FastAPI(
    title='Stockton DSSA - Data Gathering & Warehousing',
    description='Fall 2021 - Deploy Predictive Web Service'
    
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/predict')
def predict(data : request_body):
    y_pred = predict_sentiment(data.review)
    return y_pred
from fastapi import FastAPI
from app.score import predict_sentiment
from app.models import request_body


app = FastAPI(
    title='Stockton DSSA',
    description='Deploy Predictive Web Service',
    
)

@app.get("/")
def read_root():
    return {"Hello": "Stockton DSSA Students!"}


@app.post('/predict')
def predict(data : request_body):
    y_pred = predict_sentiment(data.review)
    return y_pred


# Remember to run we need to put uvicorn app.main:app --reload in the terminal since our main sits in our app directory
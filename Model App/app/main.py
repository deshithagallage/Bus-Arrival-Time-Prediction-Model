from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .schemas.predict import PredictionInput
from .crud.predict import predict_arrival_time

app = FastAPI()

origins = ['http://localhost:8000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "status": "Model Application is running smoothly",
        "api_version": "1.0.0",
        "message": "Welcome to the Bus Arrival Prediction Model API"
    }

@app.post("/predict")
def predict_time_to_arrival(input: PredictionInput):
    try:
        prediction = predict_arrival_time(input)
        return {"prediction": prediction}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
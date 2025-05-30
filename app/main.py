from fastapi import FastAPI
from app.schemas import GestureInput, GestureOutput
from app.predict import predict_gesture

app = FastAPI(title="Hand Gesture Classification API")

@app.post("/predict", response_model=GestureOutput)
def predict(input_data: GestureInput):
    return predict_gesture(input_data)

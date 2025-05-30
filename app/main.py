from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.responses import PlainTextResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from app.schemas import GestureInput, GestureOutput
from app.predict import predict_gesture

app = FastAPI(title="Hand Gesture Classification API")

@app.post("/predict", response_model=GestureOutput)
def predict(input_data: GestureInput):
    return predict_gesture(input_data)

from fastapi import Response

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
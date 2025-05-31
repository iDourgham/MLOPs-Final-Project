# from fastapi import FastAPI
# from fastapi.responses import Response
# from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
# from app.schemas import GestureInput, GestureOutput
# from app.predict import predict_gesture
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import Request

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from app.schemas import GestureInput, GestureOutput
from app.predict import predict_gesture

app = FastAPI(title="Hand Gesture Classification API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],  # your React frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.options("/predict")
# async def options_predict(request: Request):
#     return Response(status_code=200)

@app.post("/predict", response_model=GestureOutput)
def predict(input_data: GestureInput):
    return predict_gesture(input_data)

from fastapi import Response

@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
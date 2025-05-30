import numpy as np
import joblib
from app.schemas import GestureInput, GestureOutput
import os
from fastapi import HTTPException
from prometheus_client import Gauge
import time
from prometheus_client import Counter

request_counter = Counter("prediction_requests_total", "Total number of prediction requests")

# Prometheus metric
prediction_latency_gauge = Gauge("prediction_latency_seconds", "Time taken for model prediction")

# Load model and label encoder
model_path = os.path.join("model", "modelXGBoost.pkl")
encoder_path = os.path.join("model", "label_encoder.pkl")

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

custom_label_map = {
    "one": "left",
    "two_up": "up",
    "three": "down",
    "four": "right"
}

def predict_gesture(data: GestureInput) -> GestureOutput:
    request_counter.inc()
    start_time = time.time()  # ⏱️ Start

    landmarks = np.array(data.landmarks)
    if landmarks.shape[0] != 63:
        raise HTTPException(status_code=400, detail=f"Input landmarks length must be 63, got {landmarks.shape[0]}")
    landmarks = landmarks.reshape(1, -1)

    prediction = model.predict(landmarks)[0]
    decoded = label_encoder.inverse_transform([prediction])[0]
    mapped_label = custom_label_map.get(decoded, "unknown")

    #Export latency metric
    duration = time.time() - start_time
    prediction_latency_gauge.set(duration)  # Prometheus metric

    return GestureOutput(prediction=mapped_label)

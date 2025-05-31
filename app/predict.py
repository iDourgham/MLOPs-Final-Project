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

# def normalize_landmarks(landmarks):
#     landmarks = np.array(landmarks).reshape(21, 3)

#     x_wrist, y_wrist = landmarks[0][0], landmarks[0][1]
#     x_tip, y_tip = landmarks[8][0], landmarks[8][1]  # Index 8 → landmark 9

#     scale = np.sqrt((x_tip - x_wrist) ** 2 + (y_tip - y_wrist) ** 2)
#     if scale == 0:
#         return landmarks.flatten()  # Return as-is to avoid division by zero

#     # Normalize x and y, keep z unnormalized (or remove z if your model ignores it)
#     normalized = []
#     for x, y, z in landmarks:
#         norm_x = (x - x_wrist) / scale
#         norm_y = (y - y_wrist) / scale
#         normalized.extend([norm_x, norm_y])  # drop z, or include as-is if used

#     return np.array(normalized)

def normalize_landmarks(landmarks):
    landmarks = np.array(landmarks).reshape(21, 3)

    # Get wrist (landmark 1) and middle fingertip (landmark 9)
    x_wrist, y_wrist = landmarks[0][0], landmarks[0][1]
    x_tip, y_tip = landmarks[8][0], landmarks[8][1]  # landmark 9 is at index 8

    scale = np.sqrt((x_tip - x_wrist) ** 2 + (y_tip - y_wrist) ** 2)
    if scale == 0:
        return landmarks.flatten()  # Return original if scale is zero

    # Normalize x and y, keep z unchanged
    normalized = []
    for x, y, z in landmarks:
        norm_x = (x - x_wrist) / scale
        norm_y = (y - y_wrist) / scale
        normalized.extend([norm_x, norm_y, z])  # Keep original z

    return np.array(normalized)

def predict_gesture(data: GestureInput) -> GestureOutput:
    request_counter.inc()
    start_time = time.time()  # ⏱️ Start

    landmarks = np.array(data.landmarks)
    if landmarks.shape[0] != 63:
        raise HTTPException(status_code=400, detail=f"Input landmarks length must be 63, got {landmarks.shape[0]}")
    
    # Apply normalization
    landmarks = normalize_landmarks(landmarks)
    landmarks = landmarks.reshape(1, -1)

    prediction = model.predict(landmarks)[0]
    decoded = label_encoder.inverse_transform([prediction])[0]
    mapped_label = custom_label_map.get(decoded, "unknown")

    #Export latency metric
    duration = time.time() - start_time
    prediction_latency_gauge.set(duration)  # Prometheus metric

    return GestureOutput(prediction=mapped_label)

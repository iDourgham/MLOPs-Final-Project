import numpy as np
import joblib
from app.schemas import GestureInput, GestureOutput
import os

# Load model and label encoder
model_path = os.path.join("model", "modelXGBoost.pkl")
encoder_path = os.path.join("model", "label_encoder.pkl")

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

def predict_gesture(data: GestureInput) -> GestureOutput:
    landmarks = np.array(data.landmarks).reshape(1, -1)
    prediction = model.predict(landmarks)[0]
    decoded = label_encoder.inverse_transform([prediction])[0]
    return GestureOutput(prediction=decoded)

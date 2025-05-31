from fastapi import FastAPI
from app.schemas import GestureInput, PredictionOutput
from app.predict import predict_gesture

app = FastAPI(title="Hand Gesture Classifier", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Hand Gesture Classification API is up and running!"}

@app.post("/predict", response_model=PredictionOutput)
def classify_gesture(data: GestureInput):
    encoded_label, decoded_label = predict_gesture(data.features)
    return {
        "encoded_label": encoded_label,
        "predicted_label": decoded_label
    }


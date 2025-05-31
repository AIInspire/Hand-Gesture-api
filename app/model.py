import pickle
import requests
import os

MODEL_URL = "https://github.com/AIInspire/Hand-Gesture-Classification/raw/Research/artifacts/XGBoost_model.pkl"
ENCODER_URL = "https://github.com/AIInspire/Hand-Gesture-Classification/raw/Research/artifacts/label_encoder.pkl"

MODEL_PATH = "models/XGBoost_model.pkl"
ENCODER_PATH = "models/label_encoder.pkl"

os.makedirs("models", exist_ok=True)

def download_file(url, dest_path):
    if not os.path.exists(dest_path):
        r = requests.get(url)
        with open(dest_path, "wb") as f:
            f.write(r.content)

# Download and load the model & encoder
download_file(MODEL_URL, MODEL_PATH)
download_file(ENCODER_URL, ENCODER_PATH)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    label_encoder = pickle.load(f)
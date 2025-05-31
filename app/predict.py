import numpy as np
import pickle

MODEL_PATH = "models/XGBoost_model.pkl"
ENCODER_PATH = "models/label_encoder.pkl"

# Load model and encoder
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    encoder = pickle.load(f)

def normalize_landmarks(features: list[float]) -> list[float]:
    """
    Normalize the (x, y) coordinates by:
    - Translating so the wrist (landmark 1) is the origin.
    - Scaling by the midpoint (landmark 13).
    Z-coordinates are left untouched.
    """
    features = np.array(features)
    features = features.reshape(-1, 3)  # shape: (21, 3)

    x_wrist, y_wrist = features[0][0], features[0][1]    # landmark 1 (index 0)
    x_mid, y_mid = features[12][0], features[12][1]      # landmark 13 (index 12)

    for i in range(21):
        features[i][0] = (features[i][0] - x_wrist) / x_mid  # normalize x
        features[i][1] = (features[i][1] - y_wrist) / y_mid  # normalize y
        # features[i][2] remains unchanged (z)

    return features.flatten().tolist()

def predict_gesture(features: list) -> tuple[int, str]:
    normalized_features = normalize_landmarks(features)
    features_array = np.array(normalized_features).reshape(1, -1)
    prediction_encoded = model.predict(features_array)[0]
    prediction_label = encoder.inverse_transform([prediction_encoded])[0]
    return prediction_encoded, str(prediction_label)

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, Histogram, generate_latest
from app.schemas import GestureInput, PredictionOutput
from app.predict import predict_gesture
import time

app = FastAPI(title="Hand Gesture Classifier", version="1.0")

# -----------------------
# CORS Middleware Setup
# -----------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:8888"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Prometheus Metrics Setup
# -----------------------
REQUEST_COUNT = Counter(
    "request_count", "Total number of HTTP requests"
)
REQUEST_LATENCY = Histogram(
    "request_latency_seconds", "Latency (seconds) of HTTP requests"
)

# -----------------------
# Middleware to collect metrics
# -----------------------
@app.middleware("http")
async def track_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    REQUEST_COUNT.inc()
    REQUEST_LATENCY.observe(duration)
    return response

# -----------------------
# Routes
# -----------------------
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

# -----------------------
# Expose Prometheus metrics endpoint
# -----------------------
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

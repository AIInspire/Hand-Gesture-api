# Hand Gesture Classification API

This repository contains a FastAPI application for classifying hand gestures using a trained XGBoost model.

---

## Project Structure

```
Hand-Gesture-api/
├──.github\workflows
│   ├──docker-publish.yml
├── models/
│   ├── XGBoost_model.pkl
│   └── label_encoder.pkl
├── app/
│   ├── main.py
│   ├── model.py
│   ├── predict.py
│   └── schemas.py
├── tests/
│   └── test_predict.py
├── monitoring
│   ├── prometheus.yml
│   ├── README.md
├── Dashboard.png
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## API Endpoints

- **GET /**  
  Returns a welcome message indicating the API is running.

- **POST /predict**  
  Accepts JSON input of hand gesture features and returns predicted gesture labels.

- **GET /metrics**  
  Exposes Prometheus metrics for monitoring.

---

## Monitoring Metrics Explanation

We monitor three key metrics to ensure the reliability and performance of our Hand Gesture Classification API:

### 1. `data_records_received_total` (Data-related)

- **What it tracks**: Total number of data records received for prediction.
- **Why it matters**: Measures the volume of input data being processed, helping monitor load and usage patterns.

### 2. `model_prediction_total` (Model-related)

- **What it tracks**: Total number of predictions made by the model.
- **Why it matters**: Tracks how often the model is invoked, useful to understand inference workload and utilization.

### 3. `request_latency_seconds` (Server-related)

- **What it tracks**: Histogram of latency (response time) for HTTP requests in seconds.
- **Why it matters**: Helps monitor API responsiveness and detect any performance degradation.

---

## How Monitoring Works

- Metrics are collected using the **Prometheus Python client**.
- The `/metrics` endpoint exposes them in Prometheus-compatible format.
- **Prometheus** scrapes metrics from this endpoint periodically.
- **Grafana** is used to visualize the metrics via dashboards.

---

## Running Locally with Docker Compose

Make sure you have Docker and Docker Compose installed, then run:

```bash
docker-compose up --build
```

- API available at: [http://localhost:8000](http://localhost:8000)
- Prometheus UI: [http://localhost:9090](http://localhost:9090)
- Grafana UI: [http://localhost:3000](http://localhost:3000)

---

## Contact

For any issues or questions, feel free to open an issue on the repository.


# Monitoring Metrics Explanation

We monitor three key metrics to ensure the reliability and performance of our Hand Gesture Classification API:

## 1. `data_records_received_total` (Data-related)

- **What it tracks**: Total number of data records received for prediction.
- **Why it matters**: Measures the volume of input data being processed, helping monitor load and usage patterns.

## 2. `model_prediction_total` (Model-related)

- **What it tracks**: Total number of predictions made by the model.
- **Why it matters**: Tracks how often the model is invoked, useful to understand inference workload and utilization.

## 3. `request_latency_seconds` (Server-related)

- **What it tracks**: Histogram of latency (response time) for HTTP requests in seconds.
- **Why it matters**: Helps monitor API responsiveness and detect any performance degradation.

---

# How Monitoring Works

- Metrics are collected using the **Prometheus client library** integrated in the FastAPI application.
- Metrics are exposed at the `/metrics` endpoint in Prometheus format.
- A **Prometheus server** scrapes these metrics at a set interval.
- **Grafana** is used to visualize and create dashboards from the collected metrics.

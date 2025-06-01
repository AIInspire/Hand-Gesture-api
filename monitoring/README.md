
# Monitoring Metrics Explanation

The following metrics are collected to monitor the API’s performance and health:

## 1. Server-related metric: `request_count_total`
- Total number of HTTP requests received by the API.
- Tracks the overall usage and traffic of the service.

## 2. Server-related metric: `request_latency_seconds_bucket`
- Measures the distribution of request latencies in seconds.
- Helps identify performance bottlenecks and latency issues.

## 3. Server-related metric: `process_max_fds`
- Maximum number of file descriptors the process can open.
- Important for monitoring resource limits to prevent exhaustion.

## 4. Server-related metric: `process_resident_memory_bytes`
- Resident memory usage (RAM) by the process in bytes.
- Monitors memory consumption to detect leaks or high usage.

---

# How Monitoring Works

- Metrics are collected using the **Prometheus client library** integrated in the FastAPI application.
- Metrics are exposed at the `/metrics` endpoint in Prometheus format.
- A **Prometheus server** scrapes these metrics at a set interval.
- **Grafana** is used to visualize and create dashboards from the collected metrics.

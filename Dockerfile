# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt first for caching dependencies (if you have one)
# If you don't have requirements.txt, you can create it with `pip freeze > requirements.txt`
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole repo into the container
COPY . .

# Expose the port your app will run on (adjust if different)
EXPOSE 8000

# Command to run your app
# Assuming you use FastAPI or similar with uvicorn in main.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

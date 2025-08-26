# Use the official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn pytest httpx

# Copy the entire app directory structure
COPY app/ ./app/
COPY main.py .
COPY test_api.py .

# Expose port 80 for HTTP traffic
EXPOSE 80

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

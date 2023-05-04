# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /DevOps-Python-App

# Install required packages for building Python packages
RUN apt-get update && \
    apt-get install -y build-essential

# Copy the Python script and test files into the container
COPY add_numbers.py .
COPY test_add_numbers.py .

# Install project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Run the unit tests using Pytest
CMD ["pytest", "test_add_numbers.py"]
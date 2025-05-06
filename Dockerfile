# Use an official Python runtime as a parent image

# Update Python version to match your app requirements
FROM python:3.10-slim

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Make port 8051 available to the world outside this container
EXPOSE 8051

# Define environment variable
ENV NAME ENV

# Run happiness_comparator.py when the container launches
CMD ["python", "happiness_comparator.py"]
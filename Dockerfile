From python:3.9-slim

# Build-time arguments (can be passed during docker build)
ARG BUILD_ENV=production
ARG PYTHON_VERSION=3.9

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./src ./src
COPY ./Server ./Server
COPY config.py .

# Copy environment file
COPY .env* ./

Expose 8010
# Set PYTHONPATH to include the app directory
ENV PYTHONPATH=/app


CMD ["uvicorn", "Server.Main:app", "--host", "0.0.0.0", "--port", "8010", "--reload"]

# ---------------------------------------------------------
# Base Image
# ---------------------------------------------------------
FROM python:3.12-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# ---------------------------------------------------------
# Install system dependencies
# ---------------------------------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------
# Install uv
# ---------------------------------------------------------
RUN pip install --no-cache-dir uv

# ---------------------------------------------------------
# Copy dependency files first (Docker cache optimization)
# ---------------------------------------------------------
COPY pyproject.toml uv.lock ./

# Install Python dependencies
RUN uv sync --frozen --no-dev

# ---------------------------------------------------------
# Copy project
# ---------------------------------------------------------
COPY . .

# ---------------------------------------------------------
# Streamlit Configuration
# ---------------------------------------------------------
EXPOSE 8501

ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# ---------------------------------------------------------
# Start application
# ---------------------------------------------------------
CMD ["uv", "run", "streamlit", "run", "app.py"]
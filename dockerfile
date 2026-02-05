# Stage 1
FROM python:3.14.3-slim AS builder

# Install compilers needed for DuckDB
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY requirements.txt .

# Create wheels for all dependencies
RUN pip wheel --no-cache-dir --wheel-dir /build/wheels -r requirements.txt


# Stage 2
FROM python:3.14.3-slim

WORKDIR /app

# Copy only the compiled wheels from the builder stage
COPY --from=builder /build/wheels /wheels
COPY requirements.txt .

# Install the pre-compiled wheels
RUN pip install --no-index --find-links=/wheels -r requirements.txt \
    && rm -rf /wheels

COPY ./src .

CMD [ "python3", "./src/01_bronze/test.py" ]
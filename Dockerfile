# Stage 1: Build stage
FROM python:3.13-slim AS builder

# Install Poetry
RUN pip install --no-cache-dir poetry==1.8.5

# Set the working directory
WORKDIR /code

# Copy Poetry files
COPY pyproject.toml poetry.lock ./

# install dependencies globally
RUN poetry config virtualenvs.create false

# Install dependencies (without dev dependencies)
RUN poetry install --without dev

# Copy the application code
COPY ./app ./app

# # Stage 2: Runtime stage
FROM python:3.13-slim

# # Set the working directory
WORKDIR /code

# # Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY ./app ./app

# Expose the port that FastAPI will use
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
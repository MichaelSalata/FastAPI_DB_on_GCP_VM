# Use BuildKit syntax
# syntax=docker/dockerfile:1.3
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim


COPY requirements.txt .
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --prefer-binary -r requirements.txt


# WORKDIR /app

# Copy the backend directory into the container
# COPY . /app

# Expose the application port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}", "--reload"]
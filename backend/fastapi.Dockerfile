# Use BuildKit syntax
# syntax=docker/dockerfile:1.3
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

COPY requirements.txt .
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --prefer-binary -r requirements.txt

CMD uvicorn app.main:app --port=${PORT:-8000} --host=0.0.0.0
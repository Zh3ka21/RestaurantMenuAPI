#!/bin/sh

echo "Waiting for PostgreSQL..."

# Wait for PostgreSQL to start
while ! nc -z db 5432; do
  sleep 1
done

echo "PostgreSQL started"

# Start the FastAPI app with Uvicorn
# Ensure to use the correct import path for your FastAPI app (replace 'app.main:app' accordingly)
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

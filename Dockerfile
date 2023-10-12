# This Dockerfile creates a Docker image for the Python application

# Load base image
FROM python:3.10

# Expose application port
EXPOSE 8000

# Environment variable to keep Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Environment variable to turn off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Add a work directory
WORKDIR /app

# Copy all files to the work directory
COPY . /app

# Update the package lists for upgrades for packages that need upgrading, as well as new packages that have just come to the repositories
# Then install Python dependencies
RUN apt-get update -y && python -m pip install --upgrade pip && pip install -r requirements.txt

# Create a non-root user with an explicit UID and add permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

# Switch to the new user
USER appuser

# Command to run the application using Gunicorn as a WSGI HTTP Server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
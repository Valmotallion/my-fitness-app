# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy dependencies first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Flask environment variables
ENV FLASK_APP=__init__
ENV PORT=5000
EXPOSE 5000

# Gunicorn points to the module inside the folder
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "myapp.app:app"]

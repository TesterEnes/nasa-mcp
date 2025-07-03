FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Set environment variable for NASA API key (can be overridden)
ENV NASA_API_KEY=DEMO_KEY

CMD ["python", "server.py"]
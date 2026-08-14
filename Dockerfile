FROM python:3.11-slim

WORKDIR /workspace
COPY . .

CMD ["python", "app/app.py"]

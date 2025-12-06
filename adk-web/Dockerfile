FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl git && apt-get clean
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir google-adk
RUN pip install --no-cache-dir litellm python-dotenv
RUN pip install --no-cache-dir -r requirements.txt || true

COPY adk-web/ ./adk-web/

ENV OLLAMA_API_BASE="http://ollama:11434"

EXPOSE 3000

CMD ["adk", "web", "--host", "0.0.0.0", "--port", "3000"]

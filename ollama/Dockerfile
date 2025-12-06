FROM ollama/ollama:latest

RUN apt-get update && apt-get install -y curl && apt-get clean

WORKDIR /app

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 11434

ENV MODEL_NAME="llama3.2:latest"

ENTRYPOINT ["/bin/bash", "/start.sh"]

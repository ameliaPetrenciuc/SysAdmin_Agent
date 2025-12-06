#!/bin/bash
set -e

echo "Starting Ollama server..."
ollama serve &
OLLAMA_PID=$!

echo "Waiting for Ollama API to become available..."
until curl -s http://localhost:11434/api/version > /dev/null; do
  echo "Ollama not ready, retrying..."
  sleep 2
done

echo "Ollama ready! Pulling model: $MODEL_NAME"
if ! ollama pull "$MODEL_NAME"; then
  echo "Failed to pull model $MODEL_NAME"
  exit 1
fi

echo "Model $MODEL_NAME pulled successfully. Ollama running."
wait $OLLAMA_PID

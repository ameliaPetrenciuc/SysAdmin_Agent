FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt ./requirements.txt
COPY mcp-server/ ./server_mcp/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8002

CMD ["python", "mcp-server/server_mcp.py"]
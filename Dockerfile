FROM python:3.12-slim

# install node
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend/package.json ./frontend/package.json
RUN npm --prefix frontend install
COPY frontend ./frontend
RUN npm --prefix frontend run build

EXPOSE 8000 3000

CMD uvicorn backend.main:app --host 0.0.0.0 --port 8000 & npm --prefix frontend start

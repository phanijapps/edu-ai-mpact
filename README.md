# edu-ai-mpact

This project provides a minimal FastAPI backend and a Next.js frontend. The backend calls OpenRouter models through the OpenAI client.

## Requirements
- Python 3.12
- Node.js 18+

## Setup
Install Python and Node dependencies:

```bash
python3.12 -m pip install -r requirements.txt
npm --prefix frontend install
```

Create an environment variable `OPENROUTER_API_KEY` with your API key.

## Running locally
Start the backend:

```bash
uvicorn backend.main:app --reload
```

In another terminal start the frontend:

```bash
npm --prefix frontend run dev
```

The site will be available at `http://localhost:3000`.

## Docker
A single Dockerfile builds and runs both services:

```bash
docker build -t edu-ai-mpact .
docker run -p 3000:3000 -p 8000:8000 -e OPENROUTER_API_KEY=sk-... edu-ai-mpact
```

## Testing
Run tests using `pytest`:

```bash
python3.12 -m pytest
```

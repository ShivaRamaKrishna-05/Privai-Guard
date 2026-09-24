# PrivAI Guard

AI-powered privacy gateway for LLM applications.

## Flow
User prompt → PII detection → contextual/risk analysis → policy → anonymize/mask/block → safe prompt → LLM → response scan → safe response.

## Run with Docker
docker compose up --build

Frontend: http://localhost:5173
Backend: http://localhost:8000
Swagger: http://localhost:8000/docs

## Local backend
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload

## Register
POST /api/v1/auth/register
{
  "email": "student@example.com",
  "password": "StrongPassword123!"
}

## Default LLM
LLM_PROVIDER=mock requires no external API key. An optional LangChain/OpenAI provider can be enabled through environment variables.

## Transformer
TRANSFORMER_ENABLED=false by default so the system can start without downloading a model. Enable it when needed.

## Important
Use synthetic test data only. Never commit .env or real secrets. This project is an educational final-year project foundation and requires additional hardening before production use.

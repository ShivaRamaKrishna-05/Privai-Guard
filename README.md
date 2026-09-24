ShivaRamaKrishna-05
Privai-Guard
Public
Go to file
t
T
author
Your Name
Initial commit: PrivAI Guard
1732c85
 · 
13 minutes ago
Name		
backend
Initial commit: PrivAI Guard
13 minutes ago
docs
Initial commit: PrivAI Guard
13 minutes ago
frontend
Initial commit: PrivAI Guard
13 minutes ago
.gitignore
Initial commit: PrivAI Guard
13 minutes ago
README.md
Initial commit: PrivAI Guard
13 minutes ago
docker-compose.yml
Initial commit: PrivAI Guard
13 minutes ago
Repository files navigation
README
Security
PrivAI Guard
AI-powered privacy gateway for LLM applications.

Flow
User prompt → PII detection → contextual/risk analysis → policy → anonymize/mask/block → safe prompt → LLM → response scan → safe response.

Run with Docker
docker compose up --build

Frontend: http://localhost:5173 Backend: http://localhost:8000 Swagger: http://localhost:8000/docs

Local backend
cd backend python -m venv .venv .venv\Scripts\activate pip install -r requirements.txt copy .env.example .env uvicorn app.main:app --reload

Register
POST /api/v1/auth/register { "email": "student@example.com", "password": "StrongPassword123!" }

Default LLM
LLM_PROVIDER=mock requires no external API key. An optional LangChain/OpenAI provider can be enabled through environment variables.

Transformer
TRANSFORMER_ENABLED=false by default so the system can start without downloading a model. Enable it when needed.

Important
Use synthetic test data only. Never commit .env or real secrets. This project is an educational final-year project foundation and requires additional hardening before production use.

About

AI Security Gateway for detecting, scoring, and sanitizing sensitive information in LLM prompts

Resources
Readme
Security policy
Security policy
Activity
Stars
0 stars
Watchers
0 watching
Forks
0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
Python
78.3%
JavaScript
19.8%
Dockerfile
1.1%
HTML
0.8%
Suggested workflows
Based on your tech stack

Python package logo
Python package
Create and test a Python package on multiple Python versions.
By GitHub Actions
Publish Python Package logo
Publish Python Package
Publish a Python Package to PyPI on release.
By GitHub Actions
Pylint logo
Pylint
Lint a Python application with pylint.
By GitHub Actions
More workflows
Footer
© 2026 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Community
Docs
Contact
Manage cookies
Do not share my personal information

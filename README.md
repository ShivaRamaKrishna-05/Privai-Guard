# PrivAI Guard

### AI Security Gateway for Privacy-Preserving LLM Applications

PrivAI Guard is an AI security and privacy gateway designed to protect sensitive information before it reaches a Large Language Model (LLM).

It detects Personally Identifiable Information (PII), evaluates privacy risk, applies configurable security policies, sanitizes prompts through anonymization or masking, blocks high-risk requests, and scans LLM responses for sensitive information.

---

## Overview

When users interact with LLM applications, prompts may unintentionally contain sensitive information such as:

* Email addresses
* Phone numbers
* IP addresses
* Physical addresses
* Government IDs
* Account numbers
* Financial information
* Credentials
* Personal names and organizations

PrivAI Guard acts as an intermediate security layer between the user and the LLM.

### Security Pipeline

```text
User Prompt
     │
     ▼
PII Detection
     │
     ▼
Risk & Context Analysis
     │
     ▼
Policy Evaluation
     │
     ├── BLOCK ──────────────► Request Rejected
     │
     ├── MASK / ANONYMIZE
     │          │
     │          ▼
     │     Sanitized Prompt
     │          │
     │          ▼
     │         LLM
     │          │
     │          ▼
     │    Response Scanner
     │          │
     │          ▼
     │     Safe Response
     │
     └── ALLOW ──────────────► LLM
```

---

## Key Features

### 🔍 PII Detection

Detects sensitive entities in user prompts, including:

* `PERSON`
* `ORG`
* `GPE`
* `LOC`
* `EMAIL`
* `PHONE`
* `IP_ADDRESS`
* `URL`
* `ADDRESS`
* `CREDIT_CARD`
* `FINANCIAL`
* `GOVERNMENT_ID`
* `ACCOUNT_NUMBER`
* `CREDENTIAL`

### 🛡️ Risk Assessment

Each detected entity contributes to a privacy risk assessment.

The gateway categorizes requests into risk levels such as:

```text
LOW
MEDIUM
HIGH
```

### 🔐 Policy-Based Protection

Different entity types can be assigned different actions:

| Entity        | Example Action |
| ------------- | -------------- |
| EMAIL         | ANONYMIZE      |
| PHONE         | MASK           |
| IP_ADDRESS    | MASK           |
| ADDRESS       | ANONYMIZE      |
| CREDIT_CARD   | BLOCK          |
| FINANCIAL     | BLOCK          |
| GOVERNMENT_ID | BLOCK          |
| CREDENTIAL    | BLOCK          |
| URL           | ALLOW          |

This policy-driven approach allows the gateway to be adapted to different privacy requirements.

### ✨ Prompt Sanitization

Sensitive information can be transformed before reaching the LLM.

Example:

```text
Original:
Contact me at john@example.com regarding my account.

Sanitized:
Contact me at [EMAIL_1] regarding my account.
```

### 🤖 LLM Gateway

PrivAI Guard supports a mock LLM mode for development and testing and can be configured for an external LLM provider through environment variables.

### 🔎 Response Scanning

The gateway also analyzes the generated LLM response for sensitive information before returning it to the user.

### 🔑 Authentication

The backend provides authentication endpoints for registering and logging into the application.

### ⚙️ Configurable Security

Security behavior can be configured through environment variables and policy settings, including:

* LLM provider
* Model configuration
* Transformer detection
* Detection threshold
* Maximum input length
* Rate limits
* Privacy policies

---

## Architecture

```text
                    ┌─────────────────────┐
                    │     Web Client      │
                    │      Frontend       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI Backend  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
       │ PII Detector│  │ Risk Engine │  │Policy Engine│
       └──────┬──────┘  └──────┬──────┘  └──────┬──────┘
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Prompt Sanitization │
                    │ Mask / Anonymize /  │
                    │       Block         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     LLM Gateway     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Response Detection  │
                    └──────────┬──────────┘
                               │
                               ▼
                         Safe Response
```

---

## Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn
* MongoDB
* Motor
* JWT Authentication
* spaCy
* Hugging Face Transformers
* PyTorch
* LangChain

### Frontend

* React
* Vite
* JavaScript
* HTML5
* CSS3

### Infrastructure

* Docker
* Docker Compose
* Git
* GitHub

---

## Project Structure

```text
Privai-Guard/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── detectors/
│   │   ├── llm/
│   │   ├── privacy/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── docs/
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

* Python 3.11+
* Node.js
* npm
* Docker Desktop (optional)
* MongoDB

---

## Run with Docker

Clone the repository:

```bash
git clone https://github.com/ShivaRamaKrishna-05/Privai-Guard.git
cd Privai-Guard
```

Start the application:

```bash
docker compose up --build
```

The application will be available at:

```text
Frontend:  http://localhost:5173
Backend:   http://localhost:8000
Swagger:   http://localhost:8000/docs
```

---

## Run Backend Locally

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```powershell
copy .env.example .env
```

Configure the required environment variables and start the server:

```bash
python -m uvicorn app.main:app --reload
```

Backend:

```text
http://localhost:8000
```

Swagger API documentation:

```text
http://localhost:8000/docs
```

---

## Run Frontend Locally

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## Authentication

### Register

```http
POST /api/v1/auth/register
```

Example request:

```json
{
  "email": "student@example.com",
  "password": "StrongPassword123!"
}
```

### Login

```http
POST /api/v1/auth/login
```

Authentication is required for protected privacy and chat operations.

---

## Privacy Analysis

PrivAI Guard exposes privacy-analysis functionality through the backend API.

A typical analysis performs:

```text
Input
  ↓
Entity Detection
  ↓
Risk Calculation
  ↓
Policy Lookup
  ↓
Action Selection
  ↓
Sanitization
```

Possible actions include:

```text
ALLOW
MASK
ANONYMIZE
BLOCK
```

---

## Example

### Input

```text
My name is John and my email is john@example.com.
Please contact me about my account.
```

### Detection

```text
PERSON → John
EMAIL  → john@example.com
```

### Policy

```text
PERSON → ANONYMIZE
EMAIL  → ANONYMIZE
```

### Sanitized Prompt

```text
My name is [PERSON_1] and my email is [EMAIL_1].
Please contact me about my account.
```

The sanitized prompt can then be forwarded to the configured LLM provider.

---

## Configuration

PrivAI Guard uses environment variables for application configuration.

Example:

```env
LLM_PROVIDER=mock
TRANSFORMER_ENABLED=false
```

The mock provider can be used for development without requiring an external LLM API key.

Do not commit your actual `.env` file.

---

## Security Considerations

PrivAI Guard is intended as an educational and development project demonstrating privacy protection for LLM applications.

For production deployment, additional security hardening should be performed, including:

* Secure secret management
* Strong authentication configuration
* HTTPS/TLS
* Production database security
* Rate-limit tuning
* Logging and monitoring
* Input validation
* Dependency security scanning
* Comprehensive security testing
* Secure deployment configuration

**Never use real personal information or production credentials for testing.**

Use synthetic test data instead.

---

## Current Scope

The project currently demonstrates:

* PII detection
* Privacy risk assessment
* Policy-based actions
* Prompt anonymization
* Prompt masking
* Request blocking
* LLM gateway integration
* Response scanning
* Authentication
* REST APIs
* Docker-based deployment

---

## Future Improvements

Potential future enhancements include:

* Advanced contextual PII detection
* More sophisticated risk scoring
* Additional LLM providers
* Improved response sanitization
* Policy management through the UI
* Audit logging
* Security analytics dashboard
* Role-based access control
* Automated security testing
* Production-ready deployment

---

## Disclaimer

This project is developed for educational and research purposes.

It demonstrates concepts related to privacy protection and security for LLM-based applications and should not be considered a complete production security solution without additional security review and hardening.

---

## Author

**Shiva Rama Krishna Konda**

Computer Science Engineering
Guru Nanak Institute of Technology, Hyderabad

GitHub: [ShivaRamaKrishna-05](https://github.com/ShivaRamaKrishna-05)

---

## License

This project is intended for educational and research purposes.

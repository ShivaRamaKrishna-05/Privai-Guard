# Architecture

Client → FastAPI → Authentication/RBAC → PII Detection (Regex/spaCy/Transformer) → Risk Engine → Policy Engine → Sanitizer → LLM Gateway → Response Scanner → User.

MongoDB stores privacy-preserving event metadata rather than raw prompt PII.

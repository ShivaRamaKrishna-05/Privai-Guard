# Security Design

Passwords use bcrypt. Access uses expiring JWTs. Admin routes require ADMIN role. Events contain categories/risk/action metadata and do not intentionally store raw prompt values. Secrets come from environment variables. Requests are sanitized before the LLM and responses are scanned before return.

This is an educational project, not a production privacy gateway. Production deployment requires stronger secret management, TLS, database authentication, robust rate limiting, dependency pinning, threat modeling and security testing.

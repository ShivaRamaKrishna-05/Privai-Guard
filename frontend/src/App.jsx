import React, { useState } from "react";
import { api } from "./services/api";

function Card({ title, value }) {
  return (
    <div className="card">
      <div className="muted">{title}</div>
      <div className="big">{value}</div>
    </div>
  );
}

export default function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [prompt, setPrompt] = useState(
    "My name is Rahul and my email is rahul@example.com."
  );

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  // Login
  async function login() {
    try {
      const data = await api("/auth/login", {
        method: "POST",
        body: JSON.stringify({ email, password }),
      });

      localStorage.setItem("token", data.access_token);
      setToken(data.access_token);
      setError("");
    } catch (e) {
      setError(e.message);
    }
  }

  // Analyze and sanitize prompt
  async function analyze() {
    try {
      const data = await api("/privacy/analyze", {
        method: "POST",
        body: JSON.stringify({ text: prompt }),
      });

      console.log("ANALYZE API RESPONSE:", JSON.stringify(data, null, 2));

      setResult(data);
      setError("");
    } catch (e) {
      setError(e.message);
    }
  }

  // Secure Chat
  async function chat() {
    try {
      const data = await api("/chat", {
        method: "POST",
        body: JSON.stringify({ prompt }),
      });

      console.log("CHAT API RESPONSE:", JSON.stringify(data, null, 2));

      setResult(data);
      setError("");
    } catch (e) {
      setError(e.message);
    }
  }

  // Logout
  function logout() {
    localStorage.removeItem("token");
    setToken(null);
    setResult(null);
    setError("");
  }

  // Login screen
  if (!token) {
    return (
      <main className="login">
        <div className="panel">
          <div className="brand">PrivAI Guard</div>

          <h1>Privacy Gateway</h1>

          <p className="muted">
            Secure prompts before they reach an LLM.
          </p>

          <input
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            placeholder="Password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button onClick={login}>Login</button>

          {error && <p className="error">{error}</p>}

          <p className="hint">
            Register first with POST /api/v1/auth/register.
          </p>
        </div>
      </main>
    );
  }

  // Dashboard
  return (
    <main>
      <header>
        <div className="brand">PrivAI Guard</div>

        <button className="secondary" onClick={logout}>
          Logout
        </button>
      </header>

      <section className="hero">
        <div>
          <div className="eyebrow">AI SECURITY GATEWAY</div>

          <h1>Privacy Simulator</h1>

          <p className="muted">
            Detect → score → sanitize → send → scan response.
          </p>
        </div>
      </section>

      {/* Result summary cards */}
      <section className="grid">
        <Card
          title="Risk Score"
          value={result?.risk_score ?? "—"}
        />

        <Card
          title="Risk Level"
          value={result?.risk_level ?? "—"}
        />

        <Card
          title="Action"
          value={result?.action ?? result?.response_action ?? "—"}
        />

        <Card
          title="Detections"
          value={
            result?.detections?.length ??
            result?.prompt_detections?.length ??
            result?.response_detections?.length ??
            0
          }
        />
      </section>

      {/* Prompt input */}
      <section className="panel">
        <h2>Prompt</h2>

        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <div className="actions">
          <button onClick={analyze}>
            Analyze &amp; Sanitize
          </button>

          <button onClick={chat}>
            Secure Chat
          </button>
        </div>

        {error && <p className="error">{error}</p>}
      </section>

      {/* Results */}
      {result && (
        <section className="grid-two">
          <div className="panel">
            <h2>Prompt Detection</h2>

            <pre>
              {JSON.stringify(
                result.detections ?? result.prompt_detections ?? [],
                null,
                2
              )}
            </pre>
          </div>

          <div className="panel">
            <h2>Sanitized Prompt</h2>

            <pre>
              {result.sanitized_text ??
                result.sanitized_prompt ??
                ""}
            </pre>
          </div>

          {result.response && (
            <div className="panel wide">
              <h2>LLM Response</h2>

              <pre>{result.response}</pre>

              <h3>Response Scan</h3>

              <pre>
                {JSON.stringify(
                  result.response_detections ?? [],
                  null,
                  2
                )}
              </pre>

              <h3>Response Action</h3>

              <p>{result.response_action ?? "—"}</p>
            </div>
          )}
        </section>
      )}
    </main>
  );
}
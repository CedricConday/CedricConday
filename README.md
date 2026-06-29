# Cedric Conday — AI Engineer

I build LLM-powered products and autonomous agent systems end to end, and I build *with* AI as the method — orchestrating multiple agents in parallel as a one-person engineering team. Self-taught into AI engineering in twelve months while caregiving full-time. Fintech and quantitative depth; US citizen, EN/DE.

📫 cedric@condaydigital.com · [LinkedIn](https://linkedin.com/in/cedricconday)

> **Building in public** — a new tool, fix, or feature most days. The commit graph is the résumé.

---

### Selected work

**[xe-mcp](https://github.com/CedricConday/xe-mcp)** — MCP server for the Xe Currency Data API.
FX tools — rate, conversion, volatility, optimal send-window, moving averages, correlation, charts — with a free ECB fallback, 49 unit tests, CI, and AWS Lambda handlers. TypeScript.

**[centrapay-mcp](https://github.com/CedricConday/centrapay-mcp)** — MCP server for Centrapay (NZ payments).
Nine tools modelled on the real Centrapay API — payment requests, settlement, idempotent refunds, merchants — with fetch-mock contract tests over every request. TypeScript.

**[TimeStitch](https://github.com/CedricConday/TimeStitch)** — temporal-context middleware for LLM and autonomous-agent sessions.
Injects standardized time/session context into every model call, with a six-model comparison. Python · MIT.

**[Protocol Tracker](https://github.com/CedricConday/protocol-tracker)** — cross-platform health app (iOS + Android).
React Native · TypeScript · Expo · SQLite. Multi-provider LLM **vision-OCR** (Anthropic / OpenAI / Groq) reads a photographed medical report and auto-fills structured data — BYO-API-key, with token & cost guardrails. Offline-first SQLite (versioned migrations), biometric auth, OS-keychain JWT sync, PDF reports, EN/DE, accessibility-oriented. Paired [web companion](https://github.com/CedricConday/protocol-tracker-web) — React/Vite/Express/Firebase with hardened Firestore rules and a server-side LLM proxy.

### Open-source contributions
Bug fixes to established projects — **litellm**, **Zettlr**, **GrowthBook**, django-scim2, krkn-ai, traceroot — each found, reproduced, fixed *with tests*, and sent upstream.

---

### Stack

**AI / LLM** — multi-provider APIs (Claude · OpenAI · Groq) · prompt & system-prompt design · multi-agent orchestration · LangChain · Model Context Protocol (self-authored multi-server stack) · RAG · vector DBs (Chroma) · vision-OCR · self-hosted open-weight models (Ollama)
**Languages** — Python · TypeScript · JavaScript · SQL · Rust · Bash
**Mobile / Web** — React Native · React 19 · Expo · SQLite · Firebase · Express · Vite · Tailwind
**Data / Quant** — pandas · NumPy · SciPy · scikit-learn · vectorbt · walk-forward backtesting · Monte-Carlo simulation
**Web3 / DeFi** — Solana (solders) · atomic transactions · Jupiter / DEX · on-chain decoding · EVM · EIP-712 / ed25519 / HMAC signing
**Infra** — Linux (Ubuntu / ARM) · Oracle Cloud · AWS (Lambda / SQS / DynamoDB / S3 / SES, SAM) · Docker · systemd · cron · Git · GitHub Actions · GDPR-aware engineering

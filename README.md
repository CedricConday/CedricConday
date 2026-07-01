# Cedric Conday — Software Engineer (AI / LLM · MCP)

I build LLM-powered products and agent systems end to end, and I build *with* AI as the method — orchestrating multiple agents in parallel as a one-person engineering team. Self-taught into software engineering in twelve months while caregiving full-time. Fintech and quantitative depth; TypeScript + Python. **Open to remote roles and relocation (incl. New Zealand).**

📫 cedric@condaydigital.com · [LinkedIn](https://linkedin.com/in/cedricconday)

> **Building in public** — a fix, tool, or feature most days. The commit graph is the résumé.

---

### Featured work

**[xe-mcp](https://github.com/CedricConday/xe-mcp)** — MCP server for the Xe Currency Data API *(TypeScript · 49 tests · CI · AWS Lambda)*
FX tools — rate, conversion, volatility, optimal send-window, correlation, charts — with a free ECB fallback so it runs with zero credentials.

**[centrapay-mcp](https://github.com/CedricConday/centrapay-mcp)** — MCP server for Centrapay, NZ payments *(TypeScript · npm · contract tests)*
Nine tools modelled on the real Centrapay API — payment requests, settlement, idempotent refunds, merchants — with fetch-mock contract tests over every request.

**[Protocol Tracker](https://github.com/CedricConday/protocol-tracker)** — cross-platform health app, iOS + Android *(React Native · Expo · TypeScript · SQLite)*
Multi-provider LLM **vision-OCR** (Anthropic / OpenAI / Groq) reads a photographed medical report and auto-fills structured data — BYO-key, with token & cost guardrails. Offline-first SQLite (versioned migrations), biometric auth, PDF reports, EN/DE, accessibility-oriented.

### Merged open-source contributions
Bugs found, reproduced, fixed *with a regression test*, and merged upstream into established projects:

- **[jaeger](https://github.com/jaegertracing/jaeger/pull/8902)** — MCP tooling reports `total_count` + truncation on `get_services` / `get_span_names` *(observability · MCP · CNCF)*
- **[mne-python](https://github.com/mne-tools/mne-python/pull/14002)** — eyetracking calibration files read as UTF-8 *(neuroimaging)*
- **[aeon](https://github.com/aeon-toolkit/aeon/pull/3585)** — `Padder` validates `fill_value`, rejects array-likes *(time-series ML)*
- **[schwifty](https://github.com/mdomke/schwifty/pull/292)** — correct ISO 7064 mod-97-10 checksum for BA *(IBAN / fintech)*
- **[js-joda](https://github.com/js-joda/js-joda/pull/804)** — `Instant.parse` accepts and resolves an offset *(date-time)*
- **[octokit/request.js](https://github.com/octokit/request.js/pull/820)** — handle primitive JSON error bodies without throwing *(GitHub SDK)*
- **[krkn-ai](https://github.com/krkn-chaos/krkn-ai/pull/382)** — include dependency in `CompositeScenario` identity *(chaos engineering)*

More fixes in review across DuckDB, OpenTelemetry, cargo-deny, faker, Zettlr, and Adyen.

---

### Stack
**AI / LLM** — multi-provider APIs (Claude · OpenAI · Groq) · prompt & system-prompt design · multi-agent orchestration · Model Context Protocol (self-authored servers) · RAG · vector DBs · vision-OCR · Ollama
**Languages** — TypeScript · Python · JavaScript · SQL · Rust · Bash
**Mobile / Web** — React Native · React 19 · Expo · SQLite · Firebase · Express · Vite
**Infra / Quality** — AWS (Lambda / SAM) · Docker · Linux · GitHub Actions · unit / contract / regression testing · observability (OpenTelemetry) · signed commits

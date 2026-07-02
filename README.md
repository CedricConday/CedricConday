# Cedric Conday — Software Engineer (AI / LLM · MCP)

I build LLM-powered products and agent systems end to end, and I build *with* AI as the method — orchestrating multiple agents in parallel as a one-person engineering team. Self-taught into software engineering in twelve months while caregiving full-time for a family member with multiple sclerosis — which is why a real thread of my work is **medical software**, alongside **fintech / payments** depth. TypeScript + Python. **Open to remote roles and relocation (incl. New Zealand).** *In Deutschland ansässig; Deutsch und Englisch, remote wie vor Ort.*

📫 cedric@condaydigital.com · [LinkedIn](https://linkedin.com/in/cedricconday)

> **Building in public** — a fix, tool, or feature most days. The commit graph is the résumé.

---

### Featured work

**[xe-mcp](https://github.com/CedricConday/xe-mcp)** — MCP server for the Xe Currency Data API *(TypeScript · 49 tests · CI · AWS Lambda)*
FX tools — rate, conversion, volatility, optimal send-window, correlation, charts — with a free ECB fallback so it runs with zero credentials.

**[centrapay-mcp](https://github.com/CedricConday/centrapay-mcp)** — MCP server for Centrapay, NZ payments *(TypeScript · npm · contract tests)*
Nine tools modelled on the real Centrapay API — payment requests, settlement, idempotent refunds, merchants — with fetch-mock contract tests over every request.

**[Protocol Tracker](https://github.com/CedricConday/protocol-tracker)** — cross-platform health app for a real MS treatment protocol, iOS + Android *(React Native · Expo · TypeScript · SQLite)*
Built for a family member's multiple-sclerosis care. Multi-provider LLM **vision-OCR** (Anthropic / OpenAI / Groq) reads a photographed medical report and auto-fills structured data — BYO-key, with token & cost guardrails. Offline-first SQLite (versioned migrations), biometric auth, PDF reports, EN/DE, accessibility-oriented.

**[nifti-qc](https://github.com/CedricConday/nifti-qc)** — quality-control for medical-imaging geometry *(Python)*
Catches silently-broken NIfTI qform/sform geometry before it corrupts a neuroimaging pipeline — the kind of quiet data bug that invalidates an MS-lesion analysis without ever raising an error.

### Open-source contributions
Bugs found, reproduced, fixed *with a regression test*, and merged upstream — **12 merged across 11 established projects**:

**Medical & neuro-imaging**
- **[mne-python](https://github.com/mne-tools/mne-python/pull/14002)** — eyetracking calibration files read as UTF-8 *(neuroimaging)*
- *In review:* MS-imaging campaign — [spinalcordtoolbox](https://github.com/spinalcordtoolbox/spinalcordtoolbox/pull/5263), [nibabel](https://github.com/nipy/nibabel/pull/1522), [dicom2nifti](https://github.com/icometrix/dicom2nifti/pull/166), [LST-AI](https://github.com/CompImg/LST-AI/pull/45) *(DICOM / NIfTI · MS lesion tooling)*

**Fintech & data**
- **[schwifty](https://github.com/mdomke/schwifty/pull/292)** — correct ISO 7064 mod-97-10 checksum for BA *(IBAN)*
- **[faker](https://github.com/joke2k/faker/pull/2403)** — compute a valid ISO 7064 Mod 11,10 check digit for the de_DE `vat_id` *(test-data)*
- **[aeon](https://github.com/aeon-toolkit/aeon/pull/3585)** — `Padder` validates `fill_value`, rejects array-likes *(time-series ML)*

**Developer tooling & infra**
- **[jaeger](https://github.com/jaegertracing/jaeger/pull/8902)** — MCP tooling reports `total_count` + truncation *(observability · MCP · CNCF)*
- **[octokit/request.js](https://github.com/octokit/request.js/pull/820)** — handle primitive JSON error bodies without throwing *(GitHub SDK)*
- **[js-joda](https://github.com/js-joda/js-joda/pull/804)** — `Instant.parse` accepts and resolves an offset *(date-time)*
- **[krkn-ai](https://github.com/krkn-chaos/krkn-ai/pull/382)** — include dependency in `CompositeScenario` identity *(chaos engineering)*

More fixes merged/in-review across DuckDB, growthbook, django-scim2, OpenTelemetry, cargo-deny, Zettlr, and Adyen.

---

### Stack
**AI / LLM** — multi-provider APIs (Claude · OpenAI · Groq) · prompt & system-prompt design · multi-agent orchestration · Model Context Protocol (self-authored servers) · RAG · vector DBs · vision-OCR · Ollama
**Languages** — TypeScript · Python · JavaScript · SQL · Rust · Bash
**Medical / imaging** — DICOM · NIfTI · neuroimaging pipelines (MNE, nibabel, spinalcordtoolbox) · FHIR / HL7 (learning)
**Data / Quant** — pandas · NumPy · SciPy · scikit-learn · backtesting · Monte-Carlo simulation
**Mobile / Web** — React Native · React 19 · Expo · SQLite · Firebase · Express · Vite
**Infra / Quality** — AWS (Lambda / SAM) · Docker · Linux · GitHub Actions · unit / contract / regression testing · observability (OpenTelemetry) · signed commits

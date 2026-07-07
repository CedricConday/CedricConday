# Cedric Conday — Software Engineer · AI / Full-Stack

Self-taught software engineer. I build LLM-powered products and agent systems end to end, with AI as the method — orchestrating several agents as a one-person team. Current interest: medical software and fintech / payments. TypeScript + Python. **Open to remote roles and relocation, incl. New Zealand.** *In Deutschland ansässig; Deutsch und Englisch, remote wie vor Ort.*

📫 cedric@condaydigital.com · [LinkedIn](https://linkedin.com/in/cedricconday)

---

### Featured work

**[xe-mcp](https://github.com/CedricConday/xe-mcp)** — MCP server for the Xe Currency Data API *(TypeScript · 49 tests · CI · AWS Lambda)*
FX tools — rate, conversion, volatility, optimal send-window, correlation, charts — with a free ECB fallback so it runs with zero credentials.

**[centrapay-mcp](https://github.com/CedricConday/centrapay-mcp)** — MCP server for Centrapay, NZ payments *(TypeScript · npm · contract tests)*
Nine tools modelled on the real Centrapay API — payment requests, settlement, idempotent refunds, merchants — with fetch-mock contract tests over every request.

**[Protocol Tracker](https://github.com/CedricConday/protocol-tracker)** — health app for a real MS treatment protocol, built for a family member's multiple-sclerosis care. Shipped in two builds:
- **v1 — cross-platform native** *(React Native · Expo · TypeScript · SQLite)*: multi-provider LLM **vision-OCR** (Anthropic / OpenAI / Groq) reads a photographed medical report and auto-fills structured data — BYO-key, with token & cost guardrails; offline-first SQLite (versioned migrations), biometric auth, PDF reports, EN/DE, accessibility-oriented.
- **v2 — re-architected as a zero-knowledge PWA** *(vanilla JS · Capacitor iOS/Android · IndexedDB · PBKDF2→AES-GCM-256)*: all patient data encrypted client-side, no server, encrypted backup/restore — privacy by design shrinks the compliance surface to zero.

**[nifti-qc](https://github.com/CedricConday/nifti-qc)** — quality-control for medical-imaging geometry *(Python)*
Catches silently-broken NIfTI qform/sform geometry before it corrupts a neuroimaging pipeline — the kind of quiet data bug that invalidates an MS-lesion analysis without ever raising an error.

### Open-source contributions
Bugs found, reproduced, fixed *with a regression test*, and merged upstream — **19 merged across 14 established projects**:
<!-- COUNT IS LIVE: never hardcode from memory — verify with `gh search prs --author CedricConday --merged --limit 100 --json url --jq 'length'` before editing. -->


**Medical & neuro-imaging**
- **[mne-python](https://github.com/mne-tools/mne-python/pull/14002)** — eyetracking calibration files read as UTF-8 *(neuroimaging)*
- **[nibabel](https://github.com/nipy/nibabel/pull/1522)** — set `patient_birth_date` dtype in the ECAT header to signed int32 *(neuroimaging — also earned a [CITATION.cff credit](https://github.com/nipy/nibabel/pull/1524))*
- *In review:* MS-imaging campaign — [dicom2nifti](https://github.com/icometrix/dicom2nifti/pull/166), [LST-AI](https://github.com/CompImg/LST-AI/pull/45) *(DICOM / NIfTI · MS lesion tooling)*

**Fintech & data**
- **[schwifty](https://github.com/mdomke/schwifty/pull/292)** — correct ISO 7064 mod-97-10 checksum for BA *(IBAN)*
- **[faker](https://github.com/joke2k/faker/pull/2403)** — compute a valid ISO 7064 Mod 11,10 check digit for the de_DE `vat_id` *(test-data)*
- **[aeon](https://github.com/aeon-toolkit/aeon/pull/3585)** — `Padder` validates `fill_value`, rejects array-likes *(time-series ML)*
- **[dpdata](https://github.com/deepmodeling/dpdata/pull/1010)** — build pymatgen `Molecule` species from `atom_types` order *(computational materials · DeepModeling)*

**Developer tooling & infra**
- **[jaeger](https://github.com/jaegertracing/jaeger/pull/8902)** — MCP tooling reports `total_count` + truncation *(observability · MCP · CNCF)*
- **[octokit/request.js](https://github.com/octokit/request.js/pull/820)** — handle primitive JSON error bodies without throwing *(GitHub SDK)*
- **[js-joda](https://github.com/js-joda/js-joda/pull/804)** — `Instant.parse` accepts and resolves an offset *(date-time)*
- **[krkn-ai](https://github.com/krkn-chaos/krkn-ai/pull/382)** — include dependency in `CompositeScenario` identity *(chaos engineering)*

More merged across DuckDB, growthbook, django-scim2, and Adyen; further fixes in review across OpenTelemetry and cargo-deny.

---

### Stack

| | |
|---|---|
| **Languages** | TypeScript · Python · JavaScript · SQL · Rust · Bash |
| **AI / LLM** | Multi-provider APIs (Claude · OpenAI · Groq) · MCP (self-authored servers) · multi-agent orchestration · RAG · vector DBs · vision-OCR |
| **Web / Mobile** | React · React Native · Expo · Vite · Express · SQLite · Firebase |
| **Data / Quant** | pandas · NumPy · SciPy · scikit-learn · backtesting · Monte-Carlo |
| **Medical / imaging** | DICOM · NIfTI · neuroimaging (MNE · nibabel) · FHIR / HL7 (learning) |
| **Infra / Quality** | AWS (Lambda · SAM) · Docker · Linux · GitHub Actions · unit / contract / regression tests · OpenTelemetry · signed commits |

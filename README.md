# Cedric Conday

TypeScript · Python. LLM tooling and MCP servers, medical / neuro-imaging software, payments and fintech data.

Germany — remote or on-site, German and English.
cedric@condaydigital.com · [condaydigital.com](https://www.condaydigital.com) · [LinkedIn](https://linkedin.com/in/cedricconday)

---

## Repositories

| repo | what it does |
|---|---|
| [xe-mcp](https://github.com/CedricConday/xe-mcp) | MCP server for the Xe Currency Data API — rates, conversion, volatility, moving averages, alerts, charts. Free ECB fallback, so it runs with no credentials. TypeScript. |
| [centrapay-mcp](https://github.com/CedricConday/centrapay-mcp) | MCP server for the Centrapay payments API (NZ) — payment requests, sandbox settlement, refunds, merchants. Verified against the live sandbox. TypeScript. |
| [buzz-mcp](https://github.com/CedricConday/buzz-mcp) | Joins any MCP client to a Buzz (NIP-29) relay as a first-class member — own keypair, own audit trail. Zero dependencies. |
| [x402-inspect](https://github.com/CedricConday/x402-inspect) | Decodes and validates x402 protocol messages — payment headers and payloads — from the CLI. |
| [nifti-qc](https://github.com/CedricConday/nifti-qc) | Catches silently-broken NIfTI geometry — qform/sform mismatch, bad affines, misaligned inputs — before a neuroimaging pipeline consumes it. Python. |
| [ms-twin-treat](https://github.com/CedricConday/ms-twin-treat) | Backtest-gated multi-scale simulation of MS interventions in silico, checked against known trial outcomes. Experimental; not validated, and not evidence about MS. |
| [automation-console](https://github.com/CedricConday/automation-console) | B2B workflow automation console — rule engine with trigger/condition/action modelling, live run log, KPI rollups. Angular 18, standalone components, signals, strict TypeScript. |
| [tryhackme-writeups](https://github.com/CedricConday/tryhackme-writeups) | Technique-first TryHackMe writeups — web, binary exploitation, blue-team, DFIR, OSINT. |
| protocol-tracker | Health-protocol tracker, two builds: React Native / Expo / SQLite with multi-provider vision-OCR, then re-architected as a zero-knowledge PWA (Capacitor, IndexedDB, PBKDF2→AES-GCM-256, no server). Private repo. |

## Merged upstream

47 pull requests across 17 projects — each a bug found, reproduced, fixed with a regression test, and merged.

<!-- COUNTS ARE LIVE: never hardcode from memory. Verify both numbers before editing:
     gh api graphql --paginate -f query='query($endCursor:String){user(login:"CedricConday"){pullRequests(first:100,after:$endCursor,states:[MERGED]){totalCount pageInfo{hasNextPage endCursor} nodes{repository{nameWithOwner}}}}}'
     Swap states:[OPEN] for the in-review figure. `gh search prs` is a lagging index and omits states you did not ask for — do not use it. -->

**Medical & neuro-imaging** — 10
- [mne-python](https://github.com/mne-tools/mne-python) ×6 — [eyelink calibration files read as UTF-8](https://github.com/mne-tools/mne-python/pull/14002), [warn when epoch events fall outside the raw range](https://github.com/mne-tools/mne-python/pull/14004), [transition bandwidth in the "filter too short" error](https://github.com/mne-tools/mne-python/pull/14005), [pick-channels crash when `_orig_units` is None](https://github.com/mne-tools/mne-python/pull/14006), [`block` argument for `stc.plot()`](https://github.com/mne-tools/mne-python/pull/14185), [missing f-string prefixes in error messages](https://github.com/mne-tools/mne-python/pull/14008)
- [nibabel](https://github.com/nipy/nibabel) ×2 — [`patient_birth_date` dtype in the ECAT header set to signed int32](https://github.com/nipy/nibabel/pull/1522), plus a [CITATION.cff credit](https://github.com/nipy/nibabel/pull/1524)
- [nilearn](https://github.com/nilearn/nilearn) ×2 — [clean non-finite values when smoothing surface images](https://github.com/nilearn/nilearn/pull/6503), [send the requested slice index to the brainsprite viewer](https://github.com/nilearn/nilearn/pull/6505)

**Fintech, IBAN & data** — 22
- [faker](https://github.com/joke2k/faker) ×8 — IBAN generators for [de_DE](https://github.com/joke2k/faker/pull/2403), [es_ES](https://github.com/joke2k/faker/pull/2404), [da_DK](https://github.com/joke2k/faker/pull/2409), [pt_BR](https://github.com/joke2k/faker/pull/2410), [en_IE](https://github.com/joke2k/faker/pull/2411), [nl_BE](https://github.com/joke2k/faker/pull/2412), [ru_RU](https://github.com/joke2k/faker/pull/2416), [uk_UA](https://github.com/joke2k/faker/pull/2417) — each producing values that failed `python-stdnum` validation
- [schwifty](https://github.com/mdomke/schwifty) ×4 — [ISO 7064 mod-97-10 registered for BA, not BT](https://github.com/mdomke/schwifty/pull/292), [validate IBAN characters over the full string](https://github.com/mdomke/schwifty/pull/293), [add Yemen to the registry](https://github.com/mdomke/schwifty/pull/294), [random BBANs that satisfy the national checksum](https://github.com/mdomke/schwifty/pull/296)
- [aeon](https://github.com/aeon-toolkit/aeon) ×4 — [`Padder` validates `fill_value`](https://github.com/aeon-toolkit/aeon/pull/3585), [`AutoARIMA` respects `max_d`](https://github.com/aeon-toolkit/aeon/pull/3614), [`NaiveForecaster` validates `seasonal_period`](https://github.com/aeon-toolkit/aeon/pull/3615), [Extended Isolation Forest detector](https://github.com/aeon-toolkit/aeon/pull/3626)
- [dpdata](https://github.com/deepmodeling/dpdata) ×3 — [pymatgen `Molecule` species built from `atom_types` order](https://github.com/deepmodeling/dpdata/pull/1010), [tuple dtype in `DataType` repr](https://github.com/deepmodeling/dpdata/pull/1005), [skip empty optional frame arrays on dump](https://github.com/deepmodeling/dpdata/pull/1011)
- [growthbook](https://github.com/growthbook/growthbook) ×2 — [URL casing preserved in pre-launch checklists](https://github.com/growthbook/growthbook/pull/6238), [`$elemMatch` matches falsy array elements](https://github.com/growthbook/growthbook/pull/6323)
- [duckdb-web](https://github.com/duckdb/duckdb-web) — [Parquet row-group pruning tip](https://github.com/duckdb/duckdb-web/pull/6983)

**Developer tooling, infra & security** — 15
- [zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) ×2 — [Slack tokens redacted in the leak detector](https://github.com/zeroclaw-labs/zeroclaw/pull/8918), [deferred `tool_search` resolves granted MCP tools](https://github.com/zeroclaw-labs/zeroclaw/pull/8775)
- [jaeger](https://github.com/jaegertracing/jaeger) ×2 — [MCP reports `total_count` and truncation](https://github.com/jaegertracing/jaeger/pull/8902), [cap `read_skill` output at `max_read_file_size`](https://github.com/jaegertracing/jaeger/pull/8993)
- [octokit/request.js](https://github.com/octokit/request.js) ×2 — [primitive JSON error bodies no longer throw](https://github.com/octokit/request.js/pull/820), [`application/octet-stream` not decoded as text](https://github.com/octokit/request.js/pull/823)
- [js-joda](https://github.com/js-joda/js-joda) ×2 — [`Instant.parse` accepts and resolves an offset](https://github.com/js-joda/js-joda/pull/804), [non-uniquely-parsable text styles excluded from parsing](https://github.com/js-joda/js-joda/pull/810)
- [krkn-ai](https://github.com/krkn-chaos/krkn-ai) ×2 — [dependency included in `CompositeScenario` identity](https://github.com/krkn-chaos/krkn-ai/pull/382), [skip pods with no containers](https://github.com/krkn-chaos/krkn-ai/pull/397)
- [adyen-node-api-library](https://github.com/Adyen/adyen-node-api-library) ×2 — HMAC length guards in [`NexoCrypto.validateHmac`](https://github.com/Adyen/adyen-node-api-library/pull/1712) and [`HmacValidator`](https://github.com/Adyen/adyen-node-api-library/pull/1725)
- [django-scim2](https://github.com/15five/django-scim2) ×2 — [`itemsPerPage` reflects resources returned](https://github.com/15five/django-scim2/pull/210), [SCIM error raised on `IntegrityError` in `PutView`](https://github.com/15five/django-scim2/pull/214)
- [mailerlite-nodejs](https://github.com/mailerlite/mailerlite-nodejs) — [edge/serverless runtimes via axios adapter fallback](https://github.com/mailerlite/mailerlite-nodejs/pull/107)

## In review

25 open across 15 projects — [nibabel](https://github.com/nipy/nibabel/pulls/CedricConday) ×7, [claude-code-security-review](https://github.com/anthropics/claude-code-security-review/pulls/CedricConday) ×5, and one each in opentelemetry-collector-contrib, pynetdicom, nipype, pybids, linkml, sandbox-runtime, buzz, traceroot, constructorio-client-javascript, nilearn, mne-python, faker, mailerlite-nodejs.

## Stack

| | |
|---|---|
| **Languages** | TypeScript · Python · JavaScript · SQL · Rust · Bash |
| **AI / LLM** | Multi-provider APIs (Claude · OpenAI · Groq) · MCP (self-authored servers) · multi-agent orchestration · RAG · vector DBs · vision-OCR |
| **Web / Mobile** | React · React Native · Expo · Vite · Express · SQLite · Firebase |
| **Data / Quant** | pandas · NumPy · SciPy · scikit-learn · backtesting · Monte-Carlo |
| **Medical / imaging** | DICOM · NIfTI · neuroimaging (MNE · nibabel) · FHIR / HL7 (learning) |
| **Infra / Quality** | AWS (Lambda · SAM) · Docker · Linux · GitHub Actions · unit / contract / regression tests · OpenTelemetry · signed commits |

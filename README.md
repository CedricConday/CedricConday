# Cedric Conday

I am a cognitive scientist. I started writing software in April 2026 because the tools I wanted for multiple sclerosis did not exist, and building them was the fastest way to find out whether they could.

## What I build

**[Protocol Tracker](https://github.com/CedricConday/protocol-tracker)** is an Android app for people on a high-dose vitamin D3 protocol. The day is anchored to the patient's own first dose rather than the clock, every reminder is an offset from it, and the record of doses, symptoms and relapses never leaves the device. It began as a build for one patient and ships as a signed APK anyone can verify.

**[ms-twin-treat](https://github.com/CedricConday/ms-twin-treat)** asks whether a multi-scale simulation of an MS therapy can be trusted at all. The backtest harness was built before the model, and nothing in the model is believed until it replays a known trial outcome. The honest result so far: the cell model beats both nulls on real interferon-beta data, and the foundation-model embedding I expected to carry it is statistically indistinguishable from a plain correlation matrix. The README says so.

**[lesiontrack](https://github.com/CedricConday/lesiontrack)** finds new, enlarging, shrinking and slowly expanding MS lesions across MRI timepoints, with one registration dependency and a run time of minutes. A synthetic backtest has to pass before any number is reported. It earned its keep immediately: it showed the registration tool's own Jacobian recovering under a third of the injected expansion, so the package now computes the Jacobian itself.

**[bidsgate](https://github.com/CedricConday/bidsgate)** turns that check into a gate for any BIDS pipeline. Inject a known lesion or volume change into real data, run the tool, score what came back. The first scorecard is LST-AI on OpenNeuro controls, and it says plainly which lesion sizes the segmenter misses.

**[nifti-qc](https://github.com/CedricConday/nifti-qc)** catches the qform/sform disagreement that silently mislocates an image in world space. I first fixed that bug inside LST-AI's own pipeline, then wrote the check so nobody has to find it three steps downstream again.

Two tools came out of the work itself rather than the subject. **[gh-odds](https://github.com/CedricConday/gh-odds)** measures, before you open a pull request, whether a repository actually merges outsiders and how long that takes. **[cachemiss](https://github.com/CedricConday/cachemiss)** reads the transcripts Claude Code keeps on disk and explains where a quota went.

Earlier, and still maintained: MCP servers for [Xe currency data](https://github.com/CedricConday/xe-mcp) and the [Centrapay](https://github.com/CedricConday/centrapay-mcp) payments API, and a decoder for [x402](https://github.com/CedricConday/x402-inspect) payment headers.

## Upstream

Most of what I know about the neuroimaging stack I learned by fixing it. Merged work in [nibabel](https://github.com/nipy/nibabel/pulls?q=is%3Apr+author%3ACedricConday), [nilearn](https://github.com/nilearn/nilearn/pulls?q=is%3Apr+author%3ACedricConday) and [MNE-Python](https://github.com/mne-tools/mne-python/pulls?q=is%3Apr+author%3ACedricConday) covers an ECAT header dtype, non-finite values in surface smoothing, the brainsprite slice index, EyeLink calibration encoding, and epoch events that fall outside the raw range. Before that it was banking identifiers: IBAN generators in [Faker](https://github.com/joke2k/faker/pulls?q=is%3Apr+author%3ACedricConday) that pass real checksum validation, and the registry in [schwifty](https://github.com/mdomke/schwifty/pulls?q=is%3Apr+author%3ACedricConday). The rest runs from Jaeger's MCP server to Adyen's HMAC validator to the OpenTelemetry collector. [The full list](https://github.com/pulls?q=is%3Apr+author%3ACedricConday+is%3Amerged+-user%3ACedricConday) is one search away.

Each one was a bug reproduced, fixed with a regression test, and accepted by the people who maintain the code.

## Elsewhere

[condaydigital.com](https://condaydigital.com). Germany. English and German.

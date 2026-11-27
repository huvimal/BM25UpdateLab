# BM25UpdateLab

Verify add, replacement and deletion document frequencies and rankings against a clean rebuild.

**Implemented scope:** Small in-memory BM25 updates with add, replace and delete. Not a concurrent persistent search engine or semantic retriever.

## Reproduce

Python 3.11, NumPy 2.4.6, CPU only. No API key, external dataset, model download, Docker or GPU.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -B run.py
Start-Process .\reports\report.html
```

Series runner on the owner's machine:

```powershell
Set-Location "D:\AI-Projects\outputs\AI-80-SelfServe"
python -B manager.py run --project 68
```

The installer records a shared Python runtime with NumPy so forty duplicate environments are not needed. The manager dispatches to that interpreter even when invoked with base Python.

## What is measured

`experiment.py` contains the full algorithm, authored fixtures, random seeds, train/calibration/evaluation access and meaningful success/failure assertions. Read the implementation before interpreting the figures. `common.py` supplies shared numerical helpers, not canned result data. There are no prefilled success reports.

Run outputs: `reports/results.json` with actual metrics, source fingerprints, dependency versions and explicit scope; `reports/RESULTS.md`; escaped offline `reports/report.html`. A failure saves `private/last-error.txt` and blocks publication-kit generation. Passed checks mean the local experiment executed consistently, not that the model performed well.

## Data and limitations

All bundled numerical/text/event/binary fixtures are authored for this repository and released under MIT. They are **synthetic or fictional**, not customer data or independently judged benchmarks. There are no third-party weights. Most experiments are small mechanism/ablation studies; simulations must be labelled as simulations. Non-ML infrastructure experiments are deterministic components relevant to AI pipelines and must not be described as learned AI models.

Distinct focus: Verify add, replacement and deletion document frequencies and rankings against a clean rebuild. This repository does not claim any functionality beyond its implemented scope above. No deployment, hosted CI, real customer impact, guaranteed privacy/security, complete detection, generic language understanding or universal performance claim. Small sample uncertainty and negative outcomes remain part of the result. Do not tune on evaluation data and continue calling the same results untouched test performance.

## Extend responsibly

Try a second independently generated seed, a separately licensed real dataset where appropriate, a stronger baseline and additional boundary cases. Preserve the original result and describe the changed protocol. Those extensions are not claimed as already implemented here.

## Publishing

After inspecting the current passing report, the series manager generates GitHub instructions and LinkedIn/Upwork drafts outside this repository. It never creates repositories, commits, pushes or posts. Keep `.gitignore`; do not add private data or logs. Inspect result scope, units and counterexamples before reusing any number in a profile.

## License

MIT, copyright 2026 Le Mai Vinh Hung. Covers repository code and authored fixtures; it grants no rights to outside datasets later supplied by a user.

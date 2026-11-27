# BM25UpdateLab — measured local run

Small in-memory BM25 updates with add, replace and delete. Not a concurrent persistent search engine or semantic retriever.

## Results

```json
{
  "incremental_ranking": [
    [
      "8",
      2.5618676909241285
    ],
    [
      "0",
      1.2809338454620642
    ],
    [
      "1",
      1.2809338454620642
    ],
    [
      "3",
      0.0
    ],
    [
      "4",
      0.0
    ],
    [
      "5",
      0.0
    ],
    [
      "6",
      0.0
    ],
    [
      "7",
      0.0
    ]
  ],
  "document_frequencies": {
    "snapshot": 1,
    "database": 1,
    "backup": 2,
    "restore": 2,
    "worker": 1,
    "restart": 1,
    "jobs": 1,
    "queue": 1,
    "expiration": 1,
    "renew": 1,
    "certificate": 1,
    "tls": 1,
    "timeout": 1,
    "packet": 1,
    "trace": 1,
    "network": 1,
    "clear": 1,
    "stale": 1,
    "records": 1,
    "cache": 1,
    "rebuild": 1,
    "index": 1,
    "search": 1,
    "documents": 1,
    "password": 2,
    "account": 1,
    "token": 1,
    "reset": 1,
    "audit": 1
  },
  "checks": [
    "Incremental DF equals clean rebuild",
    "Updated BM25 scores match full rebuild exactly"
  ],
  "scope": "Small in-memory BM25 updates with add, replace and delete. Not a concurrent persistent search engine or semantic retriever."
}
```

Local experiment assertions passed. This does not establish production readiness or performance on real customer data. Source fingerprints and dependency versions are in results.json.

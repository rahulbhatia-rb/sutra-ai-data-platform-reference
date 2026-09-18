# Multi-Tenant AI Data Pipeline Guard

This is a runnable POC for Sutra.AI’s Senior Platform Engineer role. It admits customer data only when tenant identity, source, schema compatibility, data quality, lineage, PII scope, and batch size are explicit.

`src/app.py` is a JSON-lines interface. Feed it batch events and it returns an `admit` or `quarantine` decision, a stable batch ID, and blockers. This makes the POC usable from an Airflow task, Lambda, Kafka consumer, or API before storage, embedding, analytics, or agent retrieval.

```bash
python3 -m unittest discover -s tests -v
python3 -m src.app < examples/events.jsonl
```

Candidate: https://www.linkedin.com/in/rahul-h-bhatia/ · https://rahulhbhatia.vercel.app

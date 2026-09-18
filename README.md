# Multi-Tenant AI Data Pipeline Guard

Application reference for Sutra.AI’s Senior Platform Engineer role. The tested policy admits a customer data batch only when tenant identity, schema compatibility, data quality, lineage, and PII scope are all explicit.

This models safe AWS data/RAG foundations: an Airflow or event-driven adapter can run the guard before storage, embedding, analytics, or agent retrieval; failures become actionable records rather than silently contaminating downstream AI results.

```bash
python3 -m unittest discover -s tests -v
```

Candidate: https://www.linkedin.com/in/rahul-h-bhatia/ · https://rahulhbhatia.vercel.app

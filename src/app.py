import json,sys
from .pipeline_guard import Batch,preflight
def evaluate(p):
 required={'tenant','source','schema_ok','quality_ok','lineage_ok','pii_scoped','record_count'}
 if required-p.keys():return {'decision':'quarantine','blockers':['incomplete-event']}
 return preflight(Batch(**{k:p[k] for k in required}))
if __name__=='__main__':
 for line in sys.stdin:
  if line.strip():print(json.dumps(evaluate(json.loads(line))))

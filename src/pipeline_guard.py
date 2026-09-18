from dataclasses import dataclass
from hashlib import sha256
@dataclass(frozen=True)
class Batch:
 tenant:str; source:str; schema_ok:bool; quality_ok:bool; lineage_ok:bool; pii_scoped:bool; record_count:int
def admit(b:Batch)->tuple[bool,tuple[str,...]]:
 x=[]
 if not b.tenant:x.append('tenant-required')
 if not b.source:x.append('source-required')
 if b.record_count<1:x.append('empty-batch')
 if not b.schema_ok:x.append('schema-drift')
 if not b.quality_ok:x.append('quality-failed')
 if not b.lineage_ok:x.append('lineage-missing')
 if not b.pii_scoped:x.append('pii-unscoped')
 return not x,tuple(x)
def preflight(b:Batch)->dict:
 ok,blockers=admit(b)
 return {'decision':'admit' if ok else 'quarantine','batch_id':sha256(f'{b.tenant}:{b.source}:{b.record_count}'.encode()).hexdigest()[:12],'blockers':list(blockers)}

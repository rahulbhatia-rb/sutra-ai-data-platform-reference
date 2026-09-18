from dataclasses import dataclass
@dataclass(frozen=True)
class Batch: tenant:str; schema_ok:bool; quality_ok:bool; lineage_ok:bool; pii_scoped:bool
def admit(b:Batch)->tuple[bool,tuple[str,...]]:
 x=[]
 if not b.tenant:x.append('tenant-required')
 if not b.schema_ok:x.append('schema-drift')
 if not b.quality_ok:x.append('quality-failed')
 if not b.lineage_ok:x.append('lineage-missing')
 if not b.pii_scoped:x.append('pii-unscoped')
 return not x,tuple(x)

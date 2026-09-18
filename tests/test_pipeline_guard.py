import unittest
from src.pipeline_guard import Batch,admit
class T(unittest.TestCase):
 def b(self,**k):
  d=dict(tenant='acme',schema_ok=True,quality_ok=True,lineage_ok=True,pii_scoped=True);d.update(k);return Batch(**d)
 def test_admit(self):self.assertTrue(admit(self.b())[0])
 def test_schema(self):self.assertIn('schema-drift',admit(self.b(schema_ok=False))[1])
 def test_pii(self):self.assertFalse(admit(self.b(pii_scoped=False))[0])

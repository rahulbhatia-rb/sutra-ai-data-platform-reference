import unittest
from src.app import evaluate
from src.pipeline_guard import Batch,admit,preflight
class T(unittest.TestCase):
 def b(self,**k):
  d=dict(tenant='acme',source='crm',schema_ok=True,quality_ok=True,lineage_ok=True,pii_scoped=True,record_count=10);d.update(k);return Batch(**d)
 def test_admit(self):self.assertTrue(admit(self.b())[0])
 def test_schema(self):self.assertIn('schema-drift',admit(self.b(schema_ok=False))[1])
 def test_pii(self):self.assertFalse(admit(self.b(pii_scoped=False))[0])
 def test_poc_interface(self):self.assertEqual(evaluate({'tenant':'x'})['decision'],'quarantine')
 def test_audit_id(self):self.assertEqual(preflight(self.b())['batch_id'],preflight(self.b())['batch_id'])

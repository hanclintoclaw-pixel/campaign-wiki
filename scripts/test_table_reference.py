import copy,unittest,tempfile
from pathlib import Path
from validate_table_reference import validate,inspect
class Schema(unittest.TestCase):
 def block(self):
  unknown={'value':None,'assertion_status':'unknown','qualifiers':['Not reviewed.'],'source_refs':[]}
  facts={k:copy.deepcopy(unknown) for k in ['identity','role','current_status','specialties','limitations']}
  facts['identity']={'value':'Example person','assertion_status':'provisional','qualifiers':[],'source_refs':['#overview']}
  return {'schema_version':1,'entity_kind':'pc','as_of':'2026-11-22','facts':facts,'sections':{'current_balances':'Current Karma and Nuyen'}}
 def test_valid_format(self):self.assertEqual(validate(self.block(),'## Current Karma and Nuyen\n'),[])
 def test_unknown_not_zero_and_status(self):
  b=self.block();b['facts']['role']['value']=0;self.assertTrue(validate(b))
  b=self.block();b['facts']['identity']['source_refs']=[];self.assertTrue(validate(b))
 def test_required_and_dates(self):
  for key in ['facts','as_of','entity_kind','schema_version']:
   b=self.block();del b[key];self.assertTrue(validate(b),key)
 def test_asset_and_missing_section(self):
  b=self.block();b['entity_kind']='asset';self.assertTrue(validate(b));self.assertTrue(validate(self.block(),'# No balance heading\n'))
 def test_unmigrated_and_duplicate_keys(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'x.md';p.write_text('---\ntitle: X\n---\n# X\n');self.assertEqual(inspect(p)['status'],'unmigrated');self.assertEqual(inspect(p,True)['status'],'error')
   p.write_text('---\ntitle: X\ntitle: Y\n---\n')
   with self.assertRaises(ValueError):inspect(p)
if __name__=='__main__':unittest.main()

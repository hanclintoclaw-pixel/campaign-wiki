#!/usr/bin/env python3
"""Authoring-only draft schema validator. Does not authorize facts or index pages."""
import argparse,datetime,json,re,sys
from pathlib import Path
try:import yaml
except ImportError:raise SystemExit('PyYAML is required; no packages were installed.')
class UniqueLoader(yaml.SafeLoader):pass
def unique(loader,node,deep=False):
 out={}
 for k,v in node.value:
  key=loader.construct_object(k,deep=deep)
  if key in out:raise ValueError('duplicate YAML key: '+str(key))
  out[key]=loader.construct_object(v,deep=deep)
 return out
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique)
CORE={'identity','role','current_status','specialties','limitations'}
ASSET={'class','owner','operator'}
def strings(x):return isinstance(x,list) and all(isinstance(s,str) and s.strip() for s in x)
def validate(block,body=None):
 e=[]
 if not isinstance(block,dict):return ['table_reference must be a mapping']
 if set(block)-{'schema_version','entity_kind','as_of','facts','sections'}:e.append('unknown table_reference fields')
 if type(block.get('schema_version')) is not int or block['schema_version']!=1:e.append('schema_version must be 1')
 kind=block.get('entity_kind')
 if kind not in ('pc','npc','asset'):e.append('entity_kind must be pc/npc/asset')
 date=block.get('as_of')
 try:
  if not isinstance(date,str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',date):raise ValueError()
  datetime.date.fromisoformat(date)
 except (ValueError,TypeError):e.append('as_of must be a quoted ISO date')
 facts=block.get('facts')
 if not isinstance(facts,dict):return e+['facts must be a mapping']
 required=CORE|(ASSET if kind=='asset' else set())
 if required-set(facts):e.append('missing facts: '+','.join(sorted(required-set(facts))))
 if set(facts)-(CORE|ASSET):e.append('unknown fact keys; use approved schema upgrade, not silent additions')
 for key,f in facts.items():
  if not isinstance(f,dict):e.append(key+': fact must be mapping');continue
  if set(f)!={'value','assertion_status','qualifiers','source_refs'}:e.append(key+': exact fact fields required')
  status=f.get('assertion_status');value=f.get('value');qual=f.get('qualifiers');refs=f.get('source_refs')
  if status not in ('confirmed','provisional','unknown','unresolved'):e.append(key+': invalid assertion_status')
  if not strings(qual) or not strings(refs):e.append(key+': qualifiers/source_refs must be string lists')
  if status in ('unknown','unresolved'):
   if value is not None or not qual:e.append(key+': unknown/unresolved requires null and an explanation')
  elif status in ('confirmed','provisional'):
   if not ((isinstance(value,str) and value.strip()) or (strings(value) and value)) or not refs:e.append(key+': known assertion requires text/list value and source_refs')
  for ref in refs if isinstance(refs,list) else []:
   if not isinstance(ref,str) or ref.startswith(('/','file:')) or re.match(r'^[A-Za-z]:[\\/]',ref):e.append(key+': private/absolute filesystem reference forbidden')
 sections=block.get('sections',{})
 if not isinstance(sections,dict):e.append('sections must be mapping');sections={}
 if set(sections)-{'current_balances','equipment','native_stats','history'}:e.append('unknown section keys')
 if kind=='pc' and not sections.get('current_balances'):e.append('pc must reference canonical current_balances section, not duplicate values')
 for key,heading in sections.items():
  if not isinstance(heading,str) or not heading.strip():e.append(key+': section heading must be text')
  elif body is not None and not re.search(r'^#{1,6} '+re.escape(heading)+r'\s*$',body,re.M):e.append(key+': referenced heading missing')
 return e
def inspect(path,require=False):
 text=Path(path).read_text();m=re.match(r'\A---\s*\n(.*?)\n---\s*(?:\n|$)',text,re.S)
 if text.startswith('---') and not m:raise ValueError('malformed/unclosed frontmatter')
 fm=yaml.load(m[1],Loader=UniqueLoader) if m else {}
 if not isinstance(fm,dict):raise ValueError('frontmatter must be mapping')
 if 'table_reference' not in fm:return {'path':str(path),'status':'error' if require else 'unmigrated','errors':['table_reference absent'] if require else []}
 errors=validate(fm['table_reference'],text[m.end():] if m else text)
 return {'path':str(path),'status':'error' if errors else 'valid-format','errors':errors,'semantic_authority':'not checked'}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--require',action='store_true');p.add_argument('pages',nargs='+');args=p.parse_args();rows=[]
 for page in args.pages:
  try:rows.append(inspect(page,args.require))
  except (OSError,ValueError,yaml.YAMLError) as x:rows.append({'path':page,'status':'error','errors':[str(x)]})
 print(json.dumps(rows,indent=2));return int(any(x['status']=='error' for x in rows))
if __name__=='__main__':raise SystemExit(main())

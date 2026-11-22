import argparse,csv,json,sys
from pathlib import Path
from urllib.parse import urlparse
def load(path):
    records=json.loads(path.read_text(encoding='utf-8'));seen=set()
    if not isinstance(records,list): raise ValueError('Expected an array')
    for row in records:
        for key in ['id','name','kind','source']:
            if not isinstance(row.get(key),str) or not row[key].strip(): raise ValueError('Missing '+key)
        if row['id'] in seen: raise ValueError('Duplicate id '+row['id'])
        source=urlparse(row['source'])
        if source.scheme!='https' or not source.hostname: raise ValueError('Invalid source')
        seen.add(row['id'])
    return records
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--input',type=Path,default=Path(__file__).parent/'data/regions.json')
    p.add_argument('--search',default='');p.add_argument('--csv',action='store_true');a=p.parse_args()
    rows=[x for x in load(a.input) if a.search.casefold() in (x['id']+' '+x['name']).casefold()]
    if a.csv:
        w=csv.DictWriter(sys.stdout,fieldnames=['id','name','kind','source'],extrasaction='ignore');w.writeheader();w.writerows(rows)
    else: print(json.dumps(rows,indent=2))

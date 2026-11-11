import json,base64,gzip,re,sys,os
F=sys.argv[1]; out=sys.argv[2]
s=open(F).read()
m=re.search(r'<script type="__bundler/manifest">\s*(.*?)\s*</script>',s,re.S)
man=json.loads(m.group(1))
t=re.search(r'<script type="__bundler/template">\s*(.*?)\s*</script>',s,re.S)
open(os.path.join(out,'template.html'),'w').write(json.loads(t.group(1)))
for u,e in man.items():
    b=base64.b64decode(e['data'])
    if e.get('compressed'): b=gzip.decompress(b)
    ext=e['mime'].split('/')[-1].replace('+xml','')
    open(os.path.join(out,f"{u}.{ext}"),'wb').write(b)
    print(u,e['mime'],len(b))

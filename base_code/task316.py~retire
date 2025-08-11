def p(g):
 l=[x for c,x in sorted(((c,x)for r in g for c,x in enumerate(r)if x))]
 o=[]
 for i in range(3):
  t=l[i*3:i*3+3]
  o.append(((t[::-1]if i&1 else t)+[0]*3)[:3])
 return o

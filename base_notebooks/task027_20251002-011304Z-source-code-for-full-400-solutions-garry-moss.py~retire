def p(r):
 d=[l[:]for l in r];a={(i,q)for i in range(len(r))for q in range(len(r[0]))if r[i][q]==1}
 if not a:return d
 for l in[0,1]:
  e=set()
  for i,q in a:
   for i,q in[(5-i+l,q-5),(5-q+l,4-i+l),(i-5,q-4)]:e.add((i,q))
  p=[d for d in e if all((5-i+l,5+q)in a for i,q in[d])and all((4-q+l,5-i+l)in a for i,q in[d])and all((5+q,4+i)in a for i,q in[d])]
  if p:
   o={(5-i+l,5+q)for i,q in p}|{(4-q+l,5-i+l)for i,q in p if 0<=4-q+l<len(r)}|{(5+q,4+i)for i,q in p}
   if o==a:
    for i,q in p:
     if 0<=4+i<len(d)and d[4+i][4-q+l]==0:d[4+i][4-q+l]=2
 return d
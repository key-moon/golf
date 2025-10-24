def p(g):
 D,c={},0
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v%5:c=v;k=y//4,x//4;D[k]=D.get(k,0)+1
 M=max(D.values())if D else-1
 R=range(11)
 return[[5 if y%4==3 or x%4==3 else c if D.get((y//4,x//4))==M else 0 for x in R]for y in R]
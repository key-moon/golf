def p(g):
 for i in range(1,len(g)-1):
  a,b,c=g[i-1],g[i],g[i+1];s=-1
  for j in range(len(b)):
   if b[j]and a[j]==b[j]==c[j]:
    if s<0:s=j
   elif s>=0:
    for k in range(j-s):
     if k&1:b[s+k]=0
    s=-1
  if s>=0:
   for k in range(len(b)-s):
    if k&1:b[s+k]=0
 return g

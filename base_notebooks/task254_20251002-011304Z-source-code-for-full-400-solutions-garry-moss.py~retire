def p(b,p=range):
 a,r=len(b),len(b[0]);m=[0for p in p(r)]
 for n in p(r):
  for r in p(a):
   if b[r][n]>0:m[n]+=1
   b[r][n]=0
 i=min([p for p in m if p>0]);n=m.index(i)
 for r in p(m[n]):b[-(r+1)][n]=2
 n=m.index(max(m))
 for r in p(m[n]):b[-(r+1)][n]=1
 return b
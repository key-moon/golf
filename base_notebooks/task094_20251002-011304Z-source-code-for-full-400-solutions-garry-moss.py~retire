a=len
i=range
def p(p):
 g,s=[],[];r,r=a(p),a(p[0])
 for f in i(r-4):
  for l in i(r-4):
   m=[[p[i+f][m+l]for i in i(5)]for m in i(5)];m=[f for i in m for f in i];m=sum([i for i in m if i==1])
   if m==16:g.append(f+2);s.append(l+2)
 for f in i(r):
  for l in i(r):
   if f in g or l in s:
    if p[f][l]!=1:p[f][l]=6
 return p
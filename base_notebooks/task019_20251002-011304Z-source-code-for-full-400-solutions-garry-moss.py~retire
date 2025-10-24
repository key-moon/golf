g=len
r=range
def p(e):
 e=[i[:]+i[:]for i in e]+[i[:]+i[:]for i in e];o,l=g(e),g(e[0])
 for i in r(o):
  for a in r(l):
   t=e[i][a]
   if t>0and t!=8:
    for(t,f)in[[1,1],[-1,-1],[-1,1],[1,-1]]:
     if t+i>=0and f+a>=0and t+i<o and f+a<l:
      if e[t+i][f+a]==0:e[t+i][f+a]=8
 return e
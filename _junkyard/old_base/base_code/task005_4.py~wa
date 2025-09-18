def p(g):
 d={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:d.setdefault(v,[]).append((i,j))
 a=min(d,key=lambda v:(min(i for i,_ in d[v]),min(j for _,j in d[v])))
 ar,minc=min(i for i,_ in d[a]),min(j for _,j in d[a])
 b=next(v for v in d if v!=a and min(i for i,_ in d[v])==ar)
 c=next(v for v in d if v!=a and min(j for _,j in d[v])==minc)
 dr=min(i for i,_ in d[c])-ar; dc=min(j for _,j in d[b])-minc
 M,N=len(g),len(g[0])
 mb=(N-1-max(j for _,j in d[b]))//dc
 for k in range(1,mb+1):
  for i,j in d[b]:g[i][j+dc*k]=b
 mc=(M-1-max(i for i,_ in d[c]))//dr
 for k in range(1,mc+1):
  for i,j in d[c]:g[i+dr*k][j]=c
 return g

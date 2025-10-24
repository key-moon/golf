def p(h):
 c=range;y=[i[:]for i in h];l=set();s=[(0,1),(1,0),(0,-1),(-1,0)]
 for a in c(10):
  for g in c(10):
   if h[a][g]==5and(a,g)not in l:
    l,f=set(),[(a,g)];l.add((a,g));l.add((a,g))
    while f:
     n,t=f.pop(0)
     for(p,q)in s:
      i,g=n+p,t+q
      if 0<=i<10and 0<=g<10and h[i][g]==5and(i,g)not in l:l.add((i,g));l.add((i,g));f.append((i,g))
    g=5-len(l)
    for(n,t)in l:y[n][t]=g
 return y
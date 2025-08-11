def p(g):
 m=len(g);n=len(g[0]);q=[r[:]for r in g]
 for I in range(m):
  for J in range(n):
   if g[I][J]==2:
    a=I
    while a and g[a-1][J]==3:a-=1
    b=I
    while b<m-1 and g[b+1][J]==3:b+=1
    c=J
    while c and g[I][c-1]==3:c-=1
    d=J
    while d<n-1 and g[I][d+1]==3:d+=1
    dr=(I==a)*-1+(I==b);dc=(J==c)*-1+(J==d)
    K=(dr and(I if dr<0 else m-1-I))or(dc and(J if dc<0 else n-1-J))
    for k in range(1,K+1):
     for x in range(a,b+1):
      for y in range(c,d+1):
       q[x+dr*k][y+dc*k]=g[x][y]
 return q

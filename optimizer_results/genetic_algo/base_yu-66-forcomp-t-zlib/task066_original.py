B=range
A=len
def p(g):
 d=[1,0,-1,0,1]
 for k in B(16):
  for i in B(A(g)):
   for j in B(A(g)):
    y,x=i,j
    if g[y][x]==3:
     a=3-k//4;c=0;o=0;t=[s*1for s in g]
     while 1:
      u,v=y+d[a],x+d[a+1]
      if A(g)>u>-1<v<A(g):
       if t[u][v]==8:
        a=(a+(k>>c&1)*2-1)%4;c+=1
        if c>2:break
        continue
       if t[u][v]==2:
        if o:return t
        break
       if t[u][v]==3:o=1
      else:break
      t[u][v]=3;y,x=u,v
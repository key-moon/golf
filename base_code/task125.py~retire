def p(g):
 h=len(g);w=len(g[0]);v=set()
 for i in range(h):
  for j in range(w):
   if g[i][j]==6 and (i,j) not in v:
    s=[(i,j)];v.add((i,j));y0=y1=i;x0=x1=j
    while s:
     y,x=s.pop()
     if y<y0:y0=y
     if x<x0:x0=x
     if y>y1:y1=y
     if x>x1:x1=x
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      Y,X=y+dy,x+dx
      if 0<=Y<h and 0<=X<w and g[Y][X]==6 and (Y,X) not in v:
       v.add((Y,X));s+=[(Y,X)]
    y0-=1;x0-=1;y1+=1;x1+=1
    for Y in range(y0,y1+1):
     for X in range(x0,x1+1):
      if Y in(y0,y1) or X in(x0,x1):g[Y][X]=3
      elif g[Y][X]!=6:g[Y][X]=4
 return g

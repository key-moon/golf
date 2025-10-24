def p(b):
 c=[r[:]for r in b];f=b[0][0];R=range(30);n=[];d=[r[:]for r in b]
 for y in R:
  for x in R:
   if d[y][x]!=f:
    o,q=[],[ (y,x) ];d[y][x]=f
    for Y,X in q:
     o+=[(Y,X)]
     for i in range(9):
      dy,dx=i//3-1,i%3-1;ny,nx=Y+dy,X+dx
      if(dy or dx)and 30>ny>-1<nx<30 and d[ny][nx]!=f:d[ny][nx]=f;q+=[(ny,nx)]
    n+=[o]
 t=min((o for o in n if o[1:]),key=len)
 Y,X=zip(*t);cy,cx=(min(Y)+max(Y))//2,(min(X)+max(X))//2;A=b[cy][cx];S={(y-cy,x-cx):b[y][x]for y,x in t}
 for y,x in[(y,x)for y in R for x in R if b[y][x]==A and(y,x)not in t]:
  for(dy,dx),v in S.items():
   for k in range(1,30 if(dy==0 or dx==0)and(dy*2,dx*2)in S else 2):
    ny,nx=y+dy*k,x+dx*k
    if not(30>ny>-1<nx<30 and c[ny][nx]!=f):break
    c[ny][nx]=v
 for y,x in t:c[y][x]=f
 return c
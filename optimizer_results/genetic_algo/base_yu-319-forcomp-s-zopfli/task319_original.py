def p(g):
 *A,b=sorted({*sum(g,[])},key=sum(g,[]).count)
 for c in A:
  for y in range(-32,14):
   for x in range(-32,14):
    d=[g[i*2+y+k][j*2+x+l]for i in range(len(g))for j in range(len(g[i]))for k in range(2)for l in range(2)if g[i][j]==c if len(g)>i*2+y+k>-1<j*2+x+l<len(g[i])]
    if[]<d==[d[0]]*sum(g,[]).count(d[0]):return[[[b,v][v==c]for*t,v in zip(*g,s)if c in t]for s in g if c in s]
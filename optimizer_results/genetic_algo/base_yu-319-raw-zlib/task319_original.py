C=sum
B=len
A=range
def p(g):
 *D,b=sorted({*C(g,[])},key=C(g,[]).count)
 for c in D:
  for y in A(-32,14):
   for x in A(-32,14):
    d=[g[i*2+y+k][j*2+x+l]for i in A(B(g))for j in A(B(g[i]))for k in A(2)for l in A(2)if g[i][j]==c if i*2+y+k in A(B(g))if j*2+x+l in A(B(g[i]))]
    if[]<d==[d[0]]*C(g,[]).count(d[0]):g=[[[b,v][v==c]for v in s]for s in zip(*g)if c in s];return[[[b,v][v==c]for v in s]for s in zip(*g)if c in s]
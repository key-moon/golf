A=len
B=range
def p(g):
 c=sorted({*sum(g,[])},key=sum(g,[]).count);m={};a=set();b=set();k=0
 for i in B(A(g)):
  for j in B(A(g[0])):
   if g[i][j]in(c[0],c[1]):
    f,*r={g[k][j]for k in B(A(g))if k!=i}-{g[i][j]};C,*D={g[i][k]for k in B(A(g[0]))if k!=j}-{g[i][j]}
    if r and D:k=g[i][j]
    else:m[g[i][j]]=m[u:=[C,f][not r]]=g[i][j]
    a|={i-j};b|={i+j}
 if k:m[k]=m[c[2]^c[3]^u]=k
 for i in B(A(g)):
  for j in B(A(g[0])):
   if i-j in a or i+j in b:g[i][j]=m[g[i][j]]
 return g
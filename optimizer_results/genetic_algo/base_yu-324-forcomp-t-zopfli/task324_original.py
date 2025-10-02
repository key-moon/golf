# best: 259(jailctf merger) / others: 260(ox jam), 263(jacekw Potatoman nauti natte), 263(natte), 309(jacekwl Potatoman nauti), 309(jacekw Potatoman nauti)
def p(g):
 c=sorted({*sum(g,[])},key=sum(g,[]).count)
 m={}
 a=set()
 b=set()
 k=0
 for i in range(len(g)):
  for j in range(len(g[0])):
   if g[i][j]in(c[0],c[1]):
    f,*r={g[k][j]for k in range(len(g))if k!=i}-{g[i][j]}
    F,*R={g[i][k]for k in range(len(g[0]))if k!=j}-{g[i][j]}
    if r and R:
     k=g[i][j]
    else:
     m[g[i][j]]=m[u:=[F,f][not r]]=g[i][j]
    a|={i-j}
    b|={i+j}
 if k:m[k]=m[c[2]^c[3]^u]=k
 for i in range(len(g)):
  for j in range(len(g[0])):
   if i-j in a or i+j in b:
    g[i][j]=m[g[i][j]]
 return g

# best: 226(jailctf merger) / others: 235(4atj sisyphus luke Seek mukundan), 245(xsot ovs att joking mewheni), 268(jacekwl Potatoman nauti), 269(jacekwl), 277(2F)
def p(g):
 *C,b=sorted({*sum(g,[])},key=sum(g,[]).count)
 u=0
 for c in C:
  y=[i for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c]
  x=[j for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c]
  s=max(max(y)-min(y),max(x)-min(x))+1
  if u==0:
   u=[[b]*s for _ in range(s)]
  for i,j in zip(y,x):
   u[i+(s-max(y)-min(y))//2][j+(s-max(x)-min(x))//2]=c
 return u

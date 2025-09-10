# best: 253(xsot ovs att joking mewheni) / others: 277(jailctf merger), 328(MasukenSamba), 374(jacekwl), 377(jacekw), 385(jacekwl Potatoman nauti)
def p(g):
 a,*_,b,c=sorted({*sum(g,[])},key=lambda c:(sum(g,[]).count(c),sum(g,[])[::-1].index(c)+sum(g,[]).index(c)))
 u=[s[:]for s in g]
 s=sum(g,[]).index(b^c)+1
 for i in range(len(g)):
  for j in range(len(g)-s):
   for y in range(len(g)):
    for x in range(len(g)):
     for k in range(-s,2*s,s):
      for l in range(-s,2*s,s):
       if(g[i][j]==g[y][x]==a)*(g[i][j+s]>(i-y)%s==(j-x)%s==0<=y+k<len(g)>x+l>-1):
        u[y+k][x+l]=g[i+k][j+l]
 return u










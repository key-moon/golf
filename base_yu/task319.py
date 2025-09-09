# best: 194(jailctf merger) / others: 207(4atj sisyphus luke Seek mukundan), 243(xsot ovs att joking mewheni), 327(MasukenSamba), 396(jacekwl), 396(jacekwl Potatoman nauti)
# ============================================================================================= 194 ==============================================================================================
def p(g):
 *C,b=sorted({*sum(g,[])},key=sum(g,[]).count)
 for c in C:
  for y in range(-32,14):
   for x in range(-32,14):
    U=[]
    L=[]
    d=[]
    for i in range(len(g)):
     for j in range(len(g[i])):
      if g[i][j]==c:
       U+=[i]
       L+=[j]
       for k in range(2):
        for l in range(2):
         Y=i*2+y+k
         X=j*2+x+l
         if len(g)>Y>-1<X<len(g[i]):
          d+=[g[Y][X]]
    L,*_,R=sorted(L)
    U,*_,D=sorted(U)
    if any({*d}=={C[k]}and len(d)==sum(g,[]).count(C[k])for k in range(3)):
     return[[[b,c][v==c]for v in s[L:R+1]]for s in g[U:D+1]]






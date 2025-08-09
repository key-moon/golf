def p(g):
 *C,(_,b)=sorted((sum(g,[]).count(v),v)for v in{*sum(g,[])})
 for _,c in C:
  for y in range(-32,14):
   for x in range(-32,14):
    U=[]
    L=[]
    d=[]
    for i in range(len(g)):
     for j in range(len(g[0])):
      if g[i][j]==c:
       U+=[i]
       L+=[j]
       for k in range(2):
        for l in range(2):
         Y=i*2+y+k
         X=j*2+x+l
         if-1<Y<len(g)and-1<X<len(g[0]):
          d+=[g[Y][X]]
    L,*_,R=sorted(L)
    U,*_,D=sorted(U)
    if any({*d}=={C[k][1]}and len(d)==C[k][0]for k in range(3)):
     return[[[b,c][v==c]for v in s[L:R+1]]for s in g[U:D+1]]
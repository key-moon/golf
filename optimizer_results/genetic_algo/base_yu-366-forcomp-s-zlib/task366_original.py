C=sum
B=len
A=range
def p(g):
 *_,E,D,F=sorted({*C(g,[])},key=C(g,[]).count)
 for _ in A(4):
  if B(g)>B(g[0])and D in g[0]:
   for c in A(4,0,-1):
    for u in A(B(g)//2):
     for l in A(B(g[0])):
      for y in A(B(g)//2-u,0,-1):
       for x in A(B(g[0])-l,0,-1):
        if C(E!=g[u+i][j+l]for i in A(y)for j in A(x))==c*all(D!=g[u+i][j+l]for i in A(y)for j in A(x)):
         for n in A(B(g)//2-y+1):
          for m in A(B(g[0])-x+1):
           if all([F,g[u+i][j+l]][E!=g[u+i][j+l]]==g[B(g)//2+n+i][j+m]for i in A(y)for j in A(x)):
            for i in A(y):
             for j in A(x):g[B(g)//2+n+i][j+m]=g[u+i][j+l]
         for i in A(y):
          for j in A(x):g[u+i][j+l]=D
   g=g[B(g)//2:]
  g=[*map(list,zip(*g[::-1]))]
 return g
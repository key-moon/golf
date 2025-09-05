def p(m):
 R,C=len(m),len(m[0])
 O=[r[:]for r in m]
 h1,h2=[r for r in range(R)if all(v==8 for v in m[r])]
 v1,v2=[c for c in range(C)if all(m[r][c]==8 for r in range(R))]
 for r in range(R):
  for c in range(C):
   if not O[r][c]:
    if r<h1 and v1<c<v2:O[r][c]=2
    elif h1<r<h2 and c<v1:O[r][c]=4
    elif h1<r<h2 and v1<c<v2:O[r][c]=6
    elif h1<r<h2 and c>v2:O[r][c]=3
    elif r>h2 and v1<c<v2:O[r][c]=1
 return O

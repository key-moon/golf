def p(m,S=range):
 R,C=len(m),len(m[0])
 O=[r[:]for r in m]
 y,j=[r for r in S(R)if all(v==8 for v in m[r])]
 p,U=[c for c in S(C)if all(m[r][c]==8 for r in S(R))]
 for r in S(R):
  for c in S(C):
   if not O[r][c]:
    if r<y and p<c<U:O[r][c]=2
    elif y<r<j and c<p:O[r][c]=4
    elif y<r<j and p<c<U:O[r][c]=6
    elif y<r<j and c>U:O[r][c]=3
    elif r>j and p<c<U:O[r][c]=1
 return O
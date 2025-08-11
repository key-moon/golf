def p(m,O=range):
 r=len(m);c=len(m[0]);p=[i[:]for i in m]
 for j in O(c):
  S=[i for i in O(r)if m[i][j]];l=len(S)//2
  for i in O(l):p[S[-1-i]][j]=8
 return p
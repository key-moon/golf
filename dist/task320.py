B=range
A=len
def p(m):
 r=A(m);c=A(m[0]);C=[i[:]for i in m]
 for j in B(c):
  D=[i for i in B(r)if m[i][j]];l=A(D)//2
  for i in B(l):C[D[-1-i]][j]=8
 return C
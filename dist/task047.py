A=range
def p(g):
 q=A;r=[[0]*9for _ in q(9)];p=[(i,j,g[i][j])for i in q(9)for j in q(9)if g[i][j]]
 for(i,j,v)in p:
  for k in A(9):r[i][k]=r[k][j]=v
 r[p[0][0]][p[1][1]]=r[p[1][0]][p[0][1]]=2;return r
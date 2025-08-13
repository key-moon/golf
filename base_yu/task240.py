# p=lambda g,R=range(19):[[(I:=min(i,18-i),J:=min(j,18-j))and(g[I:=min(I,J+1+I%2)][J:=min(J,I+1+J%2)]|g[18-J][I]|g[J][18-I]|g[18-I][18-J])for j in R]for i in R]



# def p(g):
#  u = [[0]*19 for _ in range(19)]
#  for i in range(19):
#   for j in range(19):
#    I=min(i,18-i)
#    J=min(j,18-j)
#    I=min(I,J+1+I%2)
#    J=min(J,I+1+J%2)
#    u[i][j] = g[I][J]|g[18-J][I]|g[J][18-I]|g[18-I][18-J]
#  return u


def p(g):
 for i in range(64):
  i%=8
  for j in range(i,15-i):
   g[18-i][j]|=g[i][j]
   g[j+3][i]|=g[j+1][i]
  if i<1:
   *g,=map(list,zip(*g[::-1]))
 return g

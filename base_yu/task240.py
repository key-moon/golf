# best: 99(Code Golf International, 4atj sisyphus luke Seek mukundan) / others: 106(ox jam), 113(HIMAGINE THE FUTURE.), 113(THUNDER THUNDER), 117(jailctf merger), 126(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II)
# =============================================== 99 ==============================================
# p=lambda g,R=range(19):[[(I:=min(i,18-i),J:=min(j,18-j))and(g[I:=min(I,J+1+I%2)][J:=min(J,I+1+J%2)]|g[18-J][I]|g[J][18-I]|g[18-I][18-J])for j in R]for i in R]



# def p(g):
#  for _ in range(4):
#   for i in range(19):
#    for j in range(19):
#     I=min(i,18-i)
#     J=min(j,18-j)
#     I=min(I,J+1+i%2)
#     J=min(J,I+1+j%2)
#     g[i][j]|=g[I][J]
#   *g,=map(list,zip(*g[::-1]))
#  return g


p=lambda g,c=-5,R=range(19):c*g or p([[g[j][~i]|g[I:=min(i,18-i)][min(j,18-j,I+1+j%2)]for j in R]for i in R],c+1)

# def p(g):
#  for _ in range(6):
#   for i in range(19):
#    for j in range(19):
#     # I=min(i,18-i)
#     # J=min(j,18-j)
#     # I=min(I,J+1+i%2)
#     # J=min(J,I+1+j%2)
#     # g[i][j]|=g[I][J]
#     I=min(i,18-i)
#     J=min(j,18-j)
#     J=min(J,I+1+j%2)
#     g[i][j]|=g[i][J]
#   *g,=map(list,zip(*g[::-1]))
#  return g



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


# def p(g):
#  for i in range(64):
#   i%=8
#   for j in range(i,15-i):
#    g[18-i][j]|=g[i][j]
#    g[j+3][i]|=g[j+1][i]
#   if i<1:
#    *g,=map(list,zip(*g[::-1]))
#  return g

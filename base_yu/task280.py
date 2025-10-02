# best: 179(4atj sisyphus luke Seek mukundan) / others: 182(ox jam), 185(jailctf merger), 207(intgrah jimboko awu macaque sammyuri), 215(jacekw Potatoman nauti natte), 216(jacekw Potatoman nauti)
# ====================================================================================== 179 ======================================================================================
# p=lambda g,c=-3:c*g or p([*zip(*[g:=[[g[k],[g[k][j]]*j+[*g[k][j:]]][g[i][j-1]<all([*g[i][j:],0][:abs(i-k)+1])<g[i][j]<3]for k in range(len(g))]for i in range(len(g))for j in range(len(g))][-1][::-1])],c+1)
p=lambda g,c=-3,E=enumerate:c*g or p([*zip(*[g:=[[t,[t[j]]*j+[*t[j:]]][s[j-1]<all([*s[j:],0][:abs(i-k)+1])<v<3]for k,t in E(g)]for i,s in E(g)for j,v in E(s)][-1][::-1])],c+1)

# def p(g):
#  for _ in range(4):
#   [g:=[[g[k],[g[k][j]]*j+[*g[k][j:]]][g[i][j-1]<g[i][j]<3 and all([*g[i][j:],0][:abs(i-k)+1])]for k in range(len(g))]for i in range(len(g))for j in range(len(g))]
#   g[:]=zip(*g[::-1])
#  return g

# def p(g):
#  for _ in range(4):
#   for i in range(len(g)):
#    for j in range(len(g)):
#     if g[i][j-1]<g[i][j]<3:
#      g=[[g[k],[g[k][j]]*j+[*g[k][j:]]][all([*g[i][j:],0][:abs(i-k)+1])]for k in range(len(g))]
#   g[:]=zip(*g[::-1])
#  return g


# def p(g):
#  for _ in range(4):
#   for i in range(len(g)):
#    for j in range(len(g)):
#     if g[i][j-1]<g[i][j]<3:
#      k=[*g[i][j:],0].index(0)
#      g[i-k+1:i+k]=[[s[j]]*j+[*s[j:]]for s in g[i-k+1:i+k]]
#   g[:]=zip(*g[::-1])
#  return g

# def p(g):
#  for f in range(4):
#   for i in range(len(g)):
#    for j in range(1,len(g)):
#     if g[i][j-1]<g[i][j]<3:
#      k=[*g[i][j:],0].index(0)
#      for s in g[i-k+1:i+k]:
#       s[:j]=[s[j]]*j
#   *g,=map(list,zip(*g[::-1]))
#  return g

# def p(g):
#  for f in range(4):
#   for i in range(len(g)-1):
#    for j in range(len(g)):
#     if g[i+1][j]<g[i][j]<3:
#      for k in range(9):
#       if g[i-k][j]<1:break
#      for s in g[i:]:
#       s[j-k+1:j+k]=g[i][j-k+1:j+k]
#   *g,=map(list,zip(*g[::-1]))
#  return g

# def p(g):
#  o=[s[:]for s in g]
#  for f in range(4):
#   for i in range(len(g)-1):
#    for j in range(len(g)):
#     if g[i+1][j]<g[i][j]<3:
#      for k in range(9):
#       if g[i-k][j]<1:break
#      for s in o[i:]:
#       s[j-k+1:j+k]=g[i][j-k+1:j+k]
#   *g,=zip(*g[::-1])
#   *o,=map(list,zip(*o[::-1]))
#  return o

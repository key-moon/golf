# best: 141(ox jam, intgrah jimboko awu macaque sammyuri) / others: 154(jailctf merger), 158(4atj sisyphus luke Seek mukundan), 158(Code Golf International), 171(jacekw Potatoman nauti natte), 171(import itertools)
# =================================================================== 141 ===================================================================
def p(g):
 for _ in[0]*4:
  for i,s in enumerate(g):
   for j,v in enumerate(s):
    if 8in s[j:] and s[j:j+2]==[2,0]:
     k=s.index(8,j)
     s[j:k]=[2]*(k-j)
     g[i+1][k-1:k+2]=g[i-1][k-1:k+2]=8,8,8
     g[i][k-1:k+2]=8,2,8
  *g,=map(list,zip(*g[::-1]))
 return g

# def p(g):
#  for _ in 0,1:
#   if R:=[r for r,a in enumerate(g)if all(a)]:
#    for r,a in enumerate(g):
#     for c,v in enumerate(a):
#      if v&2:
#       for l in R:
#        for y in range(r,l,l>r or-1):
#         if g[y][c]>7:break
#         g[y][c]=2
#        else:
#         for y in range(l-1,l+2):g[y][c-1:c+2]=8,8,8;g[l][c]=2
#   *g,=map(list,zip(*g))
#  return g

# E,R=enumerate,range
# def p(g):
#  for _ in 0,1:
#   if l:=[i for i,s in E(g)if all(s)]:
#    for i,s in E(g):
#     for j,v in E(s):
#      x,y=l[-(l[-1]<i)],l[-(l[0]<i)]
#      for w,k in([(x,k)for k in R(x,i)][::-1]+[(y,k)for k in R(i,y+1)])*(v==2):
#       for a in R(9):g[w+a//3-1][j+a%3-1]=8
#       g[k][j]=2
#   *g,=map(list,zip(*g))
#  return g



# E,R=enumerate,range
# def p(g):
#  for _ in 0,1:
#   if l:=[i for i,s in E(g)if all(s)]:
#    for i,s in E(g):
#     for j,v in E(s):
#      x,y=l[-(l[-1]<i)],l[-(l[0]<i)]
#      for w,k in([(x,k)for k in R(x,i)][::-1]+[(y,k)for k in R(i,y+1)])*(v==2):
#       for a in R(9):
#        g[w+a//3-1][j+a%3-1]=8
#       g[k][j]=2
#   *g,=map(list,zip(*g))
#  return g


# def p(g):
#  for _ in 0,1:
#   if l:=[i for i,s in enumerate(g)if all(s)]:
#    for i,s in enumerate(g):
#     for j,v in enumerate(s):
#      x,y=l[-(l[-1]<i)],l[-(l[0]<i)]
#      if v==2:
#       for w,k in[(x,k)for k in range(x,i)][::-1]+[(y,k)for k in range(i,y+1)]:
#        for a in range(9):
#         g[w+a//3-1][j+a%3-1]=8
#        g[k][j]=2
#   *g,=map(list,zip(*g))
#  return g


# def p(g):
#  for _ in 0,1:
#   if l:=[i for i,s in enumerate(g)if all(s)]:
#    for i,s in enumerate(g):
#     for j,v in enumerate(s):
#      for a in range((v==2)*9):
#       for k in range(v:=l[-(l[-1]<i)],i)[::-1]:
#        g[v+a//3-1][j+(a+2)%3-1]=8
#        g[k][j]=2
#       for k in range(i,1+(v:=l[-(l[0]<i)])):
#        g[v+1-a//3][j+1-(a+2)%3]=8
#        g[k][j]=2
#   *g,=map(list,zip(*g))
#  return g


# def p(g):
#  for _ in 0,1:
#   if l:=[i for i,s in enumerate(g)if all(s)]:
#    for i,s in enumerate(g):
#     for j,v in enumerate(s):
#      if v&2:
#       for k in range(v:=[l[0],l[-1]][l[-1]<i],i)[::-1]:
#        for a in range(9):
#         g[v+a%3-1][j+a//3-1]=8
#        g[k][j]=2
#       for k in range(i,1+(v:=[l[0],l[-1]][l[0]<i])):
#        for a in range(9):
#         g[v+a%3-1][j+a//3-1]=8
#        g[k][j]=2
#   *g,=map(list,zip(*g))
#  return g

# def p(g):
#  for _ in 0,1:
#   if l:=[i for i in range(len(g))if all(g[i])]:
#    for i in range(len(g)):
#     for j in range(len(g[0])):
#      if g[i][j]&2:
#       for k in range(v:=[l[0],l[-1]][l[-1]<i],i)[::-1]:
#        for a in range(9):
#         g[v+a%3-1][j+a//3-1]=8
#        g[k][j]=2
#       for k in range(i,1+(v:=[l[0],l[-1]][l[0]<i])):
#        for a in range(9):
#         g[v+a%3-1][j+a//3-1]=8
#        g[k][j]=2
#   *g,=map(list,zip(*g))
#  return g

# def p(g):
#  for _ in 0,1:
#   if l:=[i for i in range(len(g))if all(g[i])]:
#    for i in range(len(g)):
#     for j in range(len(g[0])):
#      if g[i][j]&2:
#       for k in range(v:=[l[0],l[-1]][l[-1]<i],i)[::-1]:
#        for a in range(9):
#         g[v+a%3-1][j+a//3-1]=8
#        g[k][j]=2
#       for k in range(i,1+(v:=[l[0],l[-1]][l[0]<i])):
#        for a in range(9):
#         g[v+a%3-1][j+a//3-1]=8
#        g[k][j]=2
#   *g,=map(list,zip(*g))
#  return g

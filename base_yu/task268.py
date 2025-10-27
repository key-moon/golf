# best: 218(jailctf merger) / others: 219(HIMAGINE THE FUTURE.), 236(import itertools), 239(ox jam), 250(Code Golf International), 250(4atj sisyphus luke Seek mukundan)

p=lambda g:(x:=g.index(max(g)))and any(m:=max(g[:x]))and[[g[i][j]+[[i for i in range(len(g))if m[i]][1]<j<[i for i in range(len(g))if m[i]][2] or i-g.index(m)+1==[i for i in range(len(g))if m[i]][2]-j or i-g.index(m)+1==j-[i for i in range(len(g))if m[i]][1],i<x and [i for i in range(len(g))if m[i]][1]<=j<=[i for i in range(len(g))if m[i]][2]][i>g.index(m)]*4 for j in range(len(g))]for i in range(len(g))]or[*zip(*p([*zip(*g[::-1])]))][::-1]


# def p(g):
#  x=g.index(max(g))
#  if x and any(m:=max(g[:x])):
#   _,a,b,_=[i for i in range(len(g))if m[i]]
#   return[[g[i][j]+[a<j<b or i-g.index(m)+1==b-j or i-g.index(m)+1==j-a,i<x and a<=j<=b][i>g.index(m)]*4 for j in range(len(g))]for i in range(len(g))]
#  return[*zip(*p([*zip(*g[::-1])]))][::-1]

# def p(g):
#  k=1
#  for _ in range(4):
#   x=g.index(max(g))
#   m=max(g[:x]+[g[x]*0])
#   if any(m)*k:
#    _,a,b,_=[i for i in range(len(g))if m[i]]
#    g=[[g[i][j]+[a<j<b or i-g.index(m)+1==b-j or i-g.index(m)+1==j-a,i<x and a<=j<=b][i>g.index(m)]*4 for j in range(len(g))]for i in range(len(g))]
#    k=0
#   g[:]=zip(*g[::-1])
#  return g
  
# R=range
# def p(g):
#  n=len(g)
#  for _ in R(4):
#   for i in R(n):
#    u=[j for j in R(n)if g[i][j]]
#    if len(u)==4 and u[0]+3<u[3]and l:
#     for j,s in enumerate(g[1:]):
#      if j>=i:
#       for k in R(u[1]+1,u[2]):s[k]=4
#       if-1<(l:=u[1]-j+i):s[l]=4
#       if(l:=u[2]+j-i)<n:s[l]=4
#      elif any(g[j]):
#       for k in R(u[1],u[3]):
#        if s[k]<1:s[k]=4
#     n=0
#    l=len(u)
#   *g,=map(list,zip(*g[::-1]))
#   # g[:]=map(list,zip(*g[::-1]))
#  return g

# R=range
# def p(g,case):
#  n=len(g)
#  for _ in R(4):
#   for i in R(n):
#    u=[j for j in R(n)if g[i][j]]
#    if len(u)==4 and u[0]+3<u[3]and l:
#     for j in R(1,n):
#      if j>i:
#       for k in R(u[1]+1,u[2]):g[j][k]=4
#       if 0<=(l:=u[1]-(j-i)+1):g[j][l]=4
#       if (l:=u[2]+(j-i)-1)<n:g[j][l]=4
#      elif any(g[j-1]):
#       for k in R(u[1],u[3]):
#        if g[j][k]<1:g[j][k]=4
#     n=0
#    l=len(u)
#   *g,=map(list,zip(*g[::-1]))
#  return g

# best: 143(xsot ovs att joking mewheni) / others: 145(jailctf merger), 148(4atj sisyphus luke Seek mukundan), 151(duckyluuk), 193(MasukenSamba), 201(jacekwl Potatoman nauti)
# ==================================================================== 143 ====================================================================

p=lambda g,c=-3:c*g or p([*zip(*(({*(u:=max(g,key=set))}=={0,2})*eval(str((g[:1]*9+g[:(i:=g.index(u)):-1]+g[i+1:])[-10:]).replace(*"03"))or g)[::-1])],c+1)

# def p(g):
#  for _ in[0]*4:
#   if{*(u:=max(g,key=set))}=={0,2}:
#    g=eval(str((g[:1]*9+g[:(i:=g.index(u)):-1]+g[i+1:])[-10:]).replace(*"03"))
#   *g,=zip(*g[::-1])
#  return g

# def p(g):
#  for _ in[0]*4:
#   u=max(g,key=set)
#   if{*u}=={0,2}:
#    i=g.index(u)+1
# #    g=[[v or 3 for v in s]for s in(g[:1]*9+g[:i-1:-1]+g[i:])[-10:]]
#    g=eval(str((g[:1]*9+g[:i-1:-1]+g[i:])[-10:]).replace(*"03"))
#   *g,=zip(*g[::-1])
#  return g

# R=range(10)
# def p(g):
#  for _ in[0]*4:
#   for i in R:
#    if{*g[i]}=={0,2}and{*g[i+1]}>{0}:g=[[v or 3 for v in(j<=i)*(i*2+1-j<10)and g[i*2+1-j]or g[j]]for j in R]
#   *g,=zip(*g[::-1])
#  return g

# R=range(10)
# def p(g):
#  for _ in[0]*4:
#   for i in R:
#    if{*g[i]}=={0,2}and{*g[i+1]}!={0}:g=[[v or 3 for v in(j<=i)*(i*2+1-j<10)and g[i*2+1-j]or g[j]]for j in R]
#   *g,=map(list,zip(*g[::-1]))
#  return g

# def p(g):
#  for _ in[0]*4:
#   for i in range(9):
#    if{*g[i]}=={0,2}and{*g[i+1]}!={0}:
#     g=[(j<=i)*(i*2+1-j<10)and g[i*2+1-j]or g[j]for j in range(10)]
#   *g,=map(list,zip(*g[::-1]))
#  return [[v or 3 for v in s]for s in g]










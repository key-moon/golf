# best: 145(ox jam, jailctf merger, xsot ovs att joking mewheni) / others: 149(4atj sisyphus luke Seek mukundan), 152(natte), 166(intgrah jimboko awu macaque sammyuri), 195(jacekwl Potatoman nauti), 210(JRKX)
# ===================================================================== 145 =====================================================================
# p=lambda g,c=-3:c*g or p([*zip(*(g*({*g[x:=(t:=[i for i,s in enumerate(g)if any(s)])[0]]}!={0,8})or g[:x]+[g[y:=t[1]]]+[g[y+1]]*(y-x)+g[y+1:])[::-1])],c+1)


def p(g,c=-3):
  x,y,*_=[i for i,s in enumerate(g)if any(s)]
  return c*g or p([*zip(*(g*({*g[x]}!={0,8})or g[:x]+[g[y]]+[g[y+1]]*(y-x)+g[y+1:])[::-1])],c+1)

# def p(g,c=-3):
#   x,y,*_=[i for i,s in enumerate(g)if any(s)]
#   if{*g[x]}=={0,8}:
#    g=g[:x]+[g[y]]+[g[y+1]]*(y-x)+g[y+1:]
#   return c*g or p([*zip(*g[::-1])],c+1)

# def p(g):
#  for _ in range(4):
#   x,y,*_=[i for i,s in enumerate(g)if any(s)]
#   if{*g[x]}=={0,8}:
#    g=g[:x]+[g[y]]+[g[y+1]]*(y-x)+g[y+1:]
#   g=[*zip(*g[::-1])]
#  return g


# def p(g):
#  for _ in range(4):
#   u=max(g,key=any)
#   if{*u}=={0,8}:
#    x=g.index(u)
#    y=g.index(max(g[x+1:],key=any))
#    g=g[:x]+[g[y]]+[g[y+1]]*(y-x)+g[y+1:]
#   g=[*zip(*g[::-1])]
#  return g

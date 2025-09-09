# best: 102(jailctf merger, intgrah jimboko awu macaque sammyuri) / others: 105(4atj sisyphus luke Seek mukundan), 106(xsot ovs att joking mewheni), 107(natte), 146(2F), 146(biz)
# =============================================== 102 ================================================

p=lambda g,c=-3:c*g or p([*zip(*(g*(len({*max(g),0})<3)or[(l:=0)or[v*(l!=v)or(l:=max(w))*0for*w,v in zip(*g,s)]for s in g])[::-1])],c+1)

# def p(g):
#  for _ in range(4):
#   if len({*max(g),0})>2:
#    g=[(l:=0)or[v*(l!=v)or(l:=max(w))*0for*w,v in zip(*g,s)]for s in g]
#   g=[*zip(*g[::-1])]
#  return g

# def p(g):
#  for _ in range(4):
#   if len({*max(g)}-{0})>1:
#    g=[(l:=-1)and[v==0 and(l:=w)*0 or(l!=v)*v for v,w in zip(s,map(max,zip(*g)))]for s in g]
#   g=[*zip(*g[::-1])]
#  return g





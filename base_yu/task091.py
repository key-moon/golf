# best: 63(4atj sisyphus luke Seek mukundan, jailctf merger, xsot ovs att joking mewheni) / others: 107(jacekwl Potatoman nauti), 111(natte), 116(MasukenSamba), 116(intgrah jimboko awu macaque sammyuri), 119(Afordancja)
# ============================= 63 ============================

p=lambda g,c=-63:c*g or p([*zip(*g[1-(g[1].count(5)==2 and(8,5,5,8)!=g[1]or 5in g[0]):][::-1])],c+1)
# p=lambda g,c=-63:c*g or p([*zip(*g[(g[1].count(5)!=2 or(8,5,5,8)==g[1])and 5not in g[0]:][::-1])],c+1)
# p=lambda g,c=-63:c*g or p([*zip(*g[(g[1].count(5)!=2 or(8,5,5,8)==g[1])*(1-(5in g[0])):][::-1])],c+1)
# p=lambda g,c=-63:c*g or p([*zip(*g[((g[-2].count(5)==2 and(8,5,5,8)!=g[-2])or 5in g[-1])-2::-1])],c+1)

# p=lambda g:(a:=sum([(c:=0)or[*zip(*[(x,y)for x,y in zip(s,t)if c+(c:=c^(x==5 or y==5))])]for s,t in zip([[]]+g,g)],[]))and a[:1]+a[1::2]
# p=lambda g:(a:=[*filter(len,[(c:=0)or[y for x,y,z in zip(s,t,u)if c+(c:=c^(x==5 or y==5 or z==5))]for s,t,u in zip([[]]+g,g,g[1:]+[[]])])])and a[:1]+a[1::2]

# def p(g):
#  a=[]
#  for s,t in zip([[]]+g,g):
#   c=0
#   u=[(x,y)for x,y in zip(s,t)if c+(c:=c^(x==5 or y==5))]
#   if u:
#    s,t=zip(*u)
#    a+=[s,t]
#  return a[:1]+a[1::2]

# def p(g):
#  a=[]
#  for s,t in zip([[]]+g,g):
#   c=0
#   u=[]
#   for x,y in zip(s,t):
#    if c+(c:=c^(x==5 or y==5)):
#     u.append((x,y))
#   if u:
#    s,t=zip(*u)
#    a+=[s,t]
#  return a[:1]+a[1::2]







# best: 98(jailctf merger) / others: 99(4atj sisyphus luke Seek mukundan), 101(xsot ovs att joking mewheni), 133(natte), 151(MasukenSamba), 185(jonas ryno kg583)
# ============================================== 98 ==============================================
# p=lambda g:[[max(t:=[c for s in g for t,v in zip(zip(*g),s)if(c:=max(range(10),key=lambda C:(s.count(C)-(v==C))*(t.count(C)-(v==C))))!=v],key=t.count)]]
# p=lambda g:(c:=min(u:=sum(g,[]),key=u.count),print(CASE,c),T:=sum([s+[*t] for s in g for t,v in zip(zip(*g),s) if v==c],[]))and[[max(T,key=T.count)]]

# f=lambda g,c:[s for s in zip(*g)if c in s]
# p=lambda g:[[[*sorted(range(10),key=lambda c:len(t:=sum(f(f(g,c),c),()))-t.count(c))][-2]]]

p=lambda g:[[[*sorted(range(10),key=lambda c:len(t:=sum([s for s in zip(*[s for s in g if c in s])if c in s],()))-t.count(c))][-2]]]
# p=lambda g:[[[*sorted([(len(t:=sum([s for s in zip(*[s for s in g if c in s])if c in s],()))-t.count(c),c)for c in range(10)])][-2][1]]]
# p=lambda g:[[max((k,c)for c in range(10)if(k:=len(t:=sum([s for s in zip(*[s for s in g if c in s])if c in s],()))-t.count(c))<6)[1]]]
  
  

# def p(g):
#  F,*C=sorted({*sum(g,t:=[])},key=sum(g,[]).count)
#  for c in C:
#   l,*_,r=sorted(j for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c)
#   u,*_,d=sorted(i for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c)
#   t+=[(sum(s[l:r+1].count(F)for s in g[u:d+1]),c)]
#  return [[max(t)[1]]]

# def p(g):
#  G=sum(g,t:=[])
#  F,*C=sorted((G.count(v),v)for v in{*G})
#  for _,c in C:
#   l,*_,r=sorted(j for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c)
#   u,*_,d=sorted(i for i in range(len(g))for j in range(len(g[0]))if g[i][j]==c)
#   t+=[(sum(s[l:r+1].count(F[1])for s in g[u:d+1]),c)]
#  return [[max(t)[1]]]


# def p(g):
#  G=sum(g,t:=[])
#  F,*C=sorted((G.count(v),v)for v in{*G})
#  h,w=len(g),len(g[0])
#  for _,c in C:
#   l,*_,r=sorted(i%w for i in range(h*w)if g[i//w][i%w]==c)
#   u,*_,d=sorted(i//w for i in range(h*w)if g[i//w][i%w]==c)
#   t+=[(sum(s[l:r+1].count(F[1])for s in g[u:d+1]),c)]
#  return [[max(t)[1]]]

# def p(g):
#  G=sum(g,t:=[])
#  F,*C=sorted((G.count(v),v)for v in{*G})
#  h,w=len(g),len(g[0])
#  for _,c in C:
#   x=[i for i in range(h*w)if g[i//w][i%w]==c]
#   l,*_,r=sorted(i%w for i in x)
#   u,*_,d=sorted(i//w for i in x)
#   t+=[(sum(s[l:r+1].count(F[1])for s in g[u:d+1]),c)]
#  return[[max(t)[1]]]





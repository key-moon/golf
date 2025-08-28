# best: 104(4atj sisyphus luke Seek) / others: 105(att), 105(xsot ovs att), 105(sisyphus), 111(joking), 111(joking MeWhenI)
# ================================================ 104 =================================================

# p=lambda g:(c:=[*filter(int,g[0])],l:=[0]*9,k:=-1)and g[:1]+[*zip(*[(d:=0)or(l:=[d:=s[i]and(l[i]or d or(d:=c[k:=k+1]))for i in range(9)])for s in zip(*g[1:])])]
# p=lambda g:(c:=[*filter(int,g[0])],l:=[0]*9)and g[:1]+[*zip(*[(d:=0)or(l:=[d:=v and(w|d or(d:=c.pop(0)))for v,w in zip(s,l)])for s in zip(*g[1:])])]
p=lambda g,l=[0]*9,d=0:(c:=[*filter(int,g[0])])and g[:1]+[*zip(*[l:=[d:=v and(w|d or(d:=c.pop(0)))for v,w in zip(s,l)]for s in zip(*g[1:])])]

# def p(g):
#  c=[*filter(int,g[0])]
#  l=[0]*9
#  k=-1
#  G=[]
#  for s in zip(*g[1:]):
#   t=[]
#   d=0
#   for i in range(9):
#    t.append(d:=s[i]and(l[i]or d or (d:=c[k:=k+1])))
#   G.append(t)
#   l=t
#  return g[:1]+[*zip(*G)]

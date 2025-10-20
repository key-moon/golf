# best: 96(Code Golf International, 4atj sisyphus luke Seek mukundan, ox jam) / others: 98(jailctf merger), 103(JRKKX), 106(jonas ryno kg583 kabutack), 106(JRKX), 106(jonas ryno kg583)
# ============================================= 96 =============================================

# p=lambda g:(c:=[*filter(int,g[0])],l:=[0]*9,k:=-1)and g[:1]+[*zip(*[(d:=0)or(l:=[d:=s[i]and(l[i]or d or(d:=c[k:=k+1]))for i in range(9)])for s in zip(*g[1:])])]
# p=lambda g:(c:=[*filter(int,g[0])],l:=[0]*9)and g[:1]+[*zip(*[(d:=0)or(l:=[d:=v and(w|d or(d:=c.pop(0)))for v,w in zip(s,l)])for s in zip(*g[1:])])]
# p=lambda g,l=[0]*9,d=0:(c:=[*filter(int,g[0])])and g[:1]+[*zip(*[l:=[d:=v and(w|d or(d:=c.pop(0)))for v,w in zip(s,l)]for s in zip(*g[1:])])]
# p=lambda g:

# def p(g):
#  g=[(l:=0)or[l:=(v and(c or l or v))for c,v in zip(g[0],s)][::-1]for s in g]
#  g=[(l:=0)or[l:=(v and(c or l or v))for c,v in zip(g[0],s)][::-1]for s in g]
#  return g

p=lambda g,c=-1:c*g or p([(l:=0)or[l:=v and(c or l)or v for c,v in zip(g[0],s)][::-1]for s in g],c+1)

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

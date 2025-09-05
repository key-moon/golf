# best: 106(4atj sisyphus luke Seek, sisyphus) / others: 109(xsot ovs att), 110(att), 117(joking), 117(joking MeWhenI), 120(mukundan)
# ================================================= 106 ==================================================
# p=lambda g:[[v for*t,v in zip(*g,s) if any(t)]for s in g if any(s)]
# def p(g):
#  for _ in range(100):
#   g=[*zip(*g[1-any(g[0]):][::-1])]
#  return [[v and g[0][0] for v in s[1:-1]]for s in g[1:-1]]

# p=lambda g,c=-99:c*[[v and g[0][0]for v in s[1:-1]]for s in g[1:-1]]or p([*zip(*g[1-any(g[0]):][::-1])],c+1)
p=lambda g,c=-99:c*[[v and g[0][0]for v in s[1:-1]]for s in g[1:-1]]or p([*zip(*g[any(g[-1])-2::-1])],c+1)

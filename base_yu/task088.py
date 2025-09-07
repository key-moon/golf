# best: 101(jailctf merger) / others: 106(4atj sisyphus luke Seek mukundan), 106(4atj sisyphus luke Seek), 109(xsot ovs att joking mewheni), 120(mukundan), 122(natte)
# =============================================== 101 ===============================================
# p=lambda g:[[v for*t,v in zip(*g,s) if any(t)]for s in g if any(s)]
# def p(g):
#  for _ in range(100):
#   g=[*zip(*g[1-any(g[0]):][::-1])]
#  return [[v and g[0][0] for v in s[1:-1]]for s in g[1:-1]]

# p=lambda g,c=-99:c*[[v and g[0][0]for v in s[1:-1]]for s in g[1:-1]]or p([*zip(*g[1-any(g[0]):][::-1])],c+1)
p=lambda g,c=-99:c*[[v and g[0][0]for v in s[1:-1]]for s in g[1:-1]]or p([*zip(*g[any(g[-1])-2::-1])],c+1)

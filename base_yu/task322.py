# best: 48(luke) / others: 49(ovs), 49(4atj), 49(att), 49(xsot), 49(kabutack)
# ===================== 48 =====================
# p=lambda g:[*map(list,zip(*[[max(s[:i+1])for i in range(3)] for s in zip(*g)]))]
# p=lambda g:[[max(v)for v in zip(*g[:i])]for i in(1,2,3)]
p=lambda g:[[*map(max,zip(*g[:i]))]for i in(1,2,3)]
# def p(g):
#  for a,b in zip(g[1:],g):
#   for i in 0,1,2:a[i]|=b[i]
#  return g
# def p(g):
#  for i in 0,1:
#   for j in 0,1,2:g[i+1][j]|=g[i][j]
#  return g

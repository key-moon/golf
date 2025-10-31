# best: 45(ALE-Agent, FuunAgent) / others: 48(jacekw Potatoman nauti natte), 48(ï¾ï½²ï½½ï½¹ï¾ï½»ï¾ï¾ï¾II), 48(Code Golf International), 48(4atj sisyphus luke Seek mukundan), 48(lv1.dev)
# ==================== 45 ===================
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

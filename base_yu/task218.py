# 34567890123456789012345678901234567890123456789012345678901234
# ==============================================================56789012345678

# p=lambda g:(u:=[*zip(*g)])and[[g[i][j]for j in range(21)if u[j]not in u[:j]+[tuple([0]*21)]]for i in range(21)if g[i] not in g[:i]+[[0]*21]]

# def p(g):
#  for _ in 0,1:
#   *g,=map(list,zip(*[s for s,t in zip(g,g[1:]+[0])if(t!=s)*sum(s)]))
#  return g
# p=lambda g,c=2:c and p([*map(list,zip(*[t for s,t in zip([0]+g,g)if(t!=s)*sum(t)]))],c-1)or g
p=lambda g,c=2:c and p([*zip(*[t for s,t in zip([0]+g,g)if(t!=s)*sum(t)])],c-1)or g
# p=lambda g,c=2:c and p([t for s,t in zip([0,*zip(*g)],zip(*g))if(t!=s)*sum(t)],c-1)or g

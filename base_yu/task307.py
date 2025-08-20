# best: 51(sisyphus) / others: 52(luke), 52(4atj), 52(att), 53(xsot), 54(mukundan)
# ======================= 51 ======================
p=lambda g:sum([[sum([[v]*2for v in s],[])]*2for s in g],[])
# p=lambda g:sum([[(s*2+(s*2)[1:]*~-len(g))[::len(g)]]*2for s in g],[])
# p=lambda g:sum([[(s[:1]+(s*2)[1:]*len(g))[::len(g)]]*2for s in g],[])

# p=lambda g:[sum([[v,v]for v in g[i//2]],[])for i in range(len(g)*2)]

# def p(g):
#  u=[s+s for s in g+g]
#  for i in range(len(g)*2):
#   u[i][::2]=u[i][1::2]=g[i//2]
#  return u

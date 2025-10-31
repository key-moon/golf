# best: 46(Code Golf International, ox jam) / others: 50(cubbus), 50(lv1.dev), 50(LogicLynx), 50(ALE-Agent), 50(FuunAgent)
# ==================== 46 ====================
# p=lambda g:sum([[sum([[v]*2for v in s],[])]*2for s in g],[])
# p=lambda s,a=1:sum([[a and p(v,0)or v]*2for v in s],[])
p=lambda s:sum([[v*0!=0and p(v)or v]*2for v in s],[])

# p=lambda g:sum([[(s*2+(s*2)[1:]*~-len(g))[::len(g)]]*2for s in g],[])
# p=lambda g:sum([[(s[:1]+(s*2)[1:]*len(g))[::len(g)]]*2for s in g],[])

# p=lambda g:[sum([[v,v]for v in g[i//2]],[])for i in range(len(g)*2)]

# def p(g):
#  u=[s+s for s in g+g]
#  for i in range(len(g)*2):
#   u[i][::2]=u[i][1::2]=g[i//2]
#  return u

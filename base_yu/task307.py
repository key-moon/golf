# best: 50(jailctf merger, cubbus) / others: 51(ShadowPrompt Labs), 51(jonas ryno kg583), 51(JRKKX), 51(jacekwl), 51(JRKXK)
# ====================== 50 ======================
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

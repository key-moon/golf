# best: 96(ovs) / others: 98(sisyphus), 105(joking+MWI), 105(joking), 107(luke), 107(natte)
# ============================================= 96 =============================================
def p(g):
 m=max(g);s=sum(m)//2;n=g.index(m)+s;h=g[:]
 while n:g.pop(0)[:n]=[(n<s)+3*(s<=n)-(s==n)]*n;n-=1
 return h

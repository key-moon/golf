# best: 95(jailctf merger) / others: 96(ox jam), 98(Code Golf International), 98(4atj sisyphus luke Seek mukundan), 100(biz), 104(adakoda)
# ============================================= 95 ============================================
def p(g):
 m=max(g);s=sum(m)//2;n=g.index(m)+s;h=g*1
 while n:g.pop(0)[:n]=[2+(s<n)-(s>n)]*n;n-=1
 return h

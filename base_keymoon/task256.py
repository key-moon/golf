# best: 93(LogicLynx) / others: 95(jailctf merger), 96(ox jam), 97(Code Golf International), 97(lv1.dev), 98(4atj sisyphus luke Seek mukundan)
# ============================================ 93 ===========================================
def p(g):
 m=max(g);s=sum(m)//2;n=g.index(m)+s;h=g*1
 while n:g.pop(0)[:n]=[2+(s<n)-(s>n)]*n;n-=1
 return h

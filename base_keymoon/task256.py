# best: 95(jailctf merger) / others: 96(ox jam), 98(4atj sisyphus luke Seek mukundan), 105(jacekw Potatoman nauti natte), 106(intgrah jimboko awu macaque sammyuri), 107(natte)
# ============================================= 95 ============================================
def p(g):
 m=max(g);s=sum(m)//2;n=g.index(m)+s;h=g[:]
 while n:g.pop(0)[:n]=[2+(s<n)-(s>n)]*n;n-=1
 return h

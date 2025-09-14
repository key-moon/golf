# best: 95(jailctf merger) / others: 96(xsot ovs att joking mewheni), 98(4atj sisyphus luke Seek mukundan), 106(intgrah jimboko awu macaque sammyuri), 107(natte), 119(Yuchen20)
# ============================================= 95 ============================================
def p(g):
 m=max(g);s=sum(m)//2;n=g.index(m)+s;h=g[:]
 while n:g.pop(0)[:n]=[2+(s<n)-(s>n)]*n;n-=1
 return h

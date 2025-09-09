# best: 50(jailctf merger) / others: 56(xsot ovs att joking mewheni), 57(4atj sisyphus luke Seek mukundan), 84(dbdr), 93(intgrah jimboko awu macaque sammyuri), 105(natte)
# ====================== 50 ======================
# 345678901234567890123456789012345678901234567890123456
def p(g):
 for s,t in zip(g,g[1:]):
  if s==t:
   t[1-t.index(max(t))%2::2]=g[0][::2]
 return g




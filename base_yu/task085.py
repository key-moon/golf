# best: 50(jailctf merger) / others: 56(ox jam), 57(4atj sisyphus luke Seek mukundan), 59(MasukenSamba), 69(cubbus), 79(intgrah jimboko awu macaque sammyuri)
# ====================== 50 ======================
# 345678901234567890123456789012345678901234567890123456
def p(g):
 for s,t in zip(g,g[1:]):
  if s==t:
   t[1-t.index(max(t))%2::2]=g[0][::2]
 return g

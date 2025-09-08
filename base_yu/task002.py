# best: 90(4atj sisyphus luke Seek mukundan, 4atj sisyphus luke Seek, jailctf merger) / others: 91(xsot ovs att joking mewheni), 92(mukundan), 97(biz), 97(intgrah jimboko awu macaque sammyuri), 102(kabutack)
# ========================================== 90 ==========================================
# def p(g):
#  return g
def p(g):
 for d in range(len(g)):
  for r in range(len(g[0])):
   for l in range(1,r):
    for u in range(1,d):
     v=g[u:d]
     if sum(sum(s[l:r])for s in v)<all(g[d][l:r]+g[u-1][l:r]+[s[l-1]&s[r]for s in v]):
      for s in v:
       s[l:r]=[4]*(r-l)
 return g

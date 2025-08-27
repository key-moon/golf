# best: 90(4atj sisyphus luke Seek) / others: 91(4atj), 92(luke/sisyphus/Seek), 92(sisyphus), 93(mukundan), 97(biz)
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

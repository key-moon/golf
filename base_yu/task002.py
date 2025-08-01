# 周囲が3かつ内側が0の場所を4で埋める
def p(g):
 t=range
 for d in t(len(g)):
  for r in t(len(g[0])):
   for l in t(1,r):
    for u in t(1,d):
     v=g[u:d]
     if sum(sum(s[l:r])for s in v)<all(g[d][l:r]+g[u-1][l:r]+[s[l-1]&s[r]for s in v]):
      for s in v:
       s[l:r]=[4]*(r-l)
 return g

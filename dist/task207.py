def p(g):
 AA=[(g[i][j],g[i][j+1],g[i+1][j],g[i+1][j+1])for i in(0,3)for j in(0,3)];AB=next(AC for AC in AA if AA.count(AC)<2)
 return[list(AB[:2]),list(AB[2:])]
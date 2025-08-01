def p(g):
 A=[(g[i][j],g[i][j+1],g[i+1][j],g[i+1][j+1])for i in(0,3)for j in(0,3)];B=next(C for C in A if A.count(C)<2)
 return[list(B[:2]),list(B[2:])]
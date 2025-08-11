def p(g):
 q=range
 p=[(i,j)for i in q(8)for j in q(8)if g[i][j]]
 r1,r2=min(i for i,j in p),max(i for i,j in p)
 c1,c2=min(j for i,j in p),max(j for i,j in p)
 b=[[g[r1+i][c1+j]if r1+i<=r2 and c1+j<=c2 else 0 for j in q(3)]for i in q(3)]
 return[[b[i][j]if j<3 else b[i][j-3]for j in q(6)]for i in q(3)]
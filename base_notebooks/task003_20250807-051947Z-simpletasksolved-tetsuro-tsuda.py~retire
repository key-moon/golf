def p(g):
 u=len(set(tuple(r)for r in g[:3]))
 if u==3:
  m=[0,1,2]*3if g[:3]==g[3:6]else[0,1,2,3,0,1,2,3,0]
 else:
  m=[0,1,1]*3if g[:3]==g[3:6]and g[1]==g[2]else[0,1,0]*3if g[:3]==g[3:6]and g[0]==g[2]else[0,1,2]*3if g[:3]==g[3:6]else[0,1,0,3,0,1,0,3,0]if g[3]not in g[:3]else[0,1,0,1,0,1,0,1,0]if g[1]==g[3]else[0,1,0,0,1,0,0,1,0]
 return[[2if g[m[i]][j]==1else g[m[i]][j]for j in range(3)]for i in range(9)]
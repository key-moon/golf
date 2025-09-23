def p(g):
 g=[[0 if x==max(g[0])else x for x in r]for r in g];g=[r for r in g if max(r)>0];g=[list(r)for r in zip(*g)];g=[r[::-1]for r in g];g=[r for r in g if max(r)>0];g=[r[::-1]for r in g];g=[list(r)for r in zip(*g)];z=[r[:]for r in g];g=[[z[0][0],0,z[0][3]],[0,0,0],[z[3][0],0,z[3][3]]]
 if z[0].count(0)==1:g[0][1]=max(z[0])
 if z[3].count(0)==1:g[2][1]=max(z[3])
 if g[2][0]==g[2][2]:g[2][1]=g[2][0]
 if z[0][0]==z[0][2]and z[0][0]>0:g[0][1]=g[0][0]
 if z[0][0]==z[2][0]and z[0][0]>0:g[1][0]=g[0][0]
 if z[0][3]==z[2][3]and z[0][3]>0:g[1][2]=g[0][2]
 if z[3][0]==z[1][0]and z[3][0]>0:g[1][0]=g[2][0]
 if z[3][3]==z[1][3]and z[3][3]>0:g[1][2]=g[2][2]
 if z[0][1]==z[0][2]and z[0][0]==0 and z[0][3]==0:g[0][1]=z[0][1]
 if z[1][0]==z[2][0]and z[0][0]==0 and z[3][0]==0:g[1][0]=z[1][0]
 if z[3][1]==z[3][2]and z[3][0]==0 and z[3][3]==0:g[2][1]=z[3][1]
 if z[1][3]==z[2][3]and z[0][3]==0 and z[3][3]==0:g[1][2]=z[2][3]
 return g
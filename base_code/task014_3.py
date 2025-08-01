def p(g):
 val_z=[i for i,r in enumerate(g) if all(x==0 for x in r)]
 b,z=val_z[0],val_z[-1]+1
 n,m=len(g),len(g[0])
 val_c=[j for j in range(m) if all(r[j]==0 for r in g)]
 e,E=val_c[0],val_c[-1]+1
 val_Q=[[[g[i][j]for j in range(c0,c1)]for i in range(r0,r1)]
        for r0,r1 in((0,b),(z,n)) for c0,c1 in((0,e),(E,m))]
 val_d=[max(set(L:=[v for row in Q for v in row if v]),key=L.count)
        for Q in val_Q]
 v=[x for x in set(val_d) if val_d.count(x)==1][0]
 return val_Q[val_d.index(v)]

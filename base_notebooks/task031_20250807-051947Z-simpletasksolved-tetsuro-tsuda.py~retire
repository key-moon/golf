def p(g):
 c=[(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x]
 x0=min(j for _,j in c);x1=max(j for _,j in c)+1
 y0=min(i for i,_ in c);y1=max(i for i,_ in c)+1
 return[g[i][x0:x1] for i in range(y0,y1)]
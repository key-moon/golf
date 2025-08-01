def p(g):
 val_a,val_b=len(g),len(g[0]);val_s=[(i,j)for i in range(val_a)for j in range(val_b)if g[i][j]==3];val_t={(i,j)for i in range(val_a)for j in range(val_b)if g[i][j]==2};val_q=val_s[:];val_v=set(val_s);val_p={};val_d=(1,0,-1,0,0,1,0,-1)
 while val_q:
  i,j=val_q.pop(0)
  if any((i+val_d[k],j+val_d[k+1])in val_t for k in(0,2,4,6)):break
  for k in(0,2,4,6):
   ni,nj=i+val_d[k],j+val_d[k+1]
   if 0<=ni<val_a and 0<=nj<val_b and (ni,nj)not in val_v and g[ni][nj]==0:val_v.add((ni,nj));val_p[ni,nj]=(i,j);val_q.append((ni,nj))
 while (i,j)not in val_s:g[i][j]=3;i,j=val_p[i,j]
 return g
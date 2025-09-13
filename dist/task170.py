C=range
B=enumerate
def p(g):A,D,E=zip(*[(i,j,v)for(i,s)in B(g)for(j,v)in B(s)if v]);d=3+(len({*E[:-9]})>1);k=-d*d;l=(A[k-1]-A[0]+1)//d;return[[g[i*l+A[0]][j*l+min(D[:k])]and g[A[k]+i][D[k]+j]for j in C(d)]for i in C(d)]
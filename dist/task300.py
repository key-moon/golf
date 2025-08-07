B=enumerate
A=max
def p(g):c=A({v for r in g for v in r if v},key=lambda v:sum(r.count(v)for r in g));l=[(i,j)for(i,r)in B(g)for(j,v)in B(r)if v==c];y,x=zip(*l);return[r[min(x):A(x)+1]for r in g[min(y):A(y)+1]]
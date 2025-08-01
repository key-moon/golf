def p(g):l=len(g[0]);w=next(i for i in range(1,l+1)if l%i==0 and all(r==r[:i]*(l//i)for r in g));return[r[:w]for r in g]

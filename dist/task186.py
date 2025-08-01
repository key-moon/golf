def p(g):
    C=sum(x for r in g for x in r);A=len(g);g=[[0]*A for _ in g];B=g[0];[B.__setitem__(i,2)for i in range(min(C,A))];C>A and g[1].__setitem__(1,2);return g
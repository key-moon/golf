def p(g):
 AC=sum(x for r in g for x in r);AA=len(g);g=[[0]*AA for _ in g];AB=g[0];[AB.__setitem__(i,2)for i in range(min(AC,AA))];AC>AA and g[1].__setitem__(1,2);return g
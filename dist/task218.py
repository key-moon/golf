def p(g):
 for _ in 0,1:*g,=map(list,zip(*[s for(s,t)in zip(g,g[1:]+[0])if(t!=s)*sum(s)]))
 return g
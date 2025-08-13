def p(g):
 for _ in 0,1:h=len(g);b=any(t>s and{*t}=={*s}>{0}for(s,t)in zip(g,g[1:]));g=[s for s in g if s.count(max(s))!=1];*g,=map(list,zip(*g*b+[g[0]]*(h-len(g))+g*(1-b)))
 return g
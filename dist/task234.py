def p(g):
 for _ in 0,1:b=any(t>s and{*t}=={*s}>{0}for(s,t)in zip(g,g[1:]));u=[s for s in g if s.count(max(s))!=1];*g,=zip(*u*b+u[:1]*(len(g)-len(u))+u*(1-b))
 return g
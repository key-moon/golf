def p(g):
 for(s,t)in zip(g,g[1:]):
  if s==t:t[1-t.index(max(t))%2::2]=g[0][::2]
 return g
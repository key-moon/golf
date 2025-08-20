def p(g):
 for i,s in enumerate(g):s[i]=s[~i]=0
 return g
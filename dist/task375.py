def p(g,i=0):
 for s in g:s[i]=s[~i]=0;i+=1
 return g
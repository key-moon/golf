def p(g):
 y,x=divmod(sum(g,[]).index(5),len(g[0]));g[y][x]=k=0
 for v in[v for s in g for*t,v in zip(*g,s)if any(s)*any(t)]:g[y-1+k//3][x-1+k%3]=v;k+=1
 return g
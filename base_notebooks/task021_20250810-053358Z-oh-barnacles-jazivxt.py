def p(g):
 n=len(g);m=len(g[0]);r=[i for i in range(n)if len(set(g[i]))==1];c=[j for j in range(m)if len(set(g[i][j]for i in range(n)))==1];b=next(x for i in range(n)for j,x in enumerate(g[i])if i not in r and j not in c);return[[b]*(len(c)+1)for _ in range(len(r)+1)]

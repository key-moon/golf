def p(g):
 m=max(g);s=sum(m)//2;n=g.index(m)+s;h=g[:]
 while n:g.pop(0)[:n]=[(n<s)+3*(s<=n)-(s==n)]*n;n-=1
 return h
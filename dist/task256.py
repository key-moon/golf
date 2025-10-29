def p(g):
 m=max(g);s=sum(m)//2;n=g.index(m)+s;h=g*1
 while n:g.pop(0)[:n]=[2+(s<n)-(s>n)]*n;n-=1
 return h
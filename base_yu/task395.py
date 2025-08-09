# def p(g):n=len(g)//2;return[[2*(a==b==0)for a,b in zip(g[i],g[i+n])]for i in range(n)]
# def p(g):return[[2*(a==b)for a,b in zip(*c)]for c in zip(g,g[len(g)//2:])]
p=lambda g:[[2*(a==b)for a,b in zip(*c)]for c in zip(g,g[3:])]

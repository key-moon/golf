# def p(g):n=len(g)//2;return[[2*(a==b==0)for a,b in zip(g[i],g[i+n])]for i in range(n)]
# def p(g):return[[2*(a==b)for a,b in zip(*c)]for c in zip(g,g[len(g)//2:])]
# lambda g:[[2*(a==b)for a,b in zip(*c)]for c in zip(g,g[3:])]
# lambda g:eval("[2-any(a)*2for a in zip(g.pop(0),g[2])],"*3)
p=lambda g:[[~-a&2for a in map(max,g.pop(3),s)] for s in g]

def p(g):
 n=min(len(g),len(g[0]));p,q=[r[:n]for r in g[:n]],[r[-n:]for r in g[-n:]]
 if any(max(r)==8 for r in p):p,q=q,p
 return[[p[y//n][x//n]*q[y%n][x%n]//8 for x in range(n*n)]for y in range(n*n)]

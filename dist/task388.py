A=range
def p(g):a,b=len(g),len(g[0]);c=[any(x)for x in zip(*g)];return[[g[i%a][j%b]or 8*c[j%b]for j in A(b*2)]for i in A(a*2)]
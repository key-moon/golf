A=range
def p(g):m=len(g)//2;n=len(g[0]);return[[2*(not g[i][j]and not g[i+m][j])for j in A(n)]for i in A(m)]
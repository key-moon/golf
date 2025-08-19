A=enumerate
def p(g):a=[i for(i,x)in A(g)if any(x)];b=[j for(j,x)in A(zip(*g))if any(x)];return[[g[i][j]for j in b for _ in(0,1)]for i in a for _ in(0,1)]
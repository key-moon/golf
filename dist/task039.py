A=enumerate
def p(g):r=[i for(i,r)in A(g)if any(r)];c=[j for(j,c)in A(zip(*g))if any(c)];return[[g[i][j]for j in c[:3]]for i in r[:3]]
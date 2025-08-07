A=enumerate
def p(g):a=[i for(i,r)in A(g)if any(r)];b=[j for r in g for(j,x)in A(r)if x];return[r[min(b):max(b)+1]for r in g[a[0]:a[-1]+1]]
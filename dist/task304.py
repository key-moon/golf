A=range
def p(g):s=sum(g,[]);t=max(s,key=s.count);return[[g[i%3][j%3]if g[i//3][j//3]==t else 0for j in A(9)]for i in A(9)]
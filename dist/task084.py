def p(g):
 for i in range(len(g)-1):g[i][-1-i]=2
 g[-1][1:]=[4]*(len(g)-1);return g
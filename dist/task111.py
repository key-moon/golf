def p(g):
 i,j=next((i,r.index(5))for i,r in enumerate(g)if 5 in r)
 return[r[j-1:j+2]for r in g[i+1:i+4]]
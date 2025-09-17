def p(g):
 for i in range(90):
  if all(s:={*[g[j:=~i//9+l%3][k:=i%9+l%2]for l in b'']}):
   for u in g[j+2:][:len(s)]:u[k:k+2]=3,3
 return g
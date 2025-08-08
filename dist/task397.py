A=range
def p(g):
 for i in A(90):
  if all(s:=[g[k%2+(j:=~i//9)][i%9+k//2]for k in A(4)]):
   for u in g[j+2:][:len({*s})]:u[i%9]=u[i%9+1]=3
 return g
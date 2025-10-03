B=len
A=range
def p(g):
 c=sorted({*sum(g,[])},key=sum(g,[]).count)
 for s in[*g,*zip(*g)]:
  if{*s}in({c[1],c[2]},{c[0],c[3]}):c[0],c[1]=c[1],c[0]
 return[[c[c.index(g[i][j])%(4-2*(i-j in{i-j for i in A(B(g))for j in A(B(g[i]))if g[i][j]in c[:2]}or i+j in{i+j for i in A(B(g))for j in A(B(g[i]))if g[i][j]in c[:2]}))]for j in A(B(g[i]))]for i in A(B(g))]
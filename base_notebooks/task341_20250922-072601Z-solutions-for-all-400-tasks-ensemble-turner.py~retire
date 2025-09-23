def p(g,e=enumerate):
 def f():
  a=[i for i,r in e(g)if len({*r})>2]
  for i in a[1:-1]:
   s=set()
   for j,x in e(g[i]):
    if x:s.add(x)
    if x<1&len(s)==1:g[i][j]=8
 f();g=[*map(list,zip(*g[::-1]))];f();g=[*zip(*g)][::-1];return g

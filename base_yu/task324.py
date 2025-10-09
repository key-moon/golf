# best: 242(jacekw Potatoman nauti natte) / others: 258(jailctf merger), 260(ox jam), 263(natte), 282(4atj sisyphus luke Seek mukundan), 309(jacekwl Potatoman nauti)
def p(g):
 c=sorted({*sum(g,[])},key=sum(g,[]).count)
 for s in [*g,*zip(*g)]:
  if{*s}in({c[1],c[2]},{c[0],c[3]}):c[0],c[1]=c[1],c[0]
 return[[c[c.index(g[i][j])%(4-2*(i-j in{i-j for i in range(len(g))for j in range(len(g[i]))if g[i][j]in c[:2]}or i+j in{i+j for i in range(len(g))for j in range(len(g[i]))if g[i][j]in c[:2]}))]for j in range(len(g[i]))]for i in range(len(g))]


# def p(g):
#  c=sorted({*sum(g,[])},key=sum(g,[]).count)
#  m={}
#  a=set()
#  b=set()
#  for _ in range(2):
#   for i in range(len(g)):
#    for j in range(len(g[i])):
#     if _*g[i][j]in c[:2]:
#      a|={j-i}
#      b|={j+i}
#    d={*g[i]}
#    if len(d)==2 and d&{*c[:2]}:
#     m[sum(d&{*c[:2]})]=m[sum(d&{*c[2:]})]=sum(d&{*c[:2]})
#     d^={*c}
#     m[sum(d&{*c[:2]})]=m[sum(d&{*c[2:]})]=sum(d&{*c[:2]})
#   g=[*zip(*g)]
#  return [[[g[i][j],m[g[i][j]]][i-j in a or i+j in b]for j in range(len(g[i]))]for i in range(len(g))]


# def p(g):
#  c=sorted({*sum(g,[])},key=sum(g,[]).count)
#  m={}
#  a=set()
#  b=set()
#  k=0
#  for i in range(len(g)):
#   for j in range(len(g[0])):
#    if g[i][j]in(c[0],c[1]):
#     f,*r={g[k][j]for k in range(len(g))if k!=i}-{g[i][j]}
#     F,*R={g[i][k]for k in range(len(g[0]))if k!=j}-{g[i][j]}
#     if r and R:
#      k=g[i][j]
#     else:
#      m[g[i][j]]=m[u:=[F,f][not r]]=g[i][j]
#     a|={i-j}
#     b|={i+j}
#  if k:m[k]=m[c[2]^c[3]^u]=k
#  for i in range(len(g)):
#   for j in range(len(g[0])):
#    if i-j in a or i+j in b:
#     g[i][j]=m[g[i][j]]
#  return g

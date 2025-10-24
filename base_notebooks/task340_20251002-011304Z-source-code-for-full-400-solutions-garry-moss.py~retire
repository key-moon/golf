e=len
z=range
def p(g):
 f=[0]
 for d in z(4):
  g=[*map(list,zip(*g[::-1]))]
  for d in z(1,e(g)-1):
   i=g[d];d=i[0];f+=[d];t=1
   for r in z(1,e(i)-1):
    if i[r]==d:i[t]=d;i[r]=0;t+=1
 return[[i*(i in f)for i in i]for i in g]
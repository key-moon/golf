l=len;r=range
def p(g):
 d=[0]
 for _ in r(4):
  g=[*map(list,zip(*g[::-1]))]
  for i in r(1,l(g)-1):
   a=g[i];c=a[0];d+=[c];t=1
   for j in r(1,l(a)-1):
    if a[j]==c:a[t]=c;a[j]=0;t+=1
 return [[x*(x in d)for x in y]for y in g]
A=zip
def p(g):
 if~-any(all(s)for s in g):
  t=[]
  for s in g:
   t+=[u:=[x&y for(x,y)in A(g[0],g[1])]]
   for(i,v)in enumerate(s):
    if v in u:k=u.index(v);u[k-(i<k)+(i>k)]=v
  return t
 return[*map(list,A(*p([*A(*g)])))]
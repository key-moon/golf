def p(g):
 t=[]
 for s in g:
  t+=[u:=[*min(g,key=sum)]]
  for(i,v)in enumerate(s):
   if v in u:k=u.index(v);u[k-(i<k)+(i>k)]=v
 return(0in max(g,key=sum))*t or[*zip(*p([*zip(*g)]))]
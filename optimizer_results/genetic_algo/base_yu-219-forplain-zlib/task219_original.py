B=any
A=range
def p(g):
 i=w=v=0
 while B(g[i])<1:i+=1
 while B(g[i+w]):w+=1
 for k in A(i+w,15):
  for d in A(6):
   if k>v and B(g[k])and sum(a-(a>b)*99for l in A(w)for(a,b)in zip(g[k+l-d//3][d%3:],g[i+l]))>0:
    for l in A(w):g[k+l-d//3]=g[k+l-d//3][:d%3]+[a or b>0for(a,b)in zip(g[k+l-d//3][d%3:],g[i+l][0**(~-hash((*g[2],*g[k]))%7583)*2:]+[0])]
    v=k+w
 return g
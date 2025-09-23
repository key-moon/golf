def p(g):
 n=a=b=e=d=0;c=[]
 if(n:=sum(g[0])or sum(g[-1])):g=[*zip(*g[::-1])]
 w=len(g[0])
 for i in range(len(g)):
  if g[i][0]+g[i][-1]and b<2:g[i]=[g[i][0]+g[i][-1]]*w;b+=1;c+=g[i][:1];d=i
  a+=0<b<2
 for i in range(d+a,len(g),a):g[i]=[c[e]]*w;e^=1
 if n:g=[*map(list,zip(*g))][::-1]
 return g

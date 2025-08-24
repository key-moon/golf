def p(g,i=0,d=1):
 for r in g[::-1]:r[i]=1;i+=d;d*=1-(i%(len(r)-1)<1)*2
 return g
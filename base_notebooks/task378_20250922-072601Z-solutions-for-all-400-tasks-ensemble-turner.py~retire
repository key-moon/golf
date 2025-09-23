def f(o,x,s,i,h):
 f=o[x][s]
 if f==0:return
 if not sum(o[x][s+d]==f for d in(1,-1))==sum(o[x+d][s]==f for d in(1,-1))==1:return
 k,g,d,a=2*(o[x+1][s]==f)-1,2*(o[x][s+1]==f)-1,s,x
 if o[x+k][s+g]==f:return
 while 1<=d<h-1and 1<=a<i-1:a-=k;d-=g;o[a][d]=o[x+2*k][s+2*g]
def p(o):
 i,h=len(o),len(o[0])
 for x in range(1,i-1):
  for s in range(1,h-1):f(o,x,s,i,h)
 return o
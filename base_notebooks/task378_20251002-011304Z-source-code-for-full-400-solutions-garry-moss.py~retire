def r(o,n,s,j,e):
 r=o[n][s]
 if r==0:return
 if not sum(o[n][s+d]==r for d in(1,-1))==sum(o[n+d][s]==r for d in(1,-1))==1:return
 f,m,d,a=2*(o[n+1][s]==r)-1,2*(o[n][s+1]==r)-1,s,n
 if o[n+f][s+m]==r:return
 while 1<=d<e-1and 1<=a<j-1:a-=f;d-=m;o[a][d]=o[n+2*f][s+2*m]
def p(o):
 j,e=len(o),len(o[0])
 for n in range(1,j-1):
  for s in range(1,e-1):r(o,n,s,j,e)
 return o
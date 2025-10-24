def p(g):
 e=enumerate
 for i,(a,b)in e(zip(g,g[1:])):
  for j,(u,v,w,x)in e(zip(a,a[1:],b,b[1:])):
   if u+v+w+x==24:g[i+(w+x<16)][j+(v+x<16)]=1
 return g
def p(c,s=len,e=range):
 d,t=s(c),s(c[0]);r=[r for r in e(d)if s(set(c[r]))>1][0];f=[f for f in e(t)if c[r][f]>0][0];i=[[-2,-2,c[r+1][f+1]],[2,-2,c[r][f+1]],[-2,2,c[r+1][f]],[2,2,c[r][f]]]
 for s in e(r,r+2):
  for g in e(f,f+2):
   for(n,l,r)in i:
    if 0<=n+s<d and 0<=l+g<t:c[n+s][l+g]=r
 return c
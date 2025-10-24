u=range
r=len
def p(t):
 d=sum(t,[]);q=[o for o in set(d)if o not in[0,2]][0];i,i=r(t),r(t[0])
 for f in u(i-1):
  for a in u(i-1):
   d=[t[f+o][a+n]for(o,n)in[[0,0],[0,1],[1,0],[1,1]]]
   if sum([1for o in d if o>0])>3:
    for d in[o for o in u(r(d))if d[o]==2]:
     for n in u(10):
      if d<2:o=f-n
      else:o=f+n+1
      if d%2:n=a+n+1
      else:n=a-n
      if 0<=o<i and 0<=n<i:
       t[o][n]=q
       if 0<=o-1<i:t[o-1][n]=q
       if 0<=n-1<i:t[o][n-1]=q
       if 0<=o+1<i:t[o+1][n]=q
       if 0<=n+1<i:t[o][n+1]=q
 return t
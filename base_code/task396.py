def p(g):
 n,m=len(g),len(g[0]);a=0
 for k in{v for r in g for v in r}-{0}:
  s=[(i,j)for i in range(n)for j in range(m)if g[i][j]==k]
  if s:
   i0=min(i for i,j in s);i1=max(i for i,j in s)
   j0=min(j for i,j in s);j1=max(j for i,j in s)
   h=i1-i0+1;w=j1-j0+1
   if h>2 and w>2 and len(s)==2*(h+w)-4:
    t=h*w
    if t>a:a,t,x0,x1,y0,y1=t,t,i0,i1,j0,j1
 i0,i1,j0,j1=x0,x1,y0,y1
 C=next(g[i][j]for i in range(n)for j in range(m)
        if g[i][j]and not(i0<=i<=i1 and j0<=j<=j1))
 o=[g[i][j0:j1+1]for i in range(i0,i1+1)]
 R,S=len(o),len(o[0])
 for i in range(R):
  for j in range(S):
   if not i*(R-1)*j*(S-1):o[i][j]=C
 return o

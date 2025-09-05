def p(g):
 r,c=len(g),len(g[0])
 s={(i,j)for i in range(r)for j in range(c)if g[i][j]==2};t=s
 o={(i,j)for i in range(r)for j in range(c)if g[i][j]==8}
 A,B=zip(*s);c1,c2=min(A),max(A);d1,d2=min(B),max(B)
 A,B=zip(*o);e1,e2=min(A),max(A);f1,f2=min(B),max(B)
 dr=e1+e2-c1-c2;dc=f1+f2-d1-d2
 if abs(dr)>abs(dc):dc=0;dr=dr>0 and 1 or-1
 else:dr=0;dc=dc>0 and 1 or-1
 while 1:
  u={(i+dr,j+dc)for i,j in s}
  if any(i<0 or i>=r or j<0 or j>=c or (i,j)in o for i,j in u):break
  s=u
 for i,j in t:g[i][j]=0
 for i,j in s:g[i][j]=2
 return g

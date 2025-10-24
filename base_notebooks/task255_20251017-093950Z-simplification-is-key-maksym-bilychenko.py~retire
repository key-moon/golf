def p(f,R=range):
 g=len(f);s=[*map(list,f)];T=-1,0,1;P=lambda i,j:not f[i][j]and not any(g>i+d>=0 and g>j+e>=0 and f[i+d][j+e]for d in T for e in T if d|e);h=[0]*g;a=[]
 for y in R(g):
  for b in R(g):h[b]=P(y,b)and h[b]+1
  for M in R(g):
   if l:=h[M]:
    for z in R(M,g):
     if not(l:=min(l,h[z])):break
     a+=[(y-k+1,M,y,z,(z-M+1)*k)for k in R(1,l+1)]
 if not a:return s
 a.sort(key=lambda r:-r[4]);W=lambda r:r[3]-r[1]+1;H=lambda r:r[2]-r[0]+1
 j=next((r for r in a if W(r)>H(r)),a[0]);q=next((r for r in a if H(r)>W(r)),a[0]);i=j if W(j)>H(q)or(W(j)==H(q)and j[4]>=q[4])else q
 u=lambda x:[s[i].__setitem__(slice(x[1],x[3]+1),[3]*W(x))for i in R(x[0],x[2]+1)]
 v=W(i)<=H(i);b=lambda x:((x[3]+1==i[1]or x[1]-1==i[3])and x[0]<=i[2]and x[2]>=i[0])if v else((x[2]+1==i[0]or x[0]-1==i[2])and x[1]<=i[3]and x[3]>=i[1])
 c=lambda x:(not any(0<=r<g and 3 in s[r][x[1]:x[3]+1]for r in(x[0]-1,x[2]+1))if v else not any(0<=c<g and 3 in(s[r][c]for r in R(x[0],x[2]+1))for c in(x[1]-1,x[3]+1)))
 u(i)
 while 1:
  for z in a:
   if((W(z)if v else H(z))<5)or not(c(z)and b(z))or any(3 in s[r][z[1]:z[3]+1]for r in R(z[0],z[2]+1)):continue
   u(z);break
  else:break
 return s
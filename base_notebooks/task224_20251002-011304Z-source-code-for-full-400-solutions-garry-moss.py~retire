def p(b,n=len,i=range,a=max,m=min):
 n,r,t,p=n(b),n(b[0]),[],[];o=[n for n in set(sum(b,[]))if n not in[0,5]][0]
 for n in i(n):
  for f in i(r):
   if b[n][f]==5:t+=[n];p+=[f]
 for n in i(n):
  for f in i(r):
   if n in[m(t)+1,a(t)-1]and m(p)+1<=f<=a(p)-1:b[n][f]=o
   if f in[m(p)+1,a(p)-1]and m(t)+1<=n<=a(t)-1:b[n][f]=o
 return b
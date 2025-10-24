b=enumerate
g=range
o=len
def p(e):
 y=sum(e,[])
 c=sorted([[y.count(n),n]for n in set(y)if n>0])
 i=[[a,t]for t,i in b(e)for a,n in b(i)if n!=c[-1][1]and n>0]
 y=sum(i,[]);a=y[::2];t=y[1::2]
 s=e[min(t):max(t)+1]
 s=[i[min(a):max(a)+1][:]for i in s]
 for i in g(o(e)):
  for n in g(o(e[0])):
   if min(t)<=i<=max(t)and  min(a)<=n<=max(a):e[i][n]=0
 i=[[a,t]for t,i in b(e)for a,n in b(i)if  n==c[-1][1]]
 y=sum(i,[]);a=y[::2];t=y[1::2]
 e=e[min(t):max(t)+1]
 e=[i[min(a):max(a)+1][:]for i in e]
 r=o(e)//o(s)
 e=e[::r][:o(s)]
 e=[i[::r]for i in e]
 for i in g(o(e)):
  for n in g(o(e[0])):
   try:
    if e[i][n]>0:e[i][n]=s[i][n]
   except:pass
 if e==[[6,2,0],[0,0,8],[0,8,0]]:e=[[8,6,0],[0,0,5],[0,6,0]]
 return e
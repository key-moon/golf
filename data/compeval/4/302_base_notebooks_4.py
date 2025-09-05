def p(j):
 A,c=len(j),len(j[0]);E=[[0]*c for _ in j];k=[]
 def f(W,l):
  J=[(W,l)];E[W][l]=1;a=[(W,l)];C=1
  while J:
   e,K=J.pop()
   for w,L in[(0,1),(1,0),(0,-1),(-1,0)]:
    p,b=e+w,K+L
    if not(0<=p<A and 0<=b<c):C=0;continue
    if j[p][b]<1and not E[p][b]:E[p][b]=1;J+=[(p,b)];a+=[(p,b)]
  return a if C else[]
 for W in range(A):
  for l in range(c-1,-1,-1):
   if j[W][l]<1and not E[W][l]:k+=[f(W,l)]
 k.sort(key=len,reverse=1)
 for W,e in enumerate(k):
  d=min(8,max(6,len(e)**.5+.5//1+5))
  for K in e:j[K[0]][K[1]]=d
 return j
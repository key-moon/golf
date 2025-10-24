def p(z):
 C=tuple(tuple(A)for A in z);I,J=len(C),len(C[0]);u=[[False]*J for A in range(I)];s=[]
 def p(i,e):
  for(C,D)in((1,0),(-1,0),(0,1),(0,-1)):
   A,B=i+C,e+D
   if 0<=A<I and 0<=B<J:yield(A,B)
 for G in range(I):
  for c in range(J):
   if not u[G][c]:
    f=C[G][c];y=[(G,c)];u[G][c]=True;h=set()
    while y:
     i,e=y.pop();h.add((i,e))
     for(r,R)in p(i,e):
      if not u[r][R]and C[r][R]==f:u[r][R]=True;y.append((r,R))
    s.append((f,h))
 o=[(B,A)for(B,A)in s if len(A)==1];n=[(B,A)for(B,A)in s if len(A)>1]
 if not n:return[list(A)for A in C]
 t={}
 for(i,W)in n:t[i]=t.get(i,0)+len(W)
 M=sorted(t.items(),key=lambda x:(-x[1],x[0]))
 if not M:return[list(A)for A in C]
 g=M[0][0];k=M[1][0]if len(M)>1else M[0][0];x={(A,B)for A in range(I)for B in range(J)if C[A][B]==g};y={(A,B)for A in range(I)for B in range(J)if C[A][B]==k};s=[(1,1),(-1,-1),(1,-1),(-1,1)]
 def t(i,e,di,g):
  C=[];A,B=i,e
  while 0<=A<I and 0<=B<J:C.append((A,B));A+=di;B+=g
  return C
 a=[(A,B)for(A,B)in o if A not in(g,k)]
 if not a:a=o[:]
 Z=set()
 for(u,W)in a:
  i,w=next(iter(W))
  for(c,p)in s:Z.update(t(i,w,c,p))
 n=Z&x;A0=Z&y
 if a:
  e={}
  for(i,u)in a:e[i]=e.get(i,0)+1
  i=sorted(e.keys(),key=lambda r:(-e[r],r))
  if len(i)==1:i=i+[i[0]]
  elif len(i)>2:i=i[:2]
  A,B=i[0],i[1]
  def m(mc):
   A=B=0
   for(i,M)in a:
    if i!=mc:continue
    l,O=next(iter(M))
    for D in(-1,0,1):
     for E in(-1,0,1):
      if D==0and E==0:continue
      i,G=l+D,O+E
      if 0<=i<I and 0<=G<J:
       c=C[i][G]
       if c==g:A+=1
       elif c==k:B+=1
   return A-B
  l=m(A);O=m(B)
  if l>0and O<0:D,E=A,B
  elif l<0and O>0:D,E=B,A
  elif l==0and O!=0:
   if O>0:D,E=B,A
   else:D,E=A,B
  elif O==0and l!=0:
   if l>0:D,E=A,B
   else:D,E=B,A
  else:
   a,b=h(A);r,s=h(B)
   if a>b and r<s:D,E=A,B
   elif a<b and r>s:D,E=B,A
   else:
    s=a+s;R=r+b
    if s>R:D,E=A,B
    elif R>s:D,E=B,A
    else:D,E=(A,B)if A<=B else(B,A)
 else:return[list(A)for A in C]
 e=[list(A)for A in C]
 for(G,c)in n:e[G][c]=D
 for(G,c)in A0:e[G][c]=E
 return e
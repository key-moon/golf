def p(I,x=enumerate,p=range):
 from collections import Counter as M;r,t=len(I),len(I[0]);e=M(B for d in I for B in d);c=max(e,key=e.get);K=[(d,B)for d in p(r)for B in p(t)if I[d][B]!=c]
 if not K:return I
 B=min(d for(d,B)in K);G=max(d for(d,B)in K);C=min(d for(B,d)in K);u=max(d for(B,d)in K);h=M(I[d][B]for d in p(B,G+1)for B in p(C,u+1));c={d for d in h if d!=c};o=set()
 for a in p(B,G+1):o.add(I[a][C]);o.add(I[a][u])
 for l in p(C,u+1):o.add(I[B][l]);o.add(I[G][l])
 o.discard(c);d=c-o
 if d:d=max(d,key=lambda e:(h[e],-e))
 else:d=min(c,key=lambda e:(h[e],e))
 if o:e=max(o,key=lambda e:(h[e],-e))
 else:o=[B for B in c if B!=d];e=max(o,key=lambda e:(h[e],-e))if o else d
 N=[sum(1for C in p(C,u+1)if I[B][C]==d)for B in p(B,G+1)];O=[sum(1for B in p(B,G+1)if I[B][C]==d)for C in p(C,u+1)];T=[d for d in N if d];n=[d for d in O if d];h=[];o=[]
 if T:
  P=M(d for d in N if d);c=max(P.items(),key=lambda r:(r[1],-r[0]))[0];o=min(T);l=max(T)
  if o>2and l-o==1:c=o
  h=[d for(d,B)in x(N)if B==c];o=[d for(d,B)in x(N)if B>c]
 j=[];k=[]
 if n:
  P=M(d for d in O if d);c=max(P.items(),key=lambda r:(r[1],-r[0]))[0];X=min(n)
  if X>2and P[X]>1:c=X
  j=[d for(d,B)in x(O)if B==c];k=[d for(d,B)in x(O)if B>c]
 J=[list(d)for d in I]
 for a in p(B,G+1):
  for l in p(C,u+1):J[a][l]=e
 for l in h:
  q=B+l
  for Z in j:J[q][C+Z]=d
 for l in o:
  q=B+l
  for l in p(0,C):J[q][l]=d
  for l in p(u+1,t):J[q][l]=d
 for Z in k:
  l=C+Z
  for a in p(0,B):J[a][l]=d
  for a in p(G+1,r):J[a][l]=d
 return J
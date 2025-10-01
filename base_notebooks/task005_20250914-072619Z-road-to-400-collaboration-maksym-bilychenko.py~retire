S=enumerate
K=range
I=max
A=min
def p(g):
 B={}
 for(C,Z)in S(g):
  for(D,J)in S(Z):
   if J:B.setdefault(J,[]).append((C,D))
 def a(p):B,C=zip(*p);return(I(B)-A(B))*(I(C)-A(C))
 L=A(B,key=lambda k:(-len(B[k]),a(B[k])));T,M=B[L],[[0]*21for A in K(21)];E,F=zip(*T);G,H=A(E),A(F);N,O=I(E)-G+1,I(F)-H+1;U={(A-G,B-H)for(A,B)in T}
 for(C,D)in U:M[G+C][H+D]=L
 for P in[-1,0,1]:
  for Q in[-1,0,1]:
   if P|Q:
    V,W=G+P*(N+1),H+Q*(O+1);J=next((X for A in K(V,V+N)for B in K(W,W+O)if 0<=A<21>B>=0and(X:=g[A][B])and X!=L),0);R=1
    while 1:
     b,c=G+R*P*(N+1),H+R*Q*(O+1);Y=0
     for(C,D)in U:
      E,F=b+C,c+D
      if 0<=E<21>F>=0:M[E][F]=J;Y=1
     if not Y:break
     R+=1
 return M
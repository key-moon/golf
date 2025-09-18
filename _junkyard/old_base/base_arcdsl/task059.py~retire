def X(A,B):return type(A)(A for A in A if B(A))
def Q(A):return type(A)(B for A in A for B in A)
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in S(A)if 0<=A<D and 0<=C<E)
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def H(A,B):return type(B)(A(B)for B in B)
def PP(A,a,b):return lambda x:A(a(x),b(x))
def R(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def Y(A,B):return lambda x:A(x)==B
def M(A,B):return lambda x:A(B(x))
def L(a,b):return frozenset((B,A)for A in b for B in a)
def J(A,B,C):return tuple(range(A,B,C))
def PJ(A):return max(enumerate(A))[1]
def G(A):return next(iter(A))
def V(A,B):return Q(X(A,B))
def W(A,B):return B(max(A,key=B,default=0))
def PS(b):return not b
def PU(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def U(x):return x
def p(I):I=tuple(map(tuple,I));B=Z(I);C=J(0,9,4);N=L(C,C);O=R(PU,3);Q=R(J,1);D=PP(Q,U,O);S=M(D,G);T=M(D,PJ);X=PP(L,S,T);a=R(P,B);b=R(E,I);F=M(a,b);A=H(X,N);c=W(A,F);K=Y(F,c);d=M(PS,K);e=V(A,K);f=V(A,d);g=PZ(I,B,e);h=PZ(g,0,f);return[*map(list,h)]
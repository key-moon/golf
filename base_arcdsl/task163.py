def PJ(A,B):return type(B)(A(B)for B in B)
def K(A):return type(A)(B for A in A for B in A)
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PS(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def J(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in P(A)if 0<=A<D and 0<=C<E)
def H(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def E(A,B):return frozenset((A,B)for B in P(B))
def PU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Z(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Q(A,B):return K(PJ(A,B))
def PZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def W(A,a,b):return a if A else b
def X(a,b):return frozenset((B,A)for A in b for B in a)
def V(a,b):return a,b
def G(A,B):return B.union(frozenset({A}))
def PE(A):return max(enumerate(A))[1]
def R(A):return next(iter(A))
def U(A):return frozenset({A})
def L(a,b):return a>b
def S(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));K=Y(I,4);B=R(K);C=R(B);D=PE(B);N=L(C,3);O=L(C,7);P=L(D,3);T=L(D,7);a=W(N,4,0);b=W(O,8,a);c=W(P,4,0);d=W(T,8,c);e=V(b,d);f=U(0);g=G(4,f);F=G(8,g);h=X(F,F);i=PU(I,(0,0),(3,3));j=Z(i);k=E(0,j);l=PZ(H,k);m=Q(l,h);n=PS(I,m);o=PU(I,e,(3,3));A=M(o,5,0);p=Y(A,4);q=R(p);r=Z(A);s=J(r,A);t=S(q,4);u=H(s,t);v=PS(n,u);return[*map(list,v)]
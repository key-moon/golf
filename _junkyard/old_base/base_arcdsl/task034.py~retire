def R(A):return type(A)(B for A in A for B in A)
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PS(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def L(A,B):return frozenset((A,B)for B in Z(B))
def J(A):return tuple(map(min,zip(*Z(A))))
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def X(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def G(A,B):return R(PJ(A,B))
def PJ(A,B):return type(B)(A(B)for B in B)
def PZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def V(A,B):return lambda x:A(B(x))
def E(A,B,C):return tuple(range(A,B,C))
def S(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def W(a,b):return type(a)((*a,*b))
def Q(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def K(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def U(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));A=Y(I,2);B=M(I,2,0);C=P(B);F=Y(B,C);D=W(A,F);N=L(C,D);O=V(S,Q);R=J(D);T=K(R);Z=H(A,T);a=PJ(O,Z);b=E(0,9,1);c=X(U,a,b);d=PZ(H,N);e=G(d,c);f=PS(I,e);return[*map(list,f)]
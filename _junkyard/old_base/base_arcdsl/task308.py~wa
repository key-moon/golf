def H(A):return type(A)(B for A in A for B in A)
def X(A):return max(A for(A,B)in Z(A))
def E(A):return max(A for(B,A)in Z(A))
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-L(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-U(A)+1
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return min(A for(B,A)in Z(A))
def U(A):return min(A for(A,B)in Z(A))
def M(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def K(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PX(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in M(A)-{J(A)})
def S(A):
	if len(A)==0:return A
	return PS(A,(-U(A),-L(A)))
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PZ(A):return Q(A),R(A)
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A,B):return H(PL(A,B))
def PL(A,B):return type(B)(A(B)for B in B)
def PY(A,a,b):return lambda x:A(a(x),b(x))
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PP(h,g,f):return lambda x:h(g(f(x)))
def W(A,B):return B(max(A,key=B,default=0))
def PJ(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
def Y(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def V(x):return x
def p(I):I=tuple(map(tuple,I));C=J(I);A=P(I);B=W(A,PZ);D=K(C,B);E=PL(S,A);F=PE(Y,B);H=PP(PJ,F,PZ);L=PY(PS,V,H);M=G(L,E);N=PX(D,M);return[*map(list,N)]
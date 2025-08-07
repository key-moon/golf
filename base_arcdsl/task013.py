def PG(A,B):return type(B)(A(B)for B in B)
def X(A):return max(A for(B,A)in Z(A))
def L(A):return max(A for(A,B)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-J(A)+1
def H(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(min,zip(*Z(A))))
def U(A):return frozenset((B,A[1])for B in range(30))
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def R(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Y(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PL(A):return next(iter(A))[0]
def V(A):return min(A for(B,A)in Z(A))
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in H(A)-{S(A)})
def G(A,B):return frozenset((A,B)for B in Z(B))
def W(A):return PZ(A)>PE(A)
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return X(A)-V(A)+1
def PJ(A,B):return PX(PG(A,B))
def PK(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PY(h,g,f):return lambda x:h(g(f(x)))
def K(A,B):return lambda x:A(B(x))
def PP(A,a,b):return a if A else b
def M(A,B,C):return tuple(range(A,B,C))
def PU(j):return 0,j
def E(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def PX(A):return type(A)(B for A in A for B in A)
def PS(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def Q(x):return x
def p(I):I=tuple(map(tuple,I));D=W(I);B=PP(D,R,Q);A=B(I);C=P(A);F=PX(C);H=PY(PS,E,PE);J=H(F);L=K(U,PU);N=PM(PJ,L);O=PQ(M,J);S=PE(A);T=PQ(O,S);X=PY(N,T,V);Y=PK(G,PL,X);Z=PJ(Y,C);a=PW(A,Z);b=B(a);return[*map(list,b)]
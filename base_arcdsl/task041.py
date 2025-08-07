def G(A,B):return type(B)(A(B)for B in B)
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def Q(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def L(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def U(A,B):return frozenset((A,B)for B in P(B))
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def J(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def Y(A,B):return M(G(A,B))
def R(A,a,b):return lambda x:A(a(x),b(x))
def W(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def S(A,B):return lambda x:A(B(x))
def V(A,B):return type(B)(B for B in B if B!=A)
def M(A):return type(A)(B for A in A for B in A)
def Z(x):return x
def p(I):I=tuple(map(tuple,I));B=L(I);C=V(0,B);A=W(X,I);D=W(J,E);F=R(D,A,A);G=S(M,F);H=R(U,Z,G);K=Y(H,C);N=Q(I,K);return[*map(list,N)]
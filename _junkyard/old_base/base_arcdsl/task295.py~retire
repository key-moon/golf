def Y(A,B):return type(B)(B for B in B if B!=A)
def W(A):return next(iter(A))
def PP(A,B):return type(B)(A(B)for B in B)
def M(A):return type(A)(B for A in A for B in A)
def Z(A):return max(A for(B,A)in P(A))
def S(A):return min(A for(B,A)in P(A))
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def R(A,B):return U(A,(A[0]+42*B[0],A[1]+42*B[1]))
def J(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def PZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def E(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def V(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Z(A)-S(A)+1
def L(A,B):return M(PP(A,B))
def H(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def K(A,B):return W(Y(B,A))
def Q(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
def p(I):I=tuple(map(tuple,I));C=V(I);D=X(I);F=Q(C);A=J(I,F);G=H(R,(1,1));B=K(D,0);M=E(A,B);N=L(G,M);O=PZ(A,B,N);return[*map(list,O)]
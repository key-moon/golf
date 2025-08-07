def M(A,B):return type(A)(A for A in A if B(A))
def R(A):return type(A)(B for A in A for B in A)
def Q(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def U(A):return max(A for(A,B)in P(A))
def S(A):return min(A for(A,B)in P(A))
def J(A):return max(A for(B,A)in P(A))
def X(A):return min(A for(B,A)in P(A))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-S(A)+1
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(max,zip(*P(A))))
def E(A):return tuple(map(min,zip(*P(A))))
def L(A):
	if len(A)==0:return frozenset({})
	B=P(A);C,D=E(B);F,G=Y(A);return frozenset((A,B)for A in range(C,F+1)for B in range(D,G+1))
def PJ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A):return next(iter(A))[0]
def PP(A):return K(A)==len(A)and G(A)==1
def PS(A):return G(A)==len(A)and K(A)==1
def Z(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in Q(A))
def V(A,B):return frozenset((A,B)for B in P(B))
def PU(A,B):return type(B)(A(B)for B in B)
def PE(A,a,b):return lambda x:A(a(x),b(x))
def W(A,B):return R(M(A,B))
def p(I):I=tuple(map(tuple,I));B=Z(I);C=PE(V,H,L);A=PU(C,B);D=W(A,PP);E=W(A,PS);F=PJ(I,D);G=PJ(F,E);return[*map(list,G)]
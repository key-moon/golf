def W(A,B):return type(A)(A for A in A if B(A))
def H(A):return type(A)(B for A in A for B in A)
def G(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def E(A):return max(A for(A,B)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def U(A):return max(A for(B,A)in Z(A))
def L(A):return min(A for(B,A)in Z(A))
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-J(A)+1
def PS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return tuple(map(max,zip(*Z(A))))
def X(A):return tuple(map(min,zip(*Z(A))))
def Y(A):
	if len(A)==0:return frozenset({})
	B=Z(A);C,D=X(B);E,F=V(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def PJ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PP(A):return next(iter(A))[0]
def PZ(A):return R(A)==len(A)and K(A)==1
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in G(A)-{S(A)})
def M(A,B):return frozenset((A,B)for B in Z(B))
def PU(A,B):return type(B)(A(B)for B in B)
def PE(A,a,b):return lambda x:A(a(x),b(x))
def Q(A,B):return H(W(A,B))
def p(I):I=tuple(map(tuple,I));A=P(I);B=PE(M,PP,Y);C=PU(B,A);D=Q(C,PZ);E=PJ(I,D);return[*map(list,E)]
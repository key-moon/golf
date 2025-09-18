def S(A):return max(A for(B,A)in P(A))
def E(A):return min(A for(B,A)in P(A))
def R(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def J(A):return max(A for(A,B)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-Z(A)+1
def PS(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def K(A):return Q(A),G(A)
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A):return tuple(map(min,zip(*P(A))))
def W(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=U(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def X(A):B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);C=tuple(A for(A,B)in enumerate(W(A))if len(set(B))==1);return tuple(tuple(B for(A,B)in enumerate(D)if A not in C)for(A,D)in enumerate(A)if A not in B)
def V(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def L(A,B):return PS(B,U(A),K(A))
def M(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=U(A);J,K=-F,-G;L=R(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return R(frozenset(H),(F,G))
def PZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return S(A)-E(A)+1
def H(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
def p(I):I=tuple(map(tuple,I));B=Y(I,8);A=L(B,I);C=V(I,8,0);D=V(C,1,0);E=X(D);F=G(A);J=H(F);K=M(E,J);N=Y(A,0);O=PZ(K,0,N);return[*map(list,O)]
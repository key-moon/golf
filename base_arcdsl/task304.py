def M(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def U(A):return tuple(map(min,zip(*S(A))))
def X(a,b):return a+b
def Y(a,b):return tuple(A+B for(A,B)in zip(a,b))
def E(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=U(A);J,K=-F,-G;L=V(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return V(frozenset(H),(F,G))
def W(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def L(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def P(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));C=Z(I);D=Y(I,I);B=E(I,3);F=L(B,C);G=J(B);H=P(G,F);A=Y(D,I);K=X(A,A);M=X(K,A);N=W(M,0,H);return[*map(list,N)]
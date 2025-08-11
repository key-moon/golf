def U(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def E(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def J(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Z(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def p(I):I=tuple(map(tuple,I));A=Z(I,2);B=S(I,2,0);C=J(A,(-1,-1));D=E(B,3,C);F=J(A,(-1,1));G=E(D,6,F);H=J(A,(1,-1));K=E(G,8,H);L=J(A,(1,1));M=E(K,7,L);return[*map(list,M)]
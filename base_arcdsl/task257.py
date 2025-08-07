def Y(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def L(A):return tuple(A for A in zip(*A[::-1]))
def Z(A):return X(P(L(A)))
def J(A):return X(U(L(A)))
def P(A):return A[len(A)//2+len(A)%2:]
def U(A):return A[:len(A)//2]
def V(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def p(I):I=tuple(map(tuple,I));A=U(I);B=P(I);C=J(A);D=Z(A);F=J(B);G=Z(B);H=E(D,4);K=E(C,7);L=E(F,8);M=V(G,8,L);N=V(M,4,H);O=V(N,7,K);return[*map(list,O)]
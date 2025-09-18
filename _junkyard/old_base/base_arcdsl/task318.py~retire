def L(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return A[len(A)//2+len(A)%2:]
def J(A):return A[:len(A)//2]
def X(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def Y(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def U(a,b):return a,b
def P(a,b):return a&b
def p(I):I=tuple(map(tuple,I));A=J(I);B=Z(I);C=E(A,0);D=E(B,0);F=P(C,D);G=U(4,4);H=X(3,G);K=Y(H,0,F);return[*map(list,K)]
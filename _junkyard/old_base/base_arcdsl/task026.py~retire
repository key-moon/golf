def M(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):return A[:len(A)//2]
def Z(A):return A[len(A)//2+len(A)%2:]
def Y(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def V(A):return tuple(A for A in zip(*A[::-1]))
def S(A):return Y(Z(V(A)))
def U(A):return Y(E(V(A)))
def L(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def W(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(a,b):return a&b
def p(I):I=tuple(map(tuple,I));A=U(I);B=S(I);C=X(A,0);D=X(B,0);E=P(C,D);F=L(A,9,0);G=W(F,8,E);return[*map(list,G)]
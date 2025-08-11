def E(A):return max(A for(A,B)in J(A))
def U(A):return min(A for(A,B)in J(A))
def S(A):return max(A for(B,A)in J(A))
def X(A):return min(A for(B,A)in J(A))
def W(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return S(A)-X(A)+1
def M(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-U(A)+1
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return A[len(A)//2+len(A)%2:]
def L(A):return A[:len(A)//2]
def V(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def K(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Q(A):return M(A),W(A)
def P(a,b):return a&b
def p(I):I=tuple(map(tuple,I));B=L(I);A=Z(I);C=Q(A);D=Y(B,0);E=Y(A,0);F=P(D,E);G=V(0,C);H=K(G,2,F);return[*map(list,H)]
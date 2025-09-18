def E(A):return max(A for(A,B)in S(A))
def Z(A):return max(A for(B,A)in S(A))
def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return min(A for(B,A)in S(A))
def J(A):return min(A for(A,B)in S(A))
def W(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Z(A)-L(A)+1
def V(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-J(A)+1
def X(A):return frozenset((A[0],B)for B in range(30))
def U(A):return frozenset((B,A[1])for B in range(30))
def M(A):return J(A)+V(A)//2,L(A)+W(A)//2
def G(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(a,b):return a&b
def p(I):I=tuple(map(tuple,I));C=Y(I,2);D=Y(I,8);E=M(C);F=M(D);A=X(E);B=U(F);H=P(A,B);J=G(I,2,A);K=G(J,8,B);L=G(K,4,H);return[*map(list,L)]
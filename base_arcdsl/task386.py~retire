def X(A):return max(A for(A,B)in S(A))
def U(A):return min(A for(A,B)in S(A))
def E(A):return max(A for(B,A)in S(A))
def L(A):return min(A for(B,A)in S(A))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-L(A)+1
def W(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-U(A)+1
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return A[:len(A)//2]
def Z(A):return A[len(A)//2+len(A)%2:]
def Q(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def H(A):return tuple(A for A in zip(*A[::-1]))
def J(A):return Q(Z(H(A)))
def Y(A):return Q(V(H(A)))
def G(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def R(A):return W(A),K(A)
def P(a,b):return a&b
def p(I):I=tuple(map(tuple,I));A=Y(I);B=J(I);C=M(A,0);D=M(B,0);E=P(C,D);F=R(A);H=G(0,F);K=PZ(H,3,E);return[*map(list,K)]
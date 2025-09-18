def J(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def P(A):return max(A for(B,A)in Z(A))
def E(A):return min(A for(B,A)in Z(A))
def M(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def Q(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def W(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def L(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def V(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-E(A)+1
def Y(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-S(A)+1
def X(a,b):return a,b
def p(I):I=tuple(map(tuple,I));A=Y(I);B=V(I);C=L(I,0);D=X(A,1);E=W(I,(0,0),D);F=U(E,B);G=Q(F,0,C);return[*map(list,G)]
def X(A):return max(A for(A,B)in J(A))
def E(A):return min(A for(A,B)in J(A))
def U(A):return max(A for(B,A)in J(A))
def L(A):return min(A for(B,A)in J(A))
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-E(A)+1
def R(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return A[len(A)//2+len(A)%2:]
def V(A):return A[:len(A)//2]
def W(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def H(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def K(A):return Q(A),G(A)
def S(a,b):return type(a)(A for A in a if A not in b)
def P(a,b):return a&b
def Y(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=V(I);D=Z(I);B=M(A,0);C=M(D,0);E=Y(B,C);F=P(B,C);G=S(E,F);J=K(A);L=W(0,J);N=H(L,3,G);return[*map(list,N)]
def V(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return A[len(A)//2+len(A)%2:]
def E(A):return A[:len(A)//2]
def Y(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def M(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def L(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def X(a,b):return a,b
def S(a,b):return type(a)(A for A in a if A not in b)
def P(a,b):return a&b
def U(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=E(I);D=Z(I);F=X(6,5);A=L(C,2);B=L(D,2);G=U(A,B);H=P(A,B);J=S(G,H);K=Y(0,F);N=M(K,3,J);return[*map(list,N)]
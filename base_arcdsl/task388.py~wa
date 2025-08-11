def M(A,B):return type(B)(A(B)for B in B)
def V(A):return type(A)(B for A in A for B in A)
def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def U(A):return frozenset((B,A[1])for B in range(30))
def E(a,b):return a+b
def L(a,b):return tuple(A+B for(A,B)in zip(a,b))
def S(A,B,C):
	G,H=len(A),len(A[0]);I=Z(A);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def Y(A,B):return V(M(A,B))
def p(I):I=tuple(map(tuple,I));C=P(I);D=X(I,C);F=Y(U,D);A=S(I,8,F);B=L(A,A);G=E(B,B);return[*map(list,G)]
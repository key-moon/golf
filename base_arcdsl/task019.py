def W(A,B):return type(B)(A(B)for B in B)
def V(A):return type(A)(B for A in A for B in A)
def M(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def E(a,b):return a+b
def L(a,b):return tuple(A+B for(A,B)in zip(a,b))
def J(A,B,C):
	G,H=len(A),len(A[0]);I=S(A);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def Y(A,B):return V(W(A,B))
def p(I):I=tuple(map(tuple,I));C=P(I);A=L(I,I);B=E(A,A);D=X(B,C);F=Y(Z,D);G=J(B,8,F);return[*map(list,G)]
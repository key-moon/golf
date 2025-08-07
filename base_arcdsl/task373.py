def X(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):return tuple(map(max,zip(*P(A))))
def Z(A):return tuple(map(min,zip(*P(A))))
def E(a,b):return tuple(A+B for(A,B)in zip(a,b))
def J(A):
	if isinstance(A,tuple):return A[::-1]
	B=Z(A)[0]+S(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def L(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def U(a,b):return a,b
def p(I):I=tuple(map(tuple,I));C=U(2,1);B=L(I,(0,0),C);D=J(B);A=E(B,D);F=E(A,A);G=E(F,A);return[*map(list,G)]
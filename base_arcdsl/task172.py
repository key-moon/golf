def E(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):return tuple(map(max,zip(*P(A))))
def Z(A):return tuple(map(min,zip(*P(A))))
def J(a,b):return a+b
def U(A):
	if isinstance(A,tuple):return A[::-1]
	B=Z(A)[0]+S(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def p(I):I=tuple(map(tuple,I));A=U(I);B=J(I,A);return[*map(list,B)]
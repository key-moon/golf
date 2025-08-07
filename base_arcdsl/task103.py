def L(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):return tuple(map(max,zip(*P(A))))
def Z(A):return tuple(map(min,zip(*P(A))))
def E(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def U(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Z(A)[1]+S(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def X(A,a,b):return a if A else b
def J(a,b):return a==b
def p(I):I=tuple(map(tuple,I));A=U(I);B=J(A,I);C=X(B,1,7);D=E(C,(1,1));return[*map(list,D)]
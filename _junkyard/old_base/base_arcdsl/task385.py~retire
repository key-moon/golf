def X(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(A):return tuple(map(max,zip(*Z(A))))
def S(A):return tuple(map(min,zip(*Z(A))))
def P(A):return A[len(A)//2+len(A)%2:]
def U(a,b):return a+b
def E(A):
	if isinstance(A,tuple):return A[::-1]
	B=S(A)[0]+J(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def p(I):I=tuple(map(tuple,I));A=P(I);B=E(A);C=U(B,A);return[*map(list,C)]
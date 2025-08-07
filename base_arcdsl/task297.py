def P(A):return max(A for(B,A)in Z(A))
def U(A):return min(A for(B,A)in Z(A))
def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):return tuple(map(min,zip(*Z(A))))
def E(A):return A[:len(A)//2]
def X(a,b):return a+b
def J(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def Y(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=S(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def G(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def M(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-U(A)+1
def L(a,b):return a,b
def W(A):return type(A)(B for A in A for B in A)
def V(A,B):return tuple(A for B in range(B))
def p(I):I=tuple(map(tuple,I));A=M(I);C=L(2,A);B=G(I,(0,0),C);D=E(B);F=Y(D);H=J(F,A);K=V(H,2);N=W(K);O=X(B,N);return[*map(list,O)]
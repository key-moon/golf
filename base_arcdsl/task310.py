def U(A):return max(A for(A,B)in S(A))
def J(A):return min(A for(A,B)in S(A))
def Z(A):return max(A for(B,A)in S(A))
def X(A):return min(A for(B,A)in S(A))
def M(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Z(A)-X(A)+1
def V(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-J(A)+1
def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def E(A):return tuple(map(min,zip(*S(A))))
def W(A):return V(A),M(A)
def L(A,B):return G(B,E(A),W(A))
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def p(I):I=tuple(map(tuple,I));A=P(I);B=Y(I,A);C=L(B,I);return[*map(list,C)]
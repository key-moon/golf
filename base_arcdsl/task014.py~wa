def Y(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def U(A):return max(A for(A,B)in S(A))
def J(A):return min(A for(A,B)in S(A))
def P(A):return max(A for(B,A)in S(A))
def X(A):return min(A for(B,A)in S(A))
def W(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-X(A)+1
def M(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-J(A)+1
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def E(A):return tuple(map(min,zip(*S(A))))
def Q(A):return M(A),W(A)
def L(A,B):return K(B,E(A),Q(A))
def Z(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in Y(A))
def V(A,B):return min(A,key=B)
def R(A):return len(A)
def p(I):I=tuple(map(tuple,I));A=Z(I);B=V(A,R);C=L(B,I);return[*map(list,C)]
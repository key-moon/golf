def E(A):return tuple(map(max,zip(*Z(A))))
def J(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def P(A):return max(A for(B,A)in Z(A))
def X(A):return min(A for(B,A)in Z(A))
def W(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-X(A)+1
def M(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-S(A)+1
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def U(A):return tuple(map(min,zip(*Z(A))))
def Q(A):return M(A),W(A)
def L(A,B):return K(B,U(A),Q(A))
def V(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=U(A)[1]+E(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def p(I):I=tuple(map(tuple,I));A=V(I);B=Y(I,0);C=L(B,A);return[*map(list,C)]
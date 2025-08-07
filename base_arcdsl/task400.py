def L(A):return tuple(map(max,zip(*P(A))))
def U(A):return max(A for(A,B)in P(A))
def S(A):return min(A for(A,B)in P(A))
def J(A):return max(A for(B,A)in P(A))
def X(A):return min(A for(B,A)in P(A))
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-S(A)+1
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PZ(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def E(A):return tuple(map(min,zip(*P(A))))
def H(A):return K(A),R(A)
def V(A,B):return PZ(B,E(A),H(A))
def Y(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=E(A)[1]+L(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def M(A):
	if isinstance(A,tuple):return A[::-1]
	B=E(A)[0]+L(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def Q(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def W(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def G(A,a,b):return a if A else b
def Z(A,B):return A in B
def p(I):I=tuple(map(tuple,I));C=M(I);D=Y(I);A=W(I,1);B=V(A,C);E=V(A,D);F=Q(B);H=Z(1,F);J=G(H,E,B);return[*map(list,J)]
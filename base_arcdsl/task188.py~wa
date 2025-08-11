def J(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A):return max(A for(B,A)in Z(A))
def U(A):return min(A for(B,A)in Z(A))
def W(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-U(A)+1
def V(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-S(A)+1
def M(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def Q(A):return tuple(A for A in zip(*A[::-1]))
def X(A):return M(L(Q(A)))
def L(A):return A[:len(A)//2]
def E(A):return V(A)>W(A)
def Y(A,a,b):return a if A else b
def p(I):I=tuple(map(tuple,I));A=E(I);B=Y(A,L,X);C=B(I);return[*map(list,C)]
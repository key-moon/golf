def J(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def P(A):return max(A for(B,A)in Z(A))
def E(A):return min(A for(B,A)in Z(A))
def R(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A):return tuple(map(min,zip(*Z(A))))
def V(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=U(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def H(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def L(A):return Q(A)>G(A)
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-E(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-S(A)+1
def K(A,B):return type(B)(A(B)for B in B)
def W(A,a,b):return a if A else b
def Y(a,b):return a,b
def M(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def X(x):return x
def p(I):I=tuple(map(tuple,I));A=L(I);B=W(A,V,X);C=W(A,Q,G);D=C(I);E=Y(1,D);F=B(I);J=H(F,(0,0),E);N=K(M,J);O=B(N);return[*map(list,O)]
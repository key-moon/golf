def V(A,B):return type(A)(A for A in A if B(A))
def M(A):return type(A)(B for A in A for B in A)
def P(A):return max(A for(B,A)in Z(A))
def X(A):return min(A for(B,A)in Z(A))
def U(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A,B):return S(A)==0 or X(A)==0 or U(A)==len(B)-1 or P(A)==len(B[0])-1
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Q(A,B):return type(B)(A(B)for B in B)
def W(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def L(A,B):return M(V(A,B))
def Y(A):return frozenset({A})
def p(I):I=tuple(map(tuple,I));A=J(I);B=Q(Y,A);C=W(E,I);D=L(B,C);F=K(I,8,D);return[*map(list,F)]
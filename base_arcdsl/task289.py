def E(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def L(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def J(A):return tuple(map(min,zip(*P(A))))
def U(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=J(A);K,L=-F,-G;M=X(A,(K,L));H=set()
		for(E,(N,O))in M:
			for P in range(B):
				for Q in range(B):H.add((E,(N*B+P,O*B+Q)))
		return X(frozenset(H),(F,G))
def Z(A):return len(E(A))
def S(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def p(I):I=tuple(map(tuple,I));A=Z(I);B=S(A);C=U(I,B);return[*map(list,C)]
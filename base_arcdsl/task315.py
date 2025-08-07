def Y(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Z(A):return tuple(map(min,zip(*P(A))))
def U(a,b):return a+b
def X(a,b):return tuple(A+B for(A,B)in zip(a,b))
def J(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=Z(A);J,K=-F,-G;M=L(A,(J,K));H=set()
		for(E,(N,O))in M:
			for P in range(B):
				for Q in range(B):H.add((E,(N*B+P,O*B+Q)))
		return L(frozenset(H),(F,G))
def V(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def E(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def S(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));B=J(I,3);C=X(I,I);A=X(C,I);D=U(A,A);F=U(D,A);G=E(B,0);H=E(B,1);K=S(G,H);L=V(F,0,K);return[*map(list,L)]
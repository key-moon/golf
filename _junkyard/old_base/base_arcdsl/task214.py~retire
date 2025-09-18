def J(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def X(A):return type(A)(B for A in A for B in A)
def Y(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def E(A):return tuple(tuple(A[::-1])for A in A[::-1])
def L(A):return tuple(A for A in zip(*A[::-1]))
def P(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def M(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def W(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def S(A,a,b):return X(J(A,a,b))
def V(A,B):return type(B)(A(B)for B in B)
def Z(a,b):return a,b
def U(j):return 0,j
def p(I):I=tuple(map(tuple,I));A=W(I,(0,0),(3,3));B=L(A);C=E(A);D=Z(B,C);F=Z(4,8);G=V(U,F);H=V(P,D);J=S(M,H,G);K=Y(I,J);return[*map(list,K)]
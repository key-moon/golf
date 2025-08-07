def V(A,B):return type(B)(A(B)for B in B)
def E(A):return type(A)(B for A in A for B in A)
def L(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def Z(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def Y(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def J(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def U(A,B):return E(V(A,B))
def X(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def S(A,B):return lambda x:A(B(x))
def P(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def p(I):I=tuple(map(tuple,I));A=J(I,1);B=M(I,(0,0),(3,3));C=Z(B);D=X(Y,C);E=S(D,P);F=U(E,A);G=L(I,F);return[*map(list,G)]
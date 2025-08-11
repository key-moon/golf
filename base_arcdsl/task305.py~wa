def Q(A):return type(A)(B for A in A for B in A)
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(A):return tuple(map(min,zip(*Z(A))))
def H(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def L(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=J(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def E(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in Z(A)if 0<=A<D and 0<=C<E)
def G(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def S(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def V(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def M(A,B):return Q(PP(A,B))
def PP(A,B):return type(B)(A(B)for B in B)
def R(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PZ(a,b):return tuple(zip(a,b))
def U(A,B,C):return tuple(range(A,B,C))
def Y(A):return max(A,default=0)
def P(a,b):return type(a)(A for A in a if A not in b)
def W(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def p(I):I=tuple(map(tuple,I));C=S(I);D=L(I);B=W(9);F=V(PZ,I,D);J=R(PP,Y);A=PP(J,F);K=X(A,0);N=P(C,K);O=E(N,A);Q=U(B,9,1);T=U(9,B,-1);Z=PZ(Q,T);a=R(G,O);b=M(a,Z);c=H(A,b);return[*map(list,c)]
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def W(A):return tuple(A for A in zip(*A[::-1]))
def S(A):return M(P(W(A)))
def X(A):return M(Y(W(A)))
def P(A):return A[len(A)//2+len(A)%2:]
def Y(A):return A[:len(A)//2]
def Q(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def L(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in J(A)if 0<=A<D and 0<=C<E)
def V(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def R(A,a,b):return lambda x:A(a(x),b(x))
def G(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def Z(a,b):return type(a)(A for A in a if A not in b)
def E(x):return x
def p(I):I=tuple(map(tuple,I));B=X(I);C=S(I);D=Y(B);F=P(B);H=Y(C);J=P(C);K=G(V,0);M=R(Z,U,K);A=R(L,M,E);N=A(H);O=A(F);T=A(J);W=Q(D,T);a=Q(W,O);b=Q(a,N);return[*map(list,b)]
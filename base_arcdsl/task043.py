def E(A,B):return lambda x:A(B(x))
def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Z(A,B,C):
	G,H=len(A),len(A[0]);I=P(A);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def J(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def L(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def W(A,B):return type(B)(A(B)for B in B)
def K(A,a,b):return lambda x:A(a(x),b(x))
def M(A,n):
	if n==1:return A
	return E(A,M(A,n-1))
def U(a,b):return frozenset((B,A)for A in b for B in a)
def X(a,b):return a,b
def Y(A,B):return type(B)(B for B in B if B!=A)
def G(A):return max(enumerate(A))[1]
def V(A):return next(iter(A))
def p(I):I=tuple(map(tuple,I));A=L(I,5);B=U(A,A);C=M(V,2);D=M(G,2);E=K(X,C,D);F=W(E,B);H=J(A);N=Y(H,F);O=Z(I,2,N);return[*map(list,O)]
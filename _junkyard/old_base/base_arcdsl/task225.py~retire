def PU(A,B):return type(B)(A(B)for B in B)
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def R(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Y(A):return tuple(map(max,zip(*J(A))))
def V(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=L(A)[1]+Y(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def L(A):return tuple(map(min,zip(*J(A))))
def U(A):return frozenset((A[0],B)for B in range(30))
def X(A):return frozenset((B,A[1])for B in range(30))
def G(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=L(A);J,K=-F,-G;M=PS(A,(J,K));H=set()
		for(E,(N,O))in M:
			for P in range(B):
				for Q in range(B):H.add((E,(N*B+P,O*B+Q)))
		return PS(frozenset(H),(F,G))
def S(A,B):
	G,H=len(A),len(A[0]);I=E(A);C=list(list(A)for A in A)
	for(J,(D,F))in B:
		if 0<=D<G and 0<=F<H:
			if C[D][F]==I:C[D][F]=J
	return tuple(tuple(A)for A in C)
def PX(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return V(K(V(A)))
def K(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=L(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in R(A)-{E(A)})
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def H(A,B):return PP(PU(A,B))
def PE(A,a,b):return lambda x:A(a(x),b(x))
def PZ(h,g,f):return lambda x:h(g(f(x)))
def W(a,b):return a,b
def PP(A):return type(A)(B for A in A for B in A)
def Z(a,b):return type(a)(A for A in a if A not in b)
def Q(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=P(I);D=PZ(M,K,PP);A=D(C);E=G(A,3);F=W(-2,-2);L=PS(E,F);N=S(I,L);B=J(A);O=PE(Q,U,X);R=H(O,B);T=Z(R,B);V=PX(N,0,T);return[*map(list,V)]
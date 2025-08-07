def PY(A,B):return type(B)(A(B)for B in B)
def PS(A):return type(A)(B for A in A for B in A)
def X(A):return tuple(map(min,zip(*Z(A))))
def E(A):return max(A for(A,B)in Z(A))
def U(A):return max(A for(B,A)in Z(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-J(A)+1
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return min(A for(B,A)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def S(A):
	if len(A)==0:return A
	return PU(A,(-J(A),-L(A)))
def PJ(A):return R(A),PZ(A)
def P(A,B):
	C=set();K=S(B);D,E=len(A),len(A[0]);L,M=PJ(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in PU(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
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
		F,G=X(A);J,K=-F,-G;L=PU(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return PU(frozenset(H),(F,G))
def PL(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PV(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def V(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in Z(A)if 0<=A<D and 0<=C<E)
def PU(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def W(A,B):return frozenset((A,B)for B in Z(B))
def H(A,B):return PS(PY(A,B))
def PX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def K(A,a,b):return a if A else b
def Q(a,b):return a,b
def PP(A,B):return B.union(frozenset({A}))
def M(A):return frozenset({A})
def Y(a,b):return a==b
def PM(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));E=M((0,0));F=W(0,E);C=G(F,2);J=P(I,C);L=PX(PU,C);N=H(L,J);A=PV(I,2,N);O=PM(6,6);B=Q(8,O);R=PE(A,B);S=Y(R,2);T=M(B);U=PM(B,(1,0));D=PP(U,T);X=V(D,A);Z=V(D,I);a=K(S,Z,X);b=PL(A,a);return[*map(list,b)]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PU(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def W(A):return tuple(map(max,zip(*J(A))))
def V(A):return tuple(map(min,zip(*J(A))))
def M(A):
	if len(A)==0:return frozenset({})
	B=J(A);C,D=V(B);E,F=W(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PX(B):
	if len(B)==0:return frozenset({})
	return M(B)-J(B)
def Y(A,B):
	E,I=len(A),len(A[0]);C=tuple()
	for D in range(E):
		F=tuple()
		for H in range(I):
			if H%B==0:F=F+(A[D][H],)
		C=C+(F,)
	E=len(C);G=tuple()
	for D in range(E):
		if D%B==0:G=G+(C[D],)
	return G
def PP(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=V(A);J,K=-F,-G;L=PU(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return PU(frozenset(H),(F,G))
def PY(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PW(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def L(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def Q(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();P,Q=len(A),len(A[0]);R=U(A);S=X if C else Z
	for F in R:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in S(G)if 0<=A<P and 0<=B<Q}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PZ(A,B):return PS(PV(A,B))
def PV(A,B):return type(B)(A(B)for B in B)
def PM(A,a,b):return lambda x:A(a(x),b(x))
def PL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def H(A,B):return lambda x:A(B(x))
def K(a,b):return frozenset((B,A)for A in b for B in a)
def PQ(A):return max(enumerate(A))[1]
def PJ(A):return next(iter(A))
def G(A,B):return type(A)(A for A in A if B(A))
def PS(A):return type(A)(B for A in A for B in A)
def R(a,b):return a>b
def p(I):B=True;I=tuple(map(tuple,I));C=PP(I,2);D=Q(C,B,B,B);A=P(D,2);E=PM(L,PJ,PQ);F=PL(R,5);J=H(F,E);M=K(A,A);N=G(M,J);O=PV(PS,N);S=PZ(PX,O);T=PW(C,4,S);U=PS(A);V=PY(T,U);W=Y(V,2);return[*map(list,W)]
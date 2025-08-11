def Y(A):return max(A for(B,A)in S(A))
def W(A):return min(A for(B,A)in S(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return min(A for(A,B)in S(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PV(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PE(A):return PS(A),PJ(A)
def R(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def G(A,B):return PV(B,M(A),PE(A))
def H(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=M(A);J,K=-F,-G;L=PX(A,(J,K));H=set()
		for(E,(N,O))in L:
			for P in range(B):
				for Q in range(B):H.add((E,(N*B+P,O*B+Q)))
		return PX(frozenset(H),(F,G))
def PY(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def V(A):return max(A for(A,B)in S(A))
def Q(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();Q,R=len(A),len(A[0]);S=U(A);T=X if C else P
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def J(A):
	if len(A)==0:return A
	return PX(A,(-L(A),-W(A)))
def PX(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A):return tuple(map(min,zip(*S(A))))
def K(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PP(A,B):return max(A,key=B)
def PU(A):return type(A)(B for A in A for B in A)
def PZ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a//b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]//b[0],a[1]//b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a//b[0],a//b[1]
	return a[0]//b,a[1]//b
def p(I):E=False;A=True;I=tuple(map(tuple,I));F=Q(I,E,A,A);L=K(I,4);B=G(L,I);C=PP(F,V);N=J(C);O=R(B,4,0);P=Q(O,A,E,A);D=PU(P);S=PJ(D);T=M(D);U=PJ(C);W=PZ(S,U);X=H(N,W);Y=PX(X,T);Z=PY(B,Y);return[*map(list,Z)]
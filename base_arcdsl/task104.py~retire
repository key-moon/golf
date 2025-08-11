def V(A):return max(A for(A,B)in S(A))
def L(A):return min(A for(A,B)in S(A))
def Y(A):return max(A for(B,A)in S(A))
def W(A):return min(A for(B,A)in S(A))
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PM(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return tuple(map(min,zip(*S(A))))
def PJ(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
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
		F,G=M(A);J,K=-F,-G;L=PV(A,(J,K));H=set()
		for(E,(N,O))in L:
			for P in range(B):
				for Q in range(B):H.add((E,(N*B+P,O*B+Q)))
		return PV(frozenset(H),(F,G))
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PS(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PU(A):return tuple(tuple(A[::-1])for A in A[::-1])
def PL(A):return tuple(A for A in zip(*A[::-1]))
def G(A,B,C,D):
	M=U(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);V=E if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in V(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def PV(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PX(A):return PZ(A),PE(A)
def PP(A,a,b):return a if A else b
def K(a,b):return a,b
def PY(A):return next(iter(A))
def Q(A):return frozenset({A})
def R(a,b):return type(a)((*a,*b))
def X(A,B):return A in B
def p(I):D=False;I=tuple(map(tuple,I));E=G(I,D,D,True);F=PY(E);B=S(F);J=X((0,2),B);L=X((2,2),B);M=X((2,0),B);N=K(9,9);O=PJ(0,N);P=K(3,(0,0));T=Q(P);U=H(T,2);C=H(U,2);V=PX(C);W=PV(C,V);Y=R(C,W);A=PW(O,Y);Z=PL(A);a=PU(A);b=PS(A);c=PP(J,Z,A);d=PP(L,a,c);e=PP(M,b,d);return[*map(list,e)]
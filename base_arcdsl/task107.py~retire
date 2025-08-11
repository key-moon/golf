def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def H(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PU(A,B):return G(A,(A[0]+42*B[0],A[1]+42*B[1]))
def R(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=V(A);J,K=-F,-G;L=PS(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return PS(frozenset(H),(F,G))
def Y(A,B,C):
	H,I=len(A),len(A[0]);J=E(A);D=list(list(A)for A in A)
	for(F,G)in S(C):
		if 0<=F<H and 0<=G<I:
			if D[F][G]==J:D[F][G]=B
	return tuple(tuple(A)for A in D)
def PE(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def U(A):return len(H(A))
def Q(A,B,C,D):
	M=E(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);U=X if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in U(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def M(A):return tuple(map(max,zip(*S(A))))
def W(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def V(A):return tuple(map(min,zip(*S(A))))
def L(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def PP(A,B):return min(A,key=B)
def PZ(A,B):return max(A,key=B)
def PX(A):return len(A)
def K(a,b):return type(a)((*a,*b))
def p(I):B=True;A=False;I=tuple(map(tuple,I));H=U(I);J=L(H);C=R(I,J);N=Q(C,A,A,B);D=PP(N,PX);E=V(D);F=W(D);O=PU(E,(-1,-1));P=PU(E,(1,1));S=PU(F,(1,-1));T=PU(F,(-1,1));X=K(O,P);Z=K(S,T);a=K(X,Z);G=Y(C,2,a);b=Q(G,B,A,B);c=PZ(b,M);d=PE(G,c);return[*map(list,d)]
def L(A):return max(A for(B,A)in S(A))
def W(A):return min(A for(B,A)in S(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return max(A for(A,B)in S(A))
def X(A):return min(A for(A,B)in S(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PL(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def M(A):return tuple(map(min,zip(*S(A))))
def PJ(A):return PZ(A),PS(A)
def G(A,B):return PL(B,M(A),PJ(A))
def V(A,B):
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
def PX(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Q(A,B,C,D):
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
def K(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-W(A)+1
def R(A,B):return min(A,key=B)
def H(A,B):return max(A,key=B)
def PE(A):return len(A)
def PP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a//b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]//b[0],a[1]//b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a//b[0],a//b[1]
	return a[0]//b,a[1]//b
def p(I):I=tuple(map(tuple,I));A=Q(I,False,True,True);D=H(A,PE);E=R(A,PE);B=G(D,I);C=G(E,I);F=PS(B);J=PS(C);L=PP(F,J);M=V(B,L);N=K(M,0);O=PX(C,0,N);return[*map(list,O)]
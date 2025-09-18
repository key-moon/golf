def PY(A):return next(iter(A))
def V(A):return max(A for(A,B)in S(A))
def X(A):return min(A for(A,B)in S(A))
def L(A):return max(A for(B,A)in S(A))
def W(A):return min(A for(B,A)in S(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PP(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PW(A,B):return PP(A,(A[0]+42*B[0],A[1]+42*B[1]))
def Y(A,B,C):
	G,H=len(A),len(A[0]);I=U(A);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PL(A):return next(iter(A))[0]
def PS(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def H(A,B,C,D):
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
def G(A):return tuple(map(max,zip(*S(A))))
def R(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def K(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def M(A):return tuple(map(min,zip(*S(A))))
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-W(A)+1
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-X(A)+1
def PQ(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):return PY(PE(B,A))
def PE(A,B):return type(B)(B for B in B if B!=A)
def PJ(A,B):return max(A,key=B)
def PZ(a,b):return type(a)((*a,*b))
def Q(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):B=True;I=tuple(map(tuple,I));C=PS(I);D=H(I,B,B,B);E=PQ(Q,PU,PX);A=PJ(D,E);F=PL(A);J=PE(0,C);L=PM(J,F);N=G(A);O=R(A);P=K(A);S=M(A);T=PW(N,(1,1));U=PW(O,(1,-1));V=PW(P,(-1,1));W=PW(S,(-1,-1));X=PZ(T,U);Z=PZ(V,W);a=PZ(X,Z);b=Y(I,L,a);return[*map(list,b)]
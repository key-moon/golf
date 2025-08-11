def PG(A,B):return type(B)(A(B)for B in B)
def PL(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Q(A):return tuple(map(max,zip(*S(A))))
def V(A):return tuple(map(min,zip(*S(A))))
def Y(A):return max(A for(A,B)in S(A))
def L(A):return max(A for(B,A)in S(A))
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return min(A for(B,A)in S(A))
def X(A):return min(A for(A,B)in S(A))
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-M(A)+1
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def H(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PM(A,B):return H(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PU(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PE(A):return X(A)+PS(A)//2,M(A)+PX(A)//2
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def R(A):
	if isinstance(A,tuple):return A[::-1]
	B=V(A)[0]+Q(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def PY(A):return next(iter(A))[0]
def K(A,B,C,D):
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
def G(A,B):return frozenset((A,B)for B in S(B))
def PJ(A,B):return PL(PG(A,B))
def PR(A,a,b):return lambda x:A(a(x),b(x))
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,B):return lambda x:A(B(x))
def PZ(a,b):return a,b
def PK(A):return len(A)
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));A=K(I,True,False,True);C=PK(A);B=W(C,5);D=PZ(B,B);E=PU(0,D);F=PQ(PM,(1,1));H=PP(F,PE);J=PR(G,PY,H);L=PJ(J,A);M=PW(E,L);N=R(M);return[*map(list,N)]
def R(A,B):return type(A)(A for A in A if B(A))
def PX(A):return type(A)(B for A in A for B in A)
def M(A):return max(A for(A,B)in S(A))
def L(A):return min(A for(A,B)in S(A))
def V(A):return max(A for(B,A)in S(A))
def Q(A):return min(A for(B,A)in S(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PH(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def W(A):return tuple(map(min,zip(*S(A))))
def PY(A):return PU(A),PE(A)
def PK(A):return tuple(A[1:-1]for A in A[1:-1])
def PS(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def H(A,B):return PH(B,W(A),PY(A))
def PR(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PJ(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
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
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-Q(A)+1
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-L(A)+1
def PG(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PW(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PL(h,g,f):return lambda x:h(g(f(x)))
def PZ(A,B):return lambda x:A(B(x))
def PP(A,B):return PX(R(A,B))
def Y(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def PQ(A):return len(A)
def X(A,B):return A in B
def G(a,b):return a==b
def ZP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));A=K(I,True,False,True);B=PW(H,I);C=PL(PJ,PK,B);D=PM(X,3);E=PZ(D,C);F=PG(ZP,PU,PE);J=PZ(Y,F);L=PG(G,PQ,J);M=PP(A,E);N=PP(A,L);O=PS(I,3,6);P=PR(O,2,M);Q=PR(P,1,N);return[*map(list,Q)]
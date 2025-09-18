def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def L(A):return tuple(map(max,zip(*S(A))))
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return tuple(map(min,zip(*S(A))))
def R(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=X(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def M(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=X(A)[1]+L(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PP(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def G(a,b):return a+b
def W(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return M(R(M(A)))
def PS(A):return next(iter(A))[0]
def V(A,B,C,D):
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
def PY(A,B):return type(B)(A(B)for B in B)
def PM(A,a,b):return lambda x:A(a(x),b(x))
def PX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PJ(h,g,f):return lambda x:h(g(f(x)))
def Q(A,B):return lambda x:A(B(x))
def K(a,b):return a,b
def H(A,B):return B(max(A,key=B,default=0))
def PZ(A):return type(A)(B for A in A for B in A)
def PV(A):return len(A)
def PU(A,B):return tuple(sorted(A,key=B))
def Y(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):C=False;I=tuple(map(tuple,I));A=V(I,True,C,C);D=PU(A,PV);E=H(A,PV);B=PL(K,1);F=PX(Y,E);J=Q(B,PV);L=PJ(B,F,PV);M=PM(PP,PS,J);N=PX(PP,0);O=Q(N,L);P=PM(G,M,O);R=Q(W,P);S=PY(R,D);T=PZ(S);U=W(T);return[*map(list,U)]
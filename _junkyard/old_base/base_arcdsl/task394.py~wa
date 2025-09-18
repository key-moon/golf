def H(A,B):return type(A)(A for A in A if B(A))
def PG(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return tuple(map(min,zip(*S(A))))
def PR(A):return PV(A),PQ(A)
def ZX(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def V(A):return max(A for(B,A)in S(A))
def PQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-Q(A)+1
def M(A):return max(A for(A,B)in S(A))
def ZP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in S(A))
def Y(A):return min(A for(A,B)in S(A))
def J(A):
	if len(A)==0:return A
	return PH(A,(-Y(A),-Q(A)))
def PV(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-Y(A)+1
def PL(A):
	B=J(A);D=PV(B)
	for C in range(1,D):
		E=PH(B,(-C,0));F=frozenset({(B,(A,C))for(B,(A,C))in E if A>=0})
		if F.issubset(B):return C
def PP(A):
	B=J(A);C=PQ(B)
	for D in range(1,C):
		E=PH(B,(0,-D));F=frozenset({(B,(C,A))for(B,(C,A))in E if A>=0})
		if F.issubset(B):return D
	return C
def PY(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(ZX(A,(B*C+C*E,0),(B,D))for C in range(n))
def PW(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(ZX(A,(0,B*C+C*E),(D,B))for C in range(n))
def PZ(A,B):return ZX(B,W(A),PR(A))
def ZS(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def K(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PX(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def R(A,B,C,D):
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
def X(A):return P(A)|Z(A)
def PH(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PS(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PM(A,B):return PG(ZU(A,B))
def ZU(A,B):return type(B)(A(B)for B in B)
def ZZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PK(h,g,f):return lambda x:h(g(f(x)))
def PE(a,b):return a,b
def PJ(A,B):return next(A for A in A if B(A))
def PU(A,B):return PG(H(A,B))
def L(A,B):return A in B
def ZE(b):return not b
def G(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):B=False;I=tuple(map(tuple,I));C=R(I,True,B,B);D=PS(I,0);E=ZZ(L,0);A=PK(ZE,E,PX);F=PU(C,A);H=PY(I,2);J=PW(I,2);M=PJ(H,A);N=PJ(J,A);O=K(M);P=K(N);Q=PL(O);S=PP(P);T=X((0,0));U=PM(X,T);V=PE(Q,S);W=ZJ(G,V);Y=ZU(W,U);Z=ZZ(PH,F);a=PM(Z,Y);b=ZS(I,a);c=PZ(D,b);return[*map(list,c)]
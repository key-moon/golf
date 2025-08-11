def PL(A):return type(A)(B for A in A for B in A)
def V(A):return max(A for(B,A)in S(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return max(A for(A,B)in S(A))
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A):return min(A for(B,A)in S(A))
def L(A):return min(A for(A,B)in S(A))
def J(A):
	if len(A)==0:return A
	return PM(A,(-L(A),-W(A)))
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-L(A)+1
def PP(A):
	B=J(A);D=PJ(B)
	for C in range(1,D):
		E=PM(B,(-C,0));F=frozenset({(B,(A,C))for(B,(A,C))in E if A>=0})
		if F.issubset(B):return C
def PE(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
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
def PM(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def K(A):return PJ(A)>PX(A)
def PY(A):return PJ(A),PX(A)
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-W(A)+1
def PU(A,B):return PL(PK(A,B))
def PK(A,B):return type(B)(A(B)for B in B)
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PZ(A,a,b):return a if A else b
def H(a,b):return a,b
def G(A,B,C):return tuple(range(A,B,C))
def PV(A):return next(iter(A))
def PS(i):return i,0
def Y(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def Q(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PR(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):B=True;I=tuple(map(tuple,I));C=PX(I);D=R(I,B,B,B);A=PV(D);E=PP(A);F=PS(E);J=G(0,9,1);L=PQ(Q,F);M=PK(L,J);N=PQ(PM,A);O=PU(N,M);P=H(C,C);S=K(A);T=PY(A);U=PR((1,0),T);V=Y(U);W=PM(A,V);X=PZ(S,O,W);Z=PE(0,P);a=PG(Z,A);b=PG(a,X);return[*map(list,b)]
def PR(A,B):return type(B)(A(B)for B in B)
def PX(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def V(A):return max(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return min(A for(B,A)in J(A))
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-M(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PQ(A,B):return R(A,(A[0]+42*B[0],A[1]+42*B[1]))
def R(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PJ(A):return L(A)+PP(A)//2,M(A)+PE(A)//2
def P(A,B):
	G,H=len(A),len(A[0]);I=E(A);C=list(list(A)for A in A)
	for(J,(D,F))in B:
		if 0<=D<G and 0<=F<H:
			if C[D][F]==I:C[D][F]=J
	return tuple(tuple(A)for A in C)
def PG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PL(A):return next(iter(A))[0]
def L(A):return min(A for(A,B)in J(A))
def K(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();P,Q=len(A),len(A[0]);R=U(A);S=X if C else Z
	for F in R:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in S(G)if 0<=A<P and 0<=B<Q}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def G(A,B):return frozenset((A,B)for B in J(B))
def W(A):return tuple(map(max,zip(*J(A))))
def PY(A):return PP(A),PE(A)
def PZ(A,B):return PX(PR(A,B))
def PH(A,a,b):return lambda x:A(a(x),b(x))
def PK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def H(A,B):return lambda x:A(B(x))
def ZP(a,b):return tuple(zip(a,b))
def PU(A,B):return type(B)(B for B in B if B!=A)
def PS(A,B):return B.union(frozenset({A}))
def ZZ(A):return max(enumerate(A))[1]
def PV(A):return next(iter(A))
def Q(A):return frozenset({A})
def PM(A,B):return tuple(sorted(A,key=B))
def ZS(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):E=False;A=True;I=tuple(map(tuple,I));F=PY(I);J=K(I,A,E,A);M=PK(PQ,(0,1));N=H(M,PJ);O=PH(G,PL,N);S=PZ(O,J);C=PG(I,S);T=ZS(F,(1,-1));U=Q(T);D=G(0,U);V=K(C,A,E,A);X=PS(D,V);B=PM(X,L);Y=PV(B);Z=PU(D,B);a=PU(Y,B);b=H(W,PV);c=H(W,ZZ);d=PH(R,b,c);e=H(PL,PV);f=PH(G,e,d);g=ZP(Z,a);h=PZ(f,g);i=P(C,h);return[*map(list,i)]
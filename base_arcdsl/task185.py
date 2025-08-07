def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def ZU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Q(A)-PP(A)+1
def SJ(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def ZV(A):return ZZ(A),ZU(A)
def PS(A):return tuple(map(max,zip(*E(A))))
def PE(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*E(A)))))
def PJ(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*E(A)))))
def H(A):return tuple(map(min,zip(*E(A))))
def ZW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return max(A for(B,A)in E(A))
def PP(A):return min(A for(B,A)in E(A))
def K(A):return max(A for(A,B)in E(A))
def W(A):return min(A for(A,B)in E(A))
def G(A):C,D=len(A),len(A[0]);B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);E=tuple(A for(A,B)in enumerate(PR(A))if len(set(B))==1);F=frozenset({frozenset({(A[B][C],(B,C))for C in range(D)})for B in B});G=frozenset({frozenset({(A[C][B],(C,B))for C in range(C)})for B in E});return F|G
def ZP(A):F,G=W(A)-1,PP(A)-1;H,I=K(A)+1,Q(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|L)
def PL(A):return frozenset({H(A),PJ(A),PE(A),PS(A)})
def PW(A,B):return SJ(B,H(A),ZV(A))
def R(A,B):
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
def ZG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PR(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=H(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PX(A,B):D,F=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in E(A)if 0<=A<D and 0<=C<F)
def ZX(A):return next(iter(A))[0]
def L(A):return len(PQ(A))
def PQ(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Z(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PQ(A)-{Y(A)})
def PV(A,B,C,D):
	K=Y(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=X(A);R=V if C else S
	for E in Q:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		M={(H,E)};I={E}
		while len(I)>0:
			N=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:M.add((J,F));G.add(F);N|={(A,B)for(A,B)in R(F)if 0<=A<O and 0<=B<P}
			I=N-G
		L.add(frozenset(M))
	return frozenset(L)
def PY(A,B):return frozenset((A,B)for B in E(B))
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def ZZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return K(A)-W(A)+1
def ZS(A,B):return ZE(ZR(A,B))
def ZR(A,B):return type(B)(A(B)for B in B)
def SP(A,a,b):return lambda x:A(a(x),b(x))
def ZL(A,n):
	if n==1:return A
	return PK(A,ZL(A,n-1))
def ZQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PG(A,B):return lambda x:A(x)==B
def ZY(h,g,f):return lambda x:h(g(f(x)))
def PK(A,B):return lambda x:A(B(x))
def SS(a,b):return tuple(zip(a,b))
def PZ(A,B,C):return tuple(range(A,B,C))
def ZJ(A,B):return type(B)(B for B in B if B!=A)
def SU(A):return max(enumerate(A))[1]
def ZM(A):return next(iter(A))
def PM(A,B):return type(A)(A for A in A if B(A))
def U(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def SE(a,b):return a and b
def PH(A,B):return max(A,key=B)
def ZE(A):return type(A)(B for A in A for B in A)
def ZH(A):return len(A)
def M(A,B):return A in B
def SZ(b):return not b
def PU(x):return x
def p(I):H=False;I=tuple(map(tuple,I));C=Z(I);J=PH(C,ZH);K=ZJ(J,C);N=ZE(K);A=PW(N,I);O=ZY(ZX,ZE,G);Q=O(I);S=PV(A,True,H,H);D=P(S,0);T=ZK(PX,A);B=ZY(T,PL,ZP);V=ZQ(M,Q);W=ZY(V,PQ,B);X=PK(L,B);Y=PK(SZ,W);a=PG(X,1);b=SP(SE,Y,a);c=PM(D,b);d=PK(ZX,B);e=SP(PY,d,PU);f=ZS(e,c);g=ZG(A,f);h=ZM(D);E=ZZ(h);F=ZZ(A);i=U(E);j=PZ(0,F,i);k=PZ(0,F,1);l=ZK(M,j);m=ZY(SZ,l,SU);n=ZQ(ZR,ZM);o=ZK(PM,m);p=ZK(SS,k);q=ZY(n,o,p);r=PK(PR,q);s=ZL(r,2);t=s(g);u=R(t,E);return[*map(list,u)]
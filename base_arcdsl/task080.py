def PU(A,B):return lambda x:A(B(x))
def PW(A):return type(A)(B for A in A for B in A)
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def ZP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A):return max(A for(B,A)in E(A))
def K(A):return min(A for(B,A)in E(A))
def Q(A):return max(A for(A,B)in E(A))
def V(A):return min(A for(A,B)in E(A))
def PX(A):F,G=V(A)-1,K(A)-1;H,I=Q(A)+1,W(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|L)
def ZS(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PZ(A,B):D,F=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in E(A)if 0<=A<D and 0<=C<F)
def PQ(A):return next(iter(A))[0]
def PJ(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def Z(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PJ(A)-{L(A)})
def PS(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);T=Y if C else S
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in T(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def PR(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def ZY(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def G(A):return tuple(map(min,zip(*E(A))))
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PK(A):return PL(A),PM(A)
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PY(A,B):return PW(ZE(A,B))
def ZE(A,B):return type(B)(A(B)for B in B)
def ZU(A,n):
	if n==1:return A
	return PU(A,ZU(A,n-1))
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
def PG(h,g,f):return lambda x:h(g(f(x)))
def PV(A,B):return type(B)(B for B in B if B!=A)
def ZL(A):return max(enumerate(A))[1]
def M(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def U(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PE(A,B):return max(A,key=B)
def ZX(A):return len(A)
def PH(A,B):return tuple(sorted(A,key=B))
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZV(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));E=Z(I);F=PS(I,True,False,True);B=PH(E,PL);J=ZL(B);K=PV(J,B);N=ZL(K);O=PQ(N);C=P(F,O);Q=ZU(PX,2);S=ZJ(PZ,I);T=L(I);V=ZZ(PV,T);W=PG(ZX,V,PJ);X=PG(W,S,Q);D=PE(C,X);Y=G(D);A=PK(D);a=PP(Y,A);b=M(a);c=R(A,3);d=ZV(c,(2,2));e=ZY(I,b,d);f=H(e);g=ZE(G,C);h=U(A);i=ZJ(PP,h);j=ZE(i,g);k=ZZ(PR,f);l=PY(k,j);m=ZS(I,l);return[*map(list,m)]
def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return J(A)|U(A)
def J(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def L(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def ZS(A,B):
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
def M(A):return min(A for(A,B)in E(A))
def PW(A):F,G=M(A)-1,K(A)-1;H,I=Q(A)+1,W(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|L)
def PL(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for J in A:
			D=tuple()
			for E in J:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,H=G(A);K,L=-F,-H;M=ZZ(A,(K,L));I=set()
		for(E,(N,O))in M:
			for P in range(B):
				for Q in range(B):I.add((E,(N*B+P,O*B+Q)))
		return ZZ(frozenset(I),(F,H))
def ZU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PP(A,B):D,F=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in E(A)if 0<=A<D and 0<=C<F)
def PU(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PS(A,B,C,D):
	M=Y(A)if D else None;N=set();G=set();Q,R=len(A),len(A[0]);S=L(A);T=V if C else J
	for E in S:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==M:continue
		O={(H,E)};I={E}
		while len(I)>0:
			P=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=M:O.add((K,F));G.add(F);P|={(A,B)for(A,B)in T(F)if 0<=A<Q and 0<=B<R}
			I=P-G
		N.add(frozenset(O))
	return frozenset(N)
def X(A):
	if len(A)==0:return A
	return ZZ(A,(-M(A),-K(A)))
def ZZ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PZ(A,B):return frozenset((A,B)for B in E(B))
def G(A):return tuple(map(min,zip(*E(A))))
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def Z(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def PK(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PQ(A,B):return PR(ZX(A,B))
def ZX(A,B):return type(B)(A(B)for B in B)
def ZL(A,a,b):return lambda x:A(a(x),b(x))
def ZJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PE(A,B):return lambda x:A(x)==B
def PH(h,g,f):return lambda x:h(g(f(x)))
def PX(A,B):return lambda x:A(B(x))
def PG(A,B):return type(B)(B for B in B if B!=A)
def ZP(A):return next(iter(A))
def PJ(A,B):return type(A)(A for A in A if B(A))
def PM(A,B):return max(A,key=B)
def PY(Aa):return min(Aa,default=0)
def PV(A):return max(A,default=0)
def PR(A):return type(A)(B for A in A for B in A)
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def H(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):J=False;A=True;I=tuple(map(tuple,I));K=PS(I,J,A,A);B=PS(I,A,J,A);L=ZJ(ZJ,Z);C=ZL(ZX,L,PU);M=PX(PV,C);N=PX(PY,C);O=ZL(H,M,N);D=PM(K,O);E=S(D);F=X(D);Q=PE(ZP,E);T=PJ(F,Q);U=G(T);V=P(B,E);W=ZE(PP,I);Y=ZJ(PG,0);a=PH(ZP,Y,PU);b=PH(a,W,PW);c=ZJ(R,U);d=PX(c,PK);e=ZL(H,G,d);f=ZJ(ZZ,F);g=PX(f,e);h=ZL(PL,g,PK);i=ZL(PZ,b,h);j=PQ(i,V);k=ZU(I,j);l=PR(B);m=ZU(k,l);return[*map(list,m)]
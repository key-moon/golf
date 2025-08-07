def PE(A,B):return lambda x:A(B(x))
def ZS(A,B):return type(B)(A(B)for B in B)
def PQ(A):return type(A)(B for A in A for B in A)
def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return J(A)|U(A)
def J(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PH(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return max(A for(B,A)in E(A))
def R(A):return min(A for(B,A)in E(A))
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Q(A)-R(A)+1
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-M(A)+1
def ZX(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PG(A):return PL(A),PW(A)
def L(A):return frozenset((A[0],B)for B in range(30))
def W(A):return frozenset((B,A[1])for B in range(30))
def ZU(A):return tuple(A[1:-1]for A in A[1:-1])
def PZ(A,B):return ZX(B,K(A),PG(A))
def ZE(A,B,C):
	H,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(F,G)in E(C):
		if 0<=F<H and 0<=G<I:D[F][G]=B
	return tuple(tuple(A)for A in D)
def PS(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def G(A):return max(A for(A,B)in E(A))
def M(A):return min(A for(A,B)in E(A))
def H(A,B,C,D):
	L=Y(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);S=V if C else J
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==L:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=L:N.add((K,F));G.add(F);O|={(A,B)for(A,B)in S(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def PR(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def K(A):return tuple(map(min,zip(*E(A))))
def PJ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PV(A,B):return PQ(ZS(A,B))
def ZJ(A,a,b):return lambda x:A(a(x),b(x))
def ZZ(A,n):
	if n==1:return A
	return PE(A,ZZ(A,n-1))
def PU(A,B):return lambda x:A(x)==B
def ZP(A,B):return PK(PM(B,A))
def PM(A,B):return type(B)(B for B in B if B!=A)
def PK(A):return next(iter(A))
def PP(A,B):return type(A)(A for A in A if B(A))
def PY(a,b):return a or b
def Z(a,b):return type(a)(A for A in a if A not in b)
def P(a,b):return a&b
def PX(a,b):return type(a)((*a,*b))
def p(I):O=False;I=tuple(map(tuple,I));Q=PS(I);R=H(I,O,O,True);T=PJ(I,0);B=PK(R);U=K(B);C=PZ(B,I);V=ZZ(ZU,2);Y=V(C);a=X(Y);b=PR(a,(2,2));D=ZE(C,0,b);A=S(D);c=PM(0,Q);d=ZP(c,A);e=PJ(D,A);E=PR(e,U);F=PJ(I,A);f=M(F);g=G(F);h=PU(PK,f);i=PU(PK,g);j=ZJ(PY,h,i);J=PP(E,j);k=Z(E,J);l=PV(W,J);m=PV(L,k);N=PX(l,m);n=P(T,N);o=ZE(I,d,N);p=ZE(o,A,n);return[*map(list,p)]
def W(A):return max(A for(A,B)in U(A))
def M(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def V(A):return min(A for(A,B)in U(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def ZS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A):return tuple(map(max,zip(*U(A))))
def PH(A):return PM(A),PR(A)
def ZX(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def ZE(A):return tuple(A[1:-1]for A in A[1:-1])
def PX(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PY(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(ZX(A,(B*C+C*E,0),(B,D))for C in range(n))
def PG(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(ZX(A,(0,B*C+C*E),(D,B))for C in range(n))
def PS(A,B):return ZX(B,Q(A),PH(A))
def ZJ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PZ(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Q(A)[1]+K(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PJ(A):
	if isinstance(A,tuple):return A[::-1]
	B=Q(A)[0]+K(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def H(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PP(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);S=Y if C else Z
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in S(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def E(A):
	if len(A)==0:return A
	return ZZ(A,(-V(A),-G(A)))
def ZZ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Q(A):return tuple(map(min,zip(*U(A))))
def PU(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def R(A):return PM(A)>PR(A)
def PR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-V(A)+1
def ZU(A,B):return type(B)(A(B)for B in B)
def PE(A,B):return lambda x:A(B(x))
def PL(A,a,b):return a if A else b
def ZL(A):return max(enumerate(A))[1]
def ZP(A):return next(iter(A))
def PQ(j):return 0,j
def PV(i):return i,0
def J(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PW(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def PK(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def p(I):I=tuple(map(tuple,I));L=PP(I,True,False,True);M=PX(I,5,0);N=P(L,2);O=ZP(N);A=R(O);S=PL(A,PG,PY);T=PL(A,PZ,PJ);B=PU(I,2);U=PS(B,I);V=ZE(U);W=T(V);X=S(W,2);Y=PE(E,H);C=ZU(Y,X);D=ZL(C);Z=ZP(C);a=Q(B);F=J(a);b=ZZ(D,F);c=ZZ(Z,F);d=PL(A,PR,PM);e=PL(A,PQ,PV);G=d(D);f=PW(G);K=PE(e,J);g=K(G);h=PK(g);i=K(f);j=ZZ(b,h);k=ZZ(c,i);l=ZJ(M,j);m=ZJ(l,k);return[*map(list,m)]
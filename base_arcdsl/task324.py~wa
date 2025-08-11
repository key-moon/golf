def PL(A,B):return type(B)(B for B in B if B!=A)
def PV(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def W(A):return max(A for(A,B)in E(A))
def M(A):return max(A for(B,A)in E(A))
def PQ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in E(A))
def V(A):return min(A for(A,B)in E(A))
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-V(A)+1
def H(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PK(A,B):return H(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PX(A):return V(A)+PU(A)//2,Q(A)+PY(A)//2
def ZZ(A,B,C):
	H,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(F,G)in E(C):
		if 0<=F<H and 0<=G<I:D[F][G]=B
	return tuple(tuple(A)for A in D)
def K(A,B):D,F=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in E(A)if 0<=A<D and 0<=C<F)
def PM(A):return next(iter(A))[0]
def R(A,B,C,D):
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
def Y(A):return S(A)|J(A)
def PP(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def U(A,n):return frozenset(A for A in A if len(A)==n)
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PE(A,B):return PV(PH(A,B))
def PH(A,B):return type(B)(A(B)for B in B)
def ZP(A,a,b):return lambda x:A(a(x),b(x))
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PZ(A,B):return lambda x:A(B(x))
def PJ(A,a,b):return a if A else b
def PG(A,B):return PW(PL(B,A))
def ZS(A):return max(enumerate(A))[1]
def PW(A):return next(iter(A))
def Z(a,b):return type(a)(A for A in a if A not in b)
def P(a,b):return a&b
def PS(a,b):return type(a)((*a,*b))
def G(a,b):return a==b
def p(I):N=False;I=tuple(map(tuple,I));C=R(I,True,N,N);A=U(C,1);O=PH(PM,A);Q=Z(C,A);D=PH(PM,Q);E=PW(D);S=ZS(D);T=PP(I,E);V=PP(I,S);W=PR(PK,(1,1));X=PR(PK,(-1,-1));a=PR(PK,(1,-1));b=PR(PK,(-1,1));c=ZP(PS,W,X);d=ZP(PS,a,b);e=ZP(PS,c,d);f=PZ(e,PX);F=PE(f,A);g=P(T,F);h=P(V,F);H=PW(A);B=PM(H);i=PX(H);j=Y(i);k=K(j,I);l=L(k);J=PG(O,B);M=G(l,E);m=PJ(M,B,J);n=PJ(M,J,B);o=ZZ(I,m,g);p=ZZ(o,n,h);return[*map(list,p)]
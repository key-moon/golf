def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def ZU(A,B,C):
	H,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(F,G)in E(C):
		if 0<=F<H and 0<=G<I:D[F][G]=B
	return tuple(tuple(A)for A in D)
def Y(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def K(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in E(a)for(C,D)in E(b))
def R(A):return max(A for(A,B)in E(A))
def G(A):return max(A for(B,A)in E(A))
def PR(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def H(A):return min(A for(B,A)in E(A))
def Q(A):return min(A for(A,B)in E(A))
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return G(A)-H(A)+1
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return R(A)-Q(A)+1
def PL(A):return Q(A)+PE(A)//2,H(A)+PY(A)//2
def PP(a,b):return K(a,b)==1
def L(a,b):return len(set(A for(B,A)in E(a))&set(A for(B,A)in E(b)))>0
def M(A,B):
	H,I=PL(A);J,K=PL(B);C,D=0,0
	if L(A,B):C=1 if H<J else-1
	else:D=1 if I<K else-1
	E,F=C,D;G=0
	while not PP(A,B)and G<42:G+=1;E+=C;F+=D;A=PK(A,(C,D))
	return E-C,F-D
def PQ(A,B):return ZU(A,Y(A),E(B))
def ZP(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PM(A):return next(iter(A))[0]
def PS(A,B,C,D):
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
def PK(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def U(A,n):return frozenset(A for A in A if len(A)==n)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PX(A,B):return PV(ZS(A,B))
def ZS(A,B):return type(B)(A(B)for B in B)
def ZJ(A,a,b):return lambda x:A(a(x),b(x))
def PH(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def ZZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PW(h,g,f):return lambda x:h(g(f(x)))
def PU(A,B):return lambda x:A(B(x))
def PG(A):return next(iter(A))
def PJ(A,B):return type(A)(A for A in A if B(A))
def PV(A):return type(A)(B for A in A for B in A)
def Z(a,b):return type(a)(A for A in a if A not in b)
def W(A,B):return A in B
def PZ(x):return x
def p(I):I=tuple(map(tuple,I));B=PS(I,True,False,True);A=U(B,1);C=Z(B,A);D=ZS(PM,C);E=ZZ(W,D);F=PU(E,PM);G=PJ(A,F);H=PH(P,C);J=PW(PG,H,PM);K=ZJ(M,PZ,J);L=ZJ(PK,PZ,K);N=PV(A);O=PX(L,G);Q=PQ(I,N);R=ZP(Q,O);return[*map(list,R)]
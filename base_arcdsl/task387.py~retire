def PM(A):return next(iter(A))
def PH(A,B):return type(B)(A(B)for B in B)
def PL(A):return type(A)(B for A in A for B in A)
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def M(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def G(A):return tuple(map(max,zip(*J(A))))
def W(A):return tuple(map(min,zip(*J(A))))
def ZJ(A):
	if len(A)==0:return A
	F,H=W(A);I,J=G(A);B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def PU(A):F,G=L(A)-1,Q(A)-1;H,I=M(A)+1,Y(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def PK(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def ZZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PY(A):return next(iter(A))[0]
def PS(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def V(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def H(A,B,C,D):
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
def R(A,B):return frozenset((A,B)for B in J(B))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PE(A,B):return PL(PH(A,B))
def ZP(A,a,b):return lambda x:A(a(x),b(x))
def PG(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PV(h,g,f):return lambda x:h(g(f(x)))
def PZ(A,B):return lambda x:A(B(x))
def PQ(A,B):return PM(PX(B,A))
def PX(A,B):return type(B)(B for B in B if B!=A)
def PP(A,B):return type(A)(A for A in A if B(A))
def K(A):return frozenset({A})
def PJ(A,B):return min(A,key=B)
def P(a,b):return type(a)(A for A in a if A not in b)
def ZS(n):return n%2==0
def p(I):I=tuple(map(tuple,I));B=H(I,True,False,True);C=PS(I);D=PX(0,C);E=PG(PQ,D);F=PZ(E,PY);G=ZP(R,F,PU);L=PE(G,B);A=PE(J,B);M=ZJ(A);N=P(M,A);O=PG(PJ,A);Q=PR(PZ,K);S=PG(PR,V);T=PV(Q,S,K);U=PV(K,O,T);W=ZP(V,K,U);X=PZ(ZS,W);Y=PP(N,X);Z=PK(I,L);a=ZZ(Z,5,Y);return[*map(list,a)]
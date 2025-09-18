def H(A,B):return type(A)(A for A in A if B(A))
def PQ(A):return type(A)(B for A in A for B in A)
def PH(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PX(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-Y(A)+1
def ZE(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def Q(A):return tuple(map(min,zip(*U(A))))
def PK(A):return PM(A),PW(A)
def M(A):return max(A for(B,A)in U(A))
def G(A):return min(A for(B,A)in U(A))
def W(A):return max(A for(A,B)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def PV(A):F,H=Y(A)-1,G(A)-1;I,J=W(A)+1,M(A)+1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def PS(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PZ(A,B):return ZE(B,Q(A),PK(A))
def ZJ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PG(A):return next(iter(A))[0]
def V(A,B):return Y(A)==0 or G(A)==0 or W(A)==len(B)-1 or M(A)==len(B[0])-1
def PR(A):return PW(A)==len(A)and PM(A)==1
def ZP(A):return PM(A)==len(A)and PW(A)==1
def Z(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PX(A)-{X(A)})
def R(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=L if C else S
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in U(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def K(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def ZZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PE(A,B):return lambda x:A(B(x))
def PL(A,a,b):return a if A else b
def PJ(A,B):return next(A for A in A if B(A))
def PU(A,B):return PQ(H(A,B))
def PY(A,B):return max(A,key=B)
def ZS(A):return len(A)
def PP(a,b):return a>b
def ZU(b):return not b
def p(I):G=False;I=tuple(map(tuple,I));H=R(I,True,G,G);J=P(H,0);L=ZZ(V,I);M=PE(ZU,L);N=PJ(J,M);O=PV(N);A=PZ(O,I);Q=Z(A);B=PY(Q,ZS);S=PG(B);C=U(B);D=K(PS,C,C);E=PU(D,ZP);F=PU(D,PR);T=ZS(E);W=ZS(F);X=PP(T,W);Y=PL(X,E,F);a=ZJ(A,S,Y);return[*map(list,a)]
def PM(A):return type(A)(B for A in A for B in A)
def PQ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def G(A):return max(A for(A,B)in U(A))
def V(A):return min(A for(A,B)in U(A))
def W(A):return max(A for(B,A)in U(A))
def K(A):return min(A for(B,A)in U(A))
def PV(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-V(A)+1
def PX(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PG(A,B):return PS(A,(A[0]+42*B[0],A[1]+42*B[1]))
def M(A):return frozenset((B,A[1])for B in range(30))
def PS(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def Q(A,B,C):
	G,H=len(A),len(A[0]);I=L(A);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def ZP(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A):return len(PX(A))
def PK(A):return PL(A)==len(A)and PV(A)==1
def PP(A,B,C,D):
	M=L(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=Y if C else S
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
def PW(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def R(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*U(A)))))
def PJ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def H(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PY(A,B):return PM(PH(A,B))
def PH(A,B):return type(B)(A(B)for B in B)
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PU(A,B):return lambda x:A(x)==B
def PE(A,B):return PM(PZ(A,B))
def PZ(A,B):return type(A)(A for A in A if B(A))
def Z(a,b):return type(a)(A for A in a if A not in b)
def p(I):D=False;I=tuple(map(tuple,I));E=PJ(I,2);F=PJ(I,5);G=H(PS,E,F);J=PE(G,PK);A=Q(I,2,J);K=PU(X,2);B=PP(A,D,D,True);C=PZ(B,K);L=Z(B,C);N=P(L,2);O=PY(U,N);S=PH(R,C);T=PW(S,(1,1));V=PR(PG,(-1,0));W=PY(V,T);Y=ZP(A,2,W);a=PY(M,O);b=ZP(Y,2,a);return[*map(list,b)]
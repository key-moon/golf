def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def V(A):return max(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def M(A):return min(A for(B,A)in J(A))
def L(A):return min(A for(A,B)in J(A))
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-M(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def R(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PM(A,B):return R(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PU(A):return L(A)+PP(A)//2,M(A)+PE(A)//2
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PR(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PL(A):return next(iter(A))[0]
def K(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();Q,R=len(A),len(A[0]);S=U(A);T=X if C else P
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def PY(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(A,B):return frozenset((A,B)for B in J(B))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PS(A,B):return PX(PG(A,B))
def PG(A,B):return type(B)(A(B)for B in B)
def PK(A,a,b):return lambda x:A(a(x),b(x))
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def H(A,B):return lambda x:A(B(x))
def W(A,B,C):return tuple(range(A,B,C))
def PJ(j):return 0,j
def S(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PX(A):return type(A)(B for A in A for B in A)
def PZ(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def p(I):I=tuple(map(tuple,I));A=K(I,True,False,True);B=PG(J,A);C=PQ(PM,(0,1));D=H(C,PU);E=PK(G,PL,D);F=PS(E,A);L=PW(I,F);M=W(0,5,1);N=PG(PZ,M);O=PG(S,N);P=PG(PJ,O);R=Q(PY,B,P);T=PX(R);U=PR(L,5,T);return[*map(list,U)]
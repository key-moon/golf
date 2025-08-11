def PY(A,B):return type(B)(A(B)for B in B)
def PJ(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return max(A for(A,B)in J(A))
def V(A):return max(A for(B,A)in J(A))
def PX(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A):return min(A for(B,A)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-W(A)+1
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-Y(A)+1
def PZ(A):return Y(A)+H(A)//2,W(A)+PS(A)//2
def PM(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def G(A,B,C,D):
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
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PP(A,B):return PJ(PY(A,B))
def PL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def R(A,B):return lambda x:A(B(x))
def PW(a,b):return tuple(zip(a,b))
def Q(A,B,C):return tuple(range(A,B,C))
def PQ(A):return max(enumerate(A))[1]
def PU(A):return next(iter(A))
def K(A,B):return type(A)(A for A in A if B(A))
def PV(A):return len(A)
def PE(A,B):return tuple(sorted(A,key=B))
def L(A,B):return A in B
def p(I):C=False;I=tuple(map(tuple,I));D=G(I,True,C,C);E=P(D,0);F=R(PQ,PZ);A=PE(E,F);B=PV(A);H=Q(0,B,3);J=PL(L,H);M=R(J,PQ);N=Q(0,B,1);O=PW(A,N);S=K(O,M);T=PP(PU,S);U=PM(I,4,T);return[*map(list,U)]
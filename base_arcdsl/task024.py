def PV(A,B):return type(B)(A(B)for B in B)
def PE(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Q(A):return max(A for(A,B)in U(A))
def W(A):return max(A for(B,A)in U(A))
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A):return min(A for(B,A)in U(A))
def V(A):return min(A for(A,B)in U(A))
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-G(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def X(A):return frozenset((A[0],B)for B in range(30))
def M(A):return frozenset((B,A[1])for B in range(30))
def PJ(A):return V(A)+PZ(A)//2,G(A)+PU(A)//2
def PY(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PW(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PX(A):return next(iter(A))[0]
def R(A,B,C,D):
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
def K(A,B):return frozenset((A,B)for B in U(B))
def H(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PS(A,B):return PE(PV(A,B))
def PM(A,a,b):return lambda x:A(a(x),b(x))
def PP(A,B):return lambda x:A(B(x))
def Z(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));A=R(I,True,False,True);B=H(I,2);C=PS(M,B);D=PW(I,2,C);E=P(A,2);F=Z(A,E);G=PP(X,PJ);J=PM(K,PX,G);L=PS(J,F);N=PY(D,L);return[*map(list,N)]
def R(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def PE(A):return type(A)(B for A in A for B in A)
def V(A):return max(A for(A,B)in S(A))
def Y(A):return max(A for(B,A)in S(A))
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-M(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return min(A for(B,A)in S(A))
def L(A):return min(A for(A,B)in S(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PZ(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PM(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PS(A):return tuple(tuple(A[::-1])for A in A[::-1])
def Q(A,B,C,D):
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
def J(A):
	if len(A)==0:return A
	return PL(A,(-L(A),-M(A)))
def PL(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PX(A):return PP(A),PU(A)
def G(A,a,b):return PE(R(A,a,b))
def PW(A,B):return type(B)(A(B)for B in B)
def K(A,B):return lambda x:A(B(x))
def W(A,B,C):return tuple(range(A,B,C))
def H(i):return i,0
def PQ(A):return len(A)
def PY(A,B):return tuple(sorted(A,key=B))
def PJ(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def p(I):I=tuple(map(tuple,I));B=PX(I);C=Q(I,True,False,True);D=K(PJ,PQ);E=PY(C,D);A=PW(J,E);F=PQ(A);L=W(0,F,1);M=PW(H,L);N=G(PL,A,M);O=PZ(0,B);P=PM(O,N);R=PS(P);return[*map(list,R)]
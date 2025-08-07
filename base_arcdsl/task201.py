def PR(A):return next(iter(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A):return tuple(map(max,zip(*J(A))))
def M(A):return max(A for(A,B)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def V(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-Q(A)+1
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-Y(A)+1
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def ZU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def W(A):return tuple(map(min,zip(*J(A))))
def PG(A):return PY(A),PW(A)
def PS(A):return A[:len(A)//2]
def PV(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PK(A):return tuple(A for A in zip(*A[::-1]))
def R(A):return PV(PS(PK(A)))
def ZP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def PJ(A,B):return ZU(B,W(A),PG(A))
def ZS(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PZ(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=W(A)[1]+G(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PX(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PP(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=L if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def U(A):
	if len(A)==0:return A
	return PH(A,(-Y(A),-Q(A)))
def PH(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def ZJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PE(A,B):return lambda x:A(x)==B
def PL(A,a,b):return a if A else b
def ZZ(A,B):return PR(PM(B,A))
def PM(A,B):return type(B)(B for B in B if B!=A)
def PU(A,B):return next(A for A in A if B(A))
def PQ(A):return type(A)(B for A in A for B in A)
def H(a,b):return a==b
def K(x):return x
def p(I):D=False;I=tuple(map(tuple,I));B=PP(I,D,D,True);E=ZJ(P,4);F=PE(E,0);A=PU(B,F);G=PM(A,B);J=PQ(G);C=PJ(J,I);L=ZP(C,(1,0));M=PJ(A,I);N=R(M);O=PX(N);Q=ZZ(O,0);S=H(L,Q);T=PL(S,K,PZ);V=T(A);W=U(V);X=PH(W,(1,1));Y=ZS(C,X);return[*map(list,Y)]
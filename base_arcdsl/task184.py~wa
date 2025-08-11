def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return max(A for(A,B)in S(A))
def L(A):return max(A for(B,A)in S(A))
def PX(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return min(A for(B,A)in S(A))
def X(A):return min(A for(A,B)in S(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-V(A)+1
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def PZ(A):return X(A)+H(A)//2,V(A)+PS(A)//2
def PL(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PW(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PP(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PE(A):return tuple(A for A in zip(*A[::-1]))
def PJ(A):return next(iter(A))[0]
def M(A,B,C,D):
	M=U(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);V=E if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in V(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PV(A,B):return type(B)(A(B)for B in B)
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PU(h,g,f):return lambda x:h(g(f(x)))
def G(A,B):return lambda x:A(B(x))
def PQ(a,b):return tuple(zip(a,b))
def K(A):return tuple(A)
def W(A,B):return type(A)(A for A in A if B(A))
def PM(A):return len(A)
def Q(a,b):return a>b
def R(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def p(I):A=True;I=tuple(map(tuple,I));D=J(I);E=M(I,A,A,A);F=PY(Q,2);H=G(F,PM);L=W(E,H);B=K(L);N=PV(PJ,B);O=PV(PZ,B);P=PQ(N,O);S=PW(I,0,D);T=PL(S,P);U=PY(Q,1);V=G(R,K);C=PU(U,PM,V);X=W(T,C);Y=PE(X);Z=W(Y,C);a=PP(Z);return[*map(list,a)]
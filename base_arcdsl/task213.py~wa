def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return max(A for(A,B)in S(A))
def L(A):return max(A for(B,A)in S(A))
def M(A):return min(A for(B,A)in S(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-M(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def PX(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return tuple(map(min,zip(*S(A))))
def G(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def K(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=V(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def PJ(A):return next(iter(A))[0]
def PL(A):return PP(A)==len(A)and PS(A)==1
def X(A):return min(A for(A,B)in S(A))
def Q(A,B,C,D):
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
def PV(A,B):return type(B)(A(B)for B in B)
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def H(A,a,b):return a if A else b
def PU(A):return next(iter(A))
def PM(A):return len(A)
def PZ(A,B):return tuple(A for B in range(B))
def PE(A,B):return tuple(sorted(A,key=B))
def R(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def W(x):return x
def p(I):A=True;I=tuple(map(tuple,I));B=G(I,5,0);E=Q(B,A,A,A);F=PU(E);J=PL(F);C=H(J,K,W);L=C(B);M=Q(L,A,A,A);N=PE(M,X);O=PV(PJ,N);D=R(O);P=PM(D);S=PY(PZ,P);T=PV(S,D);U=C(T);return[*map(list,U)]
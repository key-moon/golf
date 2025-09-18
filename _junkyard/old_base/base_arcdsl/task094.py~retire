def PE(A,B):return type(B)(A(B)for B in B)
def PJ(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(A,B)in S(A))
def V(A):return max(A for(B,A)in S(A))
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in S(A))
def L(A):return min(A for(A,B)in S(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-Q(A)+1
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-L(A)+1
def U(A):return frozenset((A[0],B)for B in range(30))
def Y(A):return frozenset((B,A[1])for B in range(30))
def PZ(A):return L(A)+H(A)//2,Q(A)+PS(A)//2
def M(A,B,C):
	H,I=len(A),len(A[0]);J=E(A);D=list(list(A)for A in A)
	for(F,G)in S(C):
		if 0<=F<H and 0<=G<I:
			if D[F][G]==J:D[F][G]=B
	return tuple(tuple(A)for A in D)
def G(A,B,C,D):
	M=E(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);U=X if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in U(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def PP(A,B):return PJ(PE(A,B))
def PX(A,a,b):return lambda x:A(a(x),b(x))
def K(A,B):return lambda x:A(B(x))
def R(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=G(I,True,False,True);B=PX(R,Y,U);C=K(B,PZ);D=PP(C,A);E=M(I,6,D);return[*map(list,E)]
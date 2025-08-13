def S(A,B):return type(A)(A for A in A if B(A))
def GH(A):return type(A)(B for A in A for B in A)
def H(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def V(A):return G(A)|H(A)
def G(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def R(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def X(A):return max(A for(A,B)in Y(A))
def M(A):return min(A for(A,B)in Y(A))
def J(A):return max(A for(B,A)in Y(A))
def Q(A):return min(A for(B,A)in Y(A))
def GY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-Q(A)+1
def GG(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-M(A)+1
def GV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):return tuple(map(max,zip(*Y(A))))
def K(A):return tuple(map(min,zip(*Y(A))))
def U(A):
	if len(A)==0:return frozenset({})
	B=Y(A);C,D=K(B);E,F=P(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def Y(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def GM(B):
	if len(B)==0:return frozenset({})
	return U(B)-Y(B)
def GE(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Y(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Z(A):return len(A)==len(A[0])if isinstance(A,tuple)else GG(A)*GY(A)==len(A)and GG(A)==GY(A)
def W(A,B,C,D):
	M=E(A)if D else None;N=set();I=set();Q,S=len(A),len(A[0]);T=R(A);U=V if C else G
	for F in T:
		if F in I:continue
		J=A[F[0]][F[1]]
		if J==M:continue
		O={(J,F)};K={F}
		while len(K)>0:
			P=set()
			for H in K:
				L=A[H[0]][H[1]]
				if J==L if B else L!=M:O.add((L,H));I.add(H);P|={(A,B)for(A,B)in U(H)if 0<=A<Q and 0<=B<S}
			K=P-I
		N.add(frozenset(O))
	return frozenset(N)
def GJ(A,B):return type(B)(A(B)for B in B)
def L(A,B):return GH(S(A,B))
def p(I):I=tuple(map(tuple,I));A=W(I,True,False,True);B=GJ(GM,A);C=L(B,Z);D=GE(I,2,C);return[*map(list,D)]
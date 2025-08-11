def H(A):return type(A)(B for A in A for B in A)
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return min(A for(B,A)in S(A))
def Y(A):return min(A for(A,B)in S(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Q(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PJ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def E(A):return len(Q(A))
def W(A,B,C,D):
	K=X(A)if D else None;M=set();G=set();Q,R=len(A),len(A[0]);S=U(A);T=L if C else P
	for E in S:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in T(F)if 0<=A<Q and 0<=B<R}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def J(A):
	if len(A)==0:return A
	return PP(A,(-Y(A),-M(A)))
def PP(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def V(A):return tuple(map(min,zip(*S(A))))
def K(A,B):return H(PU(A,B))
def PU(A,B):return type(B)(A(B)for B in B)
def PS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def R(A,B):return type(B)(B for B in B if B!=A)
def G(A,B):return max(A,key=B)
def p(I):C=False;I=tuple(map(tuple,I));A=W(I,C,C,True);B=G(A,E);D=J(B);F=R(B,A);H=PU(V,F);L=PS(PP,D);M=K(L,H);N=PJ(I,M);return[*map(list,N)]
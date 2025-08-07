def Q(A):return next(iter(A))
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def U(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def L(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def W(A):return next(iter(A))[0]
def X(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def E(A,B,C,D):
	L=S(A)if D else None;M=set();G=set();Q,R=len(A),len(A[0]);T=J(A);V=U if C else P
	for E in T:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==L:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=L:N.add((K,F));G.add(F);O|={(A,B)for(A,B)in V(F)if 0<=A<Q and 0<=B<R}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def M(A,B):return Q(Y(B,A))
def Y(A,B):return type(B)(B for B in B if B!=A)
def V(A,B):return max(A,key=B)
def G(A):return len(A)
def p(I):I=tuple(map(tuple,I));A=X(I);B=E(I,True,False,True);C=V(B,G);D=W(C);F=Y(0,A);H=M(F,D);J=L(H,(1,1));return[*map(list,J)]
def PJ(A,B):return type(B)(A(B)for B in B)
def PP(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A):return tuple(map(max,zip(*J(A))))
def M(A):return tuple(map(min,zip(*J(A))))
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return max(A for(B,A)in J(A))
def W(A):return min(A for(B,A)in J(A))
def V(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def PS(A):F,G=L(A)+1,W(A)+1;H,I=V(A)-1,Y(A)-1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def Q(A):
	if len(A)==0:return frozenset({})
	B=J(A);C,D=M(B);E,F=G(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def PU(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def K(A,B,C,D):
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
def H(A,B):return PP(PJ(A,B))
def R(A,B):return lambda x:A(B(x))
def p(I):A=False;I=tuple(map(tuple,I));B=K(I,True,A,A);C=P(B,5);D=R(Q,PS);E=H(D,C);F=PU(I,2,E);return[*map(list,F)]
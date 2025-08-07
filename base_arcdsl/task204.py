def V(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return max(A for(B,A)in J(A))
def M(A):return min(A for(B,A)in J(A))
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-M(A)+1
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PS(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def K(A):return len(A)==len(A[0])if isinstance(A,tuple)else R(A)*H(A)==len(A)and R(A)==H(A)
def W(A,B,C,D):
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
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return V(A)-L(A)+1
def G(A,B):return lambda x:A(B(x))
def Q(A,B):return type(A)(A for A in A if B(A))
def PP(A):return type(A)(B for A in A for B in A)
def P(a,b):return type(a)(A for A in a if A not in b)
def PJ(n):return n%2==0
def p(I):C=False;I=tuple(map(tuple,I));D=W(I,True,C,C);A=Q(D,K);E=G(PJ,R);B=Q(A,E);F=P(A,B);H=PP(B);J=PP(F);L=PS(I,2,H);M=PS(L,7,J);return[*map(list,M)]
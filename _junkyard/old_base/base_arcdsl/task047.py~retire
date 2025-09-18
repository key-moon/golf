def PU(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-Y(A)+1
def E(A):return frozenset((A[0],B)for B in range(30))
def V(A):return frozenset((B,A[1])for B in range(30))
def PS(A):return Y(A)+PP(A)//2,Q(A)+PJ(A)//2
def PY(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PW(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PE(A):return next(iter(A))[0]
def K(A,B,C,D):
	K=X(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=U(A);S=L if C else Z
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in S(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def G(A,B):return frozenset((A,B)for B in J(B))
def PZ(A,B):return PU(PV(A,B))
def PV(A,B):return type(B)(A(B)for B in B)
def PM(A,a,b):return lambda x:A(a(x),b(x))
def R(A,B):return lambda x:A(B(x))
def PQ(A):return max(enumerate(A))[1]
def PX(A):return next(iter(A))
def P(a,b):return a&b
def H(a,b):return type(a)((*a,*b))
def p(I):A=True;I=tuple(map(tuple,I));B=K(I,A,A,A);D=PM(H,V,E);C=R(D,PS);F=PM(G,PE,C);J=PZ(F,B);L=PY(I,J);M=PM(P,PX,PQ);N=PV(C,B);O=M(N);Q=PW(L,2,O);return[*map(list,Q)]
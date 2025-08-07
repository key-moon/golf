def K(A,B):return type(A)(A for A in A if B(A))
def PE(A):return type(A)(B for A in A for B in A)
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def M(A):return max(A for(A,B)in J(A))
def L(A):return min(A for(A,B)in J(A))
def Y(A):return max(A for(B,A)in J(A))
def W(A):return min(A for(B,A)in J(A))
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-W(A)+1
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-L(A)+1
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def R(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def V(A,B,C):
	H,I=len(A),len(A[0]);K=E(A);D=list(list(A)for A in A)
	for(F,G)in J(C):
		if 0<=F<H and 0<=G<I:
			if D[F][G]==K:D[F][G]=B
	return tuple(tuple(A)for A in D)
def PX(A):return PU(A)==len(A)and PS(A)==1
def PY(A):return PS(A)==len(A)and PU(A)==1
def G(A,B,C,D):
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
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def H(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def Q(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PM(A,a,b):return lambda x:A(a(x),b(x))
def PP(A,B):return PE(K(A,B))
def PJ(a,b):return a or b
def PZ(A,B):return max(A,key=B)
def PV(A):return len(A)
def p(I):I=tuple(map(tuple,I));A=P(I);B=G(I,True,False,True);C=PZ(B,PV);D=J(C);E=H(I,A);F=Q(R,D,E);K=PM(PJ,PY,PX);L=PP(F,K);M=V(I,A,L);return[*map(list,M)]
def PX(A,B):return type(B)(A(B)for B in B)
def PP(A):return type(A)(B for A in A for B in A)
def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|U(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return tuple(map(max,zip(*E(A))))
def V(A):return tuple(map(min,zip(*E(A))))
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PU(B):
	if len(B)==0:return frozenset({})
	return M(B)-E(B)
def M(A):
	if len(A)==0:return frozenset({})
	B=E(A);C,D=V(B);F,G=W(A);return frozenset((A,B)for A in range(C,F+1)for B in range(D,G+1))
def Z(A,B):
	F,G=len(A),len(A[0]);H=L(A);C=list(list(A)for A in A)
	for(I,(D,E))in B:
		if 0<=D<F and 0<=E<G:
			if C[D][E]==H:C[D][E]=I
	return tuple(tuple(A)for A in C)
def Q(A,B):D,F=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in E(A)if 0<=A<D and 0<=C<F)
def K(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);T=Y if C else S
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in T(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def G(A,B):return frozenset((A,B)for B in E(B))
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def H(A,B):return PP(PX(A,B))
def PL(A,a,b):return lambda x:A(a(x),b(x))
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PZ(h,g,f):return lambda x:h(g(f(x)))
def R(A,B):return lambda x:A(B(x))
def p(I):I=tuple(map(tuple,I));A=K(I,True,False,True);B=P(A,1);C=PE(Q,I);D=PZ(J,C,PU);E=PE(PS,(-1,0));F=R(E,M);L=PL(G,D,F);N=H(L,B);O=Z(I,N);return[*map(list,O)]
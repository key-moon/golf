def PV(A,B):return type(B)(A(B)for B in B)
def PS(A):return type(A)(B for A in A for B in A)
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|J(A)
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return tuple(map(max,zip(*U(A))))
def Y(A):return tuple(map(min,zip(*U(A))))
def V(A):
	if len(A)==0:return frozenset({})
	B=U(A);C,D=Y(B);E,F=M(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def R(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PL(A,B):return R(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PX(B):
	if len(B)==0:return frozenset({})
	return V(B)-U(B)
def PW(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Q(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in U(A)if 0<=A<D and 0<=C<E)
def G(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=L if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PZ(A,B):return PS(PV(A,B))
def PM(A,a,b):return lambda x:A(a(x),b(x))
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def H(A,B):return lambda x:A(x)==B
def PJ(h,g,f):return lambda x:h(g(f(x)))
def PP(A,B):return lambda x:A(B(x))
def PU(A):return next(iter(A))
def K(A,B):return type(A)(A for A in A if B(A))
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));A=S(I);B=G(I,True,False,True);D=PY(Q,I);C=PP(PU,PX);E=PY(P,A);F=H(E,2);J=PJ(F,D,Z);L=PY(K,J);M=PJ(PU,L,U);N=PM(W,C,M);O=PM(PL,C,N);R=PZ(O,B);T=PW(I,A,R);V=PZ(PX,B);X=PW(T,0,V);return[*map(list,X)]
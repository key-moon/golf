def PS(A):return type(A)(B for A in A for B in A)
def W(A):return min(A for(B,A)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def V(A,B,C):
	G,H=len(A),len(A[0]);I=X(A);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A):return min(A for(A,B)in J(A))
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
def U(A):
	if len(A)==0:return A
	return PE(A,(-Y(A),-W(A)))
def PE(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A):return tuple(map(min,zip(*J(A))))
def H(A,B):return PS(PM(A,B))
def PM(A,B):return type(B)(A(B)for B in B)
def PQ(A,a,b):return lambda x:A(a(x),b(x))
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PJ(h,g,f):return lambda x:h(g(f(x)))
def K(A,B):return lambda x:A(B(x))
def Q(A,B,C):return tuple(range(A,B,C))
def PZ(A,B):return type(B)(B for B in B if B!=A)
def PU(A):return next(iter(A))
def PP(j):return 0,j
def R(A,B):return max(A,key=B)
def PW(A):return len(A)
def PX(A,B):return tuple(sorted(A,key=B))
def P(a,b):return a&b
def p(I):A=True;I=tuple(map(tuple,I));D=G(I,A,A,A);B=PX(D,Y);C=PU(B);E=PZ(C,B);F=U(C);J=PY(PE,F);L=K(J,M);N=Q(2,-1,-1);O=PM(PP,N);S=PV(PM,O);T=PY(K,PW);W=PY(PY,P);X=K(T,W);Z=PY(PY,PE);a=PJ(S,Z,L);b=PQ(R,a,X);c=H(b,E);d=V(I,1,c);return[*map(list,d)]
def PR(A,B):return type(B)(A(B)for B in B)
def PM(A):return type(A)(B for A in A for B in A)
def PQ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return J(A)|U(A)
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PP(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*E(A)))))
def H(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*E(A)))))
def R(A):return tuple(map(max,zip(*E(A))))
def Q(A):return tuple(map(min,zip(*E(A))))
def M(A):return max(A for(B,A)in E(A))
def G(A):return min(A for(B,A)in E(A))
def W(A):return max(A for(A,B)in E(A))
def V(A):return min(A for(A,B)in E(A))
def PY(A):F,H=V(A)-1,G(A)-1;I,J=W(A)+1,M(A)+1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def K(A):
	if len(A)==0:return frozenset({})
	B=E(A);C,D=Q(B);F,G=R(A);return frozenset((A,B)for A in range(C,F+1)for B in range(D,G+1))
def PS(A):return frozenset({Q(A),H(A),PP(A),R(A)})
def ZZ(A,B,C):
	H,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(F,G)in E(C):
		if 0<=F<H and 0<=G<I:D[F][G]=B
	return tuple(tuple(A)for A in D)
def PJ(A,B,C,D):
	M=L(A)if D else None;N=set();G=set();Q,R=len(A),len(A[0]);S=X(A);T=Y if C else J
	for E in S:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==M:continue
		O={(H,E)};I={E}
		while len(I)>0:
			P=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=M:O.add((K,F));G.add(F);P|={(A,B)for(A,B)in T(F)if 0<=A<Q and 0<=B<R}
			I=P-G
		N.add(frozenset(O))
	return frozenset(N)
def J(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PE(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Z(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PV(A,B):return PM(PR(A,B))
def ZP(A,a,b):return lambda x:A(a(x),b(x))
def PG(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PX(A,B):return lambda x:A(x)==B
def PW(h,g,f):return lambda x:h(g(f(x)))
def PL(A,B):return PM(PU(A,B))
def PU(A,B):return type(A)(A for A in A if B(A))
def PH(A):return len(A)
def S(a,b):return type(a)(A for A in a if A not in b)
def P(a,b):return a&b
def PZ(a,b):return a==b
def p(I):A=False;I=tuple(map(tuple,I));B=PJ(I,True,A,A);C=Z(B,0);D=ZP(PZ,E,K);F=PU(C,D);G=PG(PV,J);H=PW(G,PS,PY);L=ZP(S,H,PY);M=PE(I,5);N=PK(P,M);O=PX(PH,0);Q=PW(O,N,L);R=PL(F,Q);T=ZZ(I,4,R);return[*map(list,T)]
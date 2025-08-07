def ZP(A,B):return type(B)(A(B)for B in B)
def Q(A):return max(A for(A,B)in J(A))
def V(A):return min(A for(A,B)in J(A))
def W(A):return max(A for(B,A)in J(A))
def K(A):return min(A for(B,A)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return P(A)|S(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PE(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PR(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A):return tuple(map(min,zip(*J(A))))
def PG(A):return PY(A),PW(A)
def ZU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def X(A):return frozenset((A[0],B)for B in range(30))
def M(A):return frozenset((B,A[1])for B in range(30))
def PX(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(ZU(A,(B*C+C*E,0),(B,D))for C in range(n))
def PZ(A,B):return ZU(B,G(A),PG(A))
def ZJ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PV(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PK(A):return tuple(A for A in zip(*A[::-1]))
def E(A):return len(PE(A))
def R(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();Q,R=len(A),len(A[0]);S=U(A);T=Y if C else P
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
def PS(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PW(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PM(A,B):return PQ(ZP(A,B))
def ZS(A,a,b):return lambda x:A(a(x),b(x))
def PH(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PJ(A,B):return lambda x:A(B(x))
def H(A,B):return type(A)(A for A in A if B(A))
def PL(A,B):return max(A,key=B)
def PQ(A):return type(A)(B for A in A for B in A)
def ZZ(A):return len(A)
def PP(a,b):return a>b
def PU(a,b):return type(a)((*a,*b))
def p(I):F=False;I=tuple(map(tuple,I));G=R(I,True,F,F);J=PL(G,ZZ);A=PZ(J,I);K=PY(A);L=PW(A);N=PX(A,K);O=PH(PP,4);C=PJ(O,E);P=H(N,C);Q=PQ(P);S=PK(Q);T=PX(S,L);U=H(T,C);V=PQ(U);B=PV(V);D=Z(B);W=PS(B,D);Y=ZS(PU,M,X);a=PM(Y,W);b=ZJ(B,D,a);return[*map(list,b)]
def PG(A,B):return type(B)(A(B)for B in B)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Q(A):return max(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A):return min(A for(B,A)in J(A))
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-Y(A)+1
def V(A):return frozenset((B,A[1])for B in range(30))
def PU(A):return Y(A)+PS(A)//2,G(A)+PX(A)//2
def W(A,B,C):
	G,H=len(A),len(A[0]);I=X(A);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PY(A):return next(iter(A))[0]
def E(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def Y(A):return min(A for(A,B)in J(A))
def K(A,B,C,D):
	K=X(A)if D else None;M=set();G=set();Q,R=len(A),len(A[0]);S=U(A);T=L if C else P
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
def PJ(A,B):return PL(PG(A,B))
def PR(A,a,b):return lambda x:A(a(x),b(x))
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PV(h,g,f):return lambda x:h(g(f(x)))
def PP(A,B):return lambda x:A(B(x))
def PE(A,B):return type(B)(B for B in B if B!=A)
def PM(A):return next(iter(A))
def R(A,B):return type(A)(A for A in A if B(A))
def S(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PH(a,b):return a and b
def PZ(A,B):return max(A,key=B)
def PL(A):return type(A)(B for A in A for B in A)
def PK(A):return len(A)
def H(a,b):return a>b
def p(I):B=True;I=tuple(map(tuple,I));C=K(I,B,B,B);A=PZ(C,PK);D=PE(A,C);G=PL(D);J=PY(G);F=Y(A);L=PQ(H,F);M=PP(L,Y);N=PQ(E,A);O=PR(PH,N,M);P=R(D,O);Q=S(F);T=PQ(H,Q);U=PP(T,PM);X=PQ(R,U);Z=PV(X,V,PU);a=PJ(Z,P);b=W(I,J,a);return[*map(list,b)]
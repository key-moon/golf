def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in J(A))
def V(A):return min(A for(A,B)in J(A))
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-V(A)+1
def PP(A):return A[:len(A)//2]
def S(A):return A[len(A)//2+len(A)%2:]
def PJ(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PV(A):return tuple(A for A in zip(*A[::-1]))
def E(A):return frozenset((A[0],B)for B in range(30))
def Y(A):return PJ(S(PV(A)))
def K(A):return PJ(PP(PV(A)))
def PE(A):return V(A)+PS(A)//2,Q(A)+PX(A)//2
def PQ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PR(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PY(A):return next(iter(A))[0]
def H(A,B,C,D):
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
def PM(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def R(A,B):return frozenset((A,B)for B in J(B))
def G(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*J(A)))))
def PU(A,B):return PL(PG(A,B))
def PG(A,B):return type(B)(A(B)for B in B)
def PK(A,a,b):return lambda x:A(a(x),b(x))
def PZ(A,B):return lambda x:A(B(x))
def PL(A):return type(A)(B for A in A for B in A)
def p(I):B=False;A=True;I=tuple(map(tuple,I));C=K(I);J=Y(I);L=H(J,A,B,A);M=H(C,A,B,A);N=PZ(E,PE);D=PK(R,PY,N);O=PU(D,M);P=PQ(C,O);Q=PU(D,L);S=PQ(I,Q);F=H(P,A,B,A);T=PG(G,F);U=PM(T,(0,1));V=PL(F);W=PQ(S,V);X=PR(W,5,U);return[*map(list,X)]
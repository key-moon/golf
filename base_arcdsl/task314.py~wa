def PK(A,B):return type(B)(A(B)for B in B)
def PY(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def PQ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A):return min(A for(B,A)in J(A))
def V(A):return min(A for(A,B)in J(A))
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-V(A)+1
def PZ(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PX(A):return V(A)+PJ(A)//2,Q(A)+PL(A)//2
def PG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PV(A):return next(iter(A))[0]
def E(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def Y(a,b):return len(set(A for(A,B)in J(a))&set(A for(A,B)in J(b)))>0
def R(A,B,C,D):
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
def K(A,B):return frozenset((A,B)for B in J(B))
def S(A,n):return frozenset(A for A in A if len(A)==n)
def PE(A,B):return PY(PK(A,B))
def PR(A,a,b):return lambda x:A(a(x),b(x))
def PM(h,g,f):return lambda x:h(g(f(x)))
def PS(A,B):return lambda x:A(B(x))
def PP(a,b):return frozenset((B,A)for A in b for B in a)
def PH(A):return max(enumerate(A))[1]
def PW(A):return next(iter(A))
def H(A,B):return type(A)(A for A in A if B(A))
def PU(a,b):return a or b
def G(A):return frozenset({A})
def p(I):I=tuple(map(tuple,I));B=R(I,True,False,True);A=S(B,1);C=PP(A,A);D=PR(E,PW,PH);F=PR(Y,PW,PH);J=PR(PU,D,F);L=H(C,J);M=PS(PX,PW);N=PS(PX,PH);O=PR(PZ,M,N);P=PM(G,PX,O);Q=PS(PV,PW);T=PR(K,Q,P);U=PE(T,L);V=PG(I,U);return[*map(list,V)]
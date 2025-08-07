def PR(A,B):return type(B)(A(B)for B in B)
def PV(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A):return max(A for(A,B)in J(A))
def W(A):return max(A for(B,A)in J(A))
def K(A):return min(A for(B,A)in J(A))
def M(A):return min(A for(A,B)in J(A))
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-M(A)+1
def PQ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def R(a,b):return Q(a,b)==1
def PW(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Y(A,B):
	I,J=PL(A);K,L=PL(B);C,D=0,0
	if E(A,B):C=1 if I<K else-1
	else:D=1 if J<L else-1
	F,G=C,D;H=0
	while not R(A,B)and H<42:H+=1;F+=C;G+=D;A=PW(A,(C,D))
	return F-C,G-D
def PS(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PL(A):return M(A)+PU(A)//2,K(A)+PY(A)//2
def PG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PM(A):return next(iter(A))[0]
def E(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def V(a,b):return len(set(A for(A,B)in J(a))&set(A for(A,B)in J(b)))>0
def PP(A,B,C,D):
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
def H(A,B):return frozenset((A,B)for B in J(B))
def PJ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def S(A,n):return frozenset(A for A in A if len(A)==n)
def PX(A,B):return PV(PR(A,B))
def PH(A,a,b):return lambda x:A(a(x),b(x))
def PK(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PZ(A,B):return type(A)(A for A in A if B(A))
def PE(a,b):return a or b
def ZP(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));B=PP(I,True,False,True);A=PJ(I,3);C=S(B,1);D=PK(E,A);F=PK(V,A);G=PH(PE,D,F);J=PZ(C,G);K=PK(Y,A);L=PH(ZP,PL,K);M=PH(PS,PL,L);N=PH(H,PM,M);O=PX(N,J);P=PG(I,O);return[*map(list,P)]
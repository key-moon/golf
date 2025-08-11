def Q(A):return max(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PG(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PY(A,B):return PG(A,X(A),J(B))
def W(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def PW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A):return min(A for(B,A)in J(A))
def V(A):return min(A for(A,B)in J(A))
def PX(A):return V(A)+PE(A)//2,G(A)+PL(A)//2
def R(a,b):return W(a,b)==1
def E(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def Y(A,B):
	I,J=PX(A);K,L=PX(B);C,D=0,0
	if E(A,B):C=1 if I<K else-1
	else:D=1 if J<L else-1
	F,G=C,D;H=0
	while not R(A,B)and H<42:H+=1;F+=C;G+=D;A=PM(A,(C,D))
	return F-C,G-D
def PR(A,B,C):return PQ(PY(A,B),PM(B,C))
def PQ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PZ(A,B,C,D):
	K=X(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=U(A);S=L if C else Z
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in S(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def PM(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PP(A,B):return frozenset((A,B)for B in J(B))
def PS(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def PU(A,a,b):return a if A else b
def PV(A):return next(iter(A))
def PK(x):
	if isinstance(x,int):return 0 if x==0 else 1 if x>0 else-1
	return 0 if x[0]==0 else 1 if x[0]>0 else-1,0 if x[1]==0 else 1 if x[1]>0 else-1
def PJ(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def H(a,b):return a==b
def K(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));D=PZ(I,True,False,True);E=P(D,3);A=PV(E);B=PS(I,2);C=Y(A,B);F=PV(C);G=H(F,0);J=PU(G,PL,PE);L=J(A);M=Y(B,A);N=PK(M);O=K(N,L);Q=PJ(O);R=PP(8,B);S=PM(R,Q);T=PQ(I,S);U=PR(T,A,C);return[*map(list,U)]
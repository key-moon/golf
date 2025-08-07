def PP(A,B):return type(A)(A for A in A if B(A))
def PK(A,B):return type(B)(A(B)for B in B)
def PY(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PH(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PM(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return max(A for(B,A)in J(A))
def Q(A):return max(A for(A,B)in J(A))
def PZ(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PQ(A,B):return PZ(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PW(A):F,H=Y(A)+1,G(A)+1;I,J=Q(A)-1,M(A)-1;B,C=min(F,I),min(H,J);D,E=max(F,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};L={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(K|L)
def PV(A,B):return PH(A,X(A),J(B))
def W(A,B,C):
	G,H=len(A),len(A[0]);I=X(A);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def V(A,B):return Y(A)==0 or G(A)==0 or Q(A)==len(B)-1 or M(A)==len(B[0])-1
def E(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def G(A):return min(A for(B,A)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def H(A,B,C,D):
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
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PL(A,B):return PY(PK(A,B))
def PG(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PU(A,a,b):return a if A else b
def PS(A,B):return PY(PP(A,B))
def PE(A,B):return min(A,key=B)
def PX(A,B):return max(A,key=B)
def PJ(A,B):return B(max(A,key=B,default=0))
def PR(A):return len(A)
def R(a,b):return a==b
def K(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):L=False;A=True;I=tuple(map(tuple,I));B=H(I,A,L,A);C=PE(B,PR);M=PX(B,PR);D=E(C,M);N=PU(D,(1,0),(0,1));F=PU(D,Y,G);O=PJ(B,F);Q=F(C);S=R(O,Q);T=PU(S,-1,1);U=K(N,T);X=PW(C);Z=PG(PQ,U);a=PL(Z,X);J=W(I,8,a);b=H(J,A,L,A);c=P(b,8);d=PG(V,I);e=PS(c,d);f=PV(J,e);return[*map(list,f)]
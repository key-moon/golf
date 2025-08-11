def PX(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PY(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def K(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PV(A,B):return K(A,(A[0]+42*B[0],A[1]+42*B[1]))
def E(A):return frozenset((A[0],B)for B in range(30))
def H(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def V(A,B,C):
	G,H=len(A),len(A[0]);I=X(A);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A):return min(A for(B,A)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def G(A,B,C,D):
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
def PL(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def R(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PE(A,B):return PX(PW(A,B))
def PW(A,B):return type(B)(A(B)for B in B)
def PQ(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PS(A,a,b):return a if A else b
def PU(i):return i,0
def PJ(A,B):return min(A,key=B)
def PP(Aa):return min(Aa,default=0)
def PZ(A):return max(A,default=0)
def Q(a,b):return a==b
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));A=G(I,True,False,True);B=R(I,8);C=H(I,8,4);D=P(A,2);F=PJ(A,Y);J=PW(Y,D);K=PQ(W,PZ,PP);L=K(J);N=PU(L);O=M(F);S=Q(O,0);T=PS(S,(0,-1),(0,1));U=PM(PV,T);X=PE(U,B);Z=V(C,8,X);a=PL(B,N);b=PE(E,a);c=V(Z,8,b);return[*map(list,c)]
def GQ(A):return type(A)(B for A in A for B in A)
def HG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def GL(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Y(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def H(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def P(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):return max(A for(B,A)in M(A))
def Z(A):return min(A for(B,A)in M(A))
def S(A):return max(A for(A,B)in M(A))
def U(A):return min(A for(A,B)in M(A))
def HJ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in M(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def GP(A,B):return HJ(A,Q(A),M(B))
def GU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def W(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in M(A)if 0<=A<D and 0<=C<E)
def GK(A):return next(iter(A))[0]
def R(A,B):return U(A)==0 or Z(A)==0 or S(A)==len(B)-1 or E(A)==len(B[0])-1
def GV(A,B,C,D):
	L=Q(A)if D else None;M=set();G=set();R,S=len(A),len(A[0]);T=P(A);U=X if C else H
	for E in T:
		if E in G:continue
		I=A[E[0]][E[1]]
		if I==L:continue
		N={(I,E)};J={E}
		while len(J)>0:
			O=set()
			for F in J:
				K=A[F[0]][F[1]]
				if I==K if B else K!=L:N.add((K,F));G.add(F);O|={(A,B)for(A,B)in U(F)if 0<=A<R and 0<=B<S}
			J=O-G
		M.add(frozenset(N))
	return frozenset(M)
def X(A):return H(A)|Y(A)
def K(A):
	if len(A)==0:return A
	return GL(A,(-U(A),-Z(A)))
def GH(A,B):return frozenset((A,B)for B in M(B))
def M(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def Q(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def GE(A,B):return GQ(GZ(A,B))
def GZ(A,B):return type(B)(A(B)for B in B)
def HH(A,a,b):return lambda x:A(a(x),b(x))
def GX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def GS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def GY(A,B):return lambda x:A(x)==B
def GW(h,g,f):return lambda x:h(g(f(x)))
def GM(A,B):return lambda x:A(B(x))
def GJ(A):return tuple(A)
def GG(A,B):return type(A)(A for A in A if B(A))
def V(A):return max(set(A),key=A.count)
def GR(A,B):return max(A,key=B)
def J(a,b):return type(a)(A for A in a if A not in b)
def HY(b):return not b
def L(x):return x
def p(I):I=tuple(map(tuple,I));N=Q(I);A=GV(I,True,True,False);B=G(A,N);C=GM(K,M);O=J(A,B);P=GS(R,I);S=GM(HY,P);D=GG(B,S);T=GS(W,I);U=GX(GE,X);Y=GM(U,M);Z=HH(J,Y,L);E=GW(Q,T,Z);a=GJ(D);b=GZ(E,a);c=V(b);d=GY(E,c);F=GG(D,d);e=GX(GR,O);f=GX(GY,C);H=GW(e,f,C);g=GM(GK,H);h=HH(GH,g,L);i=GE(H,F);j=GP(I,i);k=GE(h,F);l=GU(j,k);return[*map(list,l)]
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def W(A):return max(A for(B,A)in U(A))
def K(A):return min(A for(B,A)in U(A))
def Q(A):return max(A for(A,B)in U(A))
def V(A):return min(A for(A,B)in U(A))
def PM(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PU(A,B):return PM(A,L(A),U(B))
def PY(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def PX(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def PQ(A,B,C):return PY(PU(A,B),PX(B,C))
def M(A,B):return V(A)==0 or K(A)==0 or Q(A)==len(B)-1 or W(A)==len(B[0])-1
def H(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);T=Y if C else S
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in T(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def E(A):
	if len(A)==0:return A
	return PX(A,(-V(A),-K(A)))
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A):return tuple(map(min,zip(*U(A))))
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PS(A,B):return lambda x:A(x)==B
def PJ(A,B):return lambda x:A(B(x))
def PG(A):return max(enumerate(A))[1]
def PE(A):return next(iter(A))
def PZ(A,B):return next(A for A in A if B(A))
def PP(A,B):return type(A)(A for A in A if B(A))
def Z(a,b):return type(a)(A for A in a if A not in b)
def PW(b):return not b
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):O=False;I=tuple(map(tuple,I));B=H(I,True,O,O);C=P(B,0);Q=PV(M,I);S=PJ(PW,Q);D=PP(C,S);F=PE(D);J=PG(D);K=Z(B,C);A=PJ(E,U);T=A(F);V=A(J);W=PS(A,T);X=PS(A,V);L=PZ(K,W);N=PZ(K,X);Y=G(F);a=G(J);b=G(L);c=G(N);d=R(Y,b);e=R(a,c);f=PQ(I,L,d);g=PQ(f,N,e);return[*map(list,g)]
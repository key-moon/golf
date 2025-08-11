def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def X(A,B,C,D):
	L=S(A)if D else None;M=set();G=set();Q,R=len(A),len(A[0]);T=J(A);V=U if C else P
	for E in T:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==L:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				K=A[F[0]][F[1]]
				if H==K if B else K!=L:N.add((K,F));G.add(F);O|={(A,B)for(A,B)in V(F)if 0<=A<Q and 0<=B<R}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def U(A):return P(A)|Z(A)
def G(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def L(A,B):return Y(Q(A,B))
def Q(A,B):return type(B)(A(B)for B in B)
def V(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def W(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def Y(A):return type(A)(B for A in A for B in A)
def E(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):B=True;I=tuple(map(tuple,I));C=X(I,B,B,B);D=U((0,0));F=L(U,D);H=W(E,3);J=Q(H,F);K=Y(C);N=V(G,K);A=L(N,J);O=G(A,(-1,1));P=G(A,(1,-1));R=M(I,A);S=M(R,O);T=M(S,P);return[*map(list,T)]
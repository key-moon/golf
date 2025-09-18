def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PU(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def R(A):return next(iter(A))[0]
def Y(A):return min(A for(B,A)in J(A))
def M(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();Q,R=len(A),len(A[0]);S=U(A);T=X if C else P
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PJ(A,B):return type(B)(A(B)for B in B)
def PZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def Q(A,B):return lambda x:A(B(x))
def G(a,b):return a,b
def V(A,B,C):return tuple(range(A,B,C))
def PE(A):return max(enumerate(A))[1]
def H(A):return next(iter(A))
def W(A,B):return type(A)(A for A in A if B(A))
def K(j):return 0,j
def S(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def L(A,B):return A in B
def PX(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));C=U(I);D=M(I,True,False,True);B=H(D);E=R(B);A=Y(B);F=V(A,10,2);J=PS(L,F);N=Q(J,PE);O=W(C,N);P=S(A);T=PX(A,3);X=V(P,10,4);Z=V(T,10,4);a=PZ(G,9);b=PJ(K,X);c=PJ(a,Z);d=PU(I,E,O);e=PU(d,5,b);f=PU(e,5,c);return[*map(list,f)]
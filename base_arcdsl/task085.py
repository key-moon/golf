def PS(A):return type(A)(B for A in A for B in A)
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PW(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def W(A,B,C,D):
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
def V(A):return tuple(map(max,zip(*J(A))))
def Y(A):return tuple(map(min,zip(*J(A))))
def PP(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def PZ(A,B):return PS(PL(A,B))
def PL(A,B):return type(B)(A(B)for B in B)
def PV(A,a,b):return lambda x:A(a(x),b(x))
def PY(A,n):
	if n==1:return A
	return K(A,PY(A,n-1))
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def K(A,B):return lambda x:A(B(x))
def PG(a,b):return tuple(zip(a,b))
def R(a,b):return a,b
def PM(A):return max(enumerate(A))[1]
def PJ(A):return next(iter(A))
def H(A):return tuple(A)
def Q(A,B):return type(A)(A for A in A if B(A))
def L(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def S(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PQ(n):return n%2==0
def M(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));C=W(I,True,False,True);A=H(C);D=K(S,Y);E=K(L,V);B=PL(D,A);F=PL(E,A);J=PP(G,B,F);N=PL(PM,B);O=K(PM,PJ);P=PY(PM,2);T=PV(M,O,P);U=K(PQ,T);X=PE(PX,R);Z=PE(K,U);a=K(Z,X);b=PV(Q,PJ,a);c=PG(J,N);d=PZ(b,c);e=PW(I,0,d);return[*map(list,e)]
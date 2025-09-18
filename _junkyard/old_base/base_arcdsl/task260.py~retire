def PU(A):return next(iter(A))
def PJ(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PY(A,B):return Q(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def R(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PQ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PP(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def M(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=L if C else S
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in U(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def V(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*U(A)))))
def Y(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*U(A)))))
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PZ(A,B):return PJ(PM(A,B))
def PM(A,B):return type(B)(A(B)for B in B)
def PW(A,a,b):return lambda x:A(a(x),b(x))
def PL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def G(A,B):return lambda x:A(x)==B
def K(A,B):return lambda x:A(B(x))
def PX(A,B):return PU(PS(B,A))
def PS(A,B):return type(B)(B for B in B if B!=A)
def W(A,B):return type(A)(A for A in A if B(A))
def Z(a,b):return type(a)(A for A in a if A not in b)
def H(a,b):return type(a)((*a,*b))
def PG(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));D=PP(I);E=M(I,True,False,True);F=PS(0,D);J=PX(F,5);A=P(E,5);L=PL(PE,I);N=K(L,Y);O=G(N,5);B=W(A,O);Q=Z(A,B);S=PM(Y,B);T=PM(V,Q);U=PV(PG,(-1,1));X=PV(PG,(1,-1));a=PM(U,S);b=PM(X,T);c=PV(PY,(1,1));d=PV(PY,(-1,-1));C=PW(H,c,d);e=PZ(C,a);f=PZ(C,b);g=H(e,f);h=PQ(I,J,g);i=R(h,5,0);return[*map(list,i)]
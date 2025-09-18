def PP(A,B):return type(A)(A for A in A if B(A))
def PW(A):return type(A)(B for A in A for B in A)
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def G(A):return max(A for(A,B)in U(A))
def W(A):return max(A for(B,A)in U(A))
def K(A):return min(A for(B,A)in U(A))
def M(A):return min(A for(A,B)in U(A))
def PM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-K(A)+1
def PL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return G(A)-M(A)+1
def PK(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in U(a)for(C,D)in U(b))
def R(a,b):return Q(a,b)==1
def X(a,b):return len(set(A for(B,A)in U(a))&set(A for(B,A)in U(b)))>0
def PG(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def V(A,B):
	H,I=PV(A);J,K=PV(B);C,D=0,0
	if X(A,B):C=1 if H<J else-1
	else:D=1 if I<K else-1
	E,F=C,D;G=0
	while not R(A,B)and G<42:G+=1;E+=C;F+=D;A=PG(A,(C,D))
	return E-C,F-D
def PJ(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PV(A):return M(A)+PL(A)//2,K(A)+PM(A)//2
def ZS(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def H(A,B,C,D):
	M=L(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);T=E(A);U=Y if C else S
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
def Y(A):return S(A)|J(A)
def Z(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PY(A,B):return PW(PH(A,B))
def PH(A,B):return type(B)(A(B)for B in B)
def ZZ(A,a,b):return lambda x:A(a(x),b(x))
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PE(A,B):return lambda x:A(B(x))
def PZ(a,b):return frozenset((B,A)for A in b for B in a)
def ZJ(A):return max(enumerate(A))[1]
def PQ(A):return next(iter(A))
def PU(A,B):return PW(PP(A,B))
def PX(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def ZP(A):return len(A)
def PS(a,b):return a>b
def P(a,b):return a&b
def ZU(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));A=H(I,True,False,True);F=Z(A,2);G=Z(A,8);B=PZ(F,G);J=ZZ(V,PQ,ZJ);K=PE(PX,J);C=PE(PV,PQ);D=ZZ(ZU,C,K);L=ZZ(PJ,C,D);M=PH(L,B);N=PR(PS,8);O=PE(N,ZP);E=PU(M,O);Q=ZS(I,2,E);R=PH(D,B);S=P(E,R);T=PY(Y,S);U=ZS(Q,8,T);return[*map(list,U)]
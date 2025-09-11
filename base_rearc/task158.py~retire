def YG(A,B):return type(B)(A(B)for B in B)
def HQ(A):return type(A)(B for A in A for B in A)
def Q(A):return max(A for(A,B)in V(A))
def M(A):return max(A for(B,A)in V(A))
def HP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-GY(A)+1
def HR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-R(A)+1
def YH(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def GY(A):return min(A for(B,A)in V(A))
def R(A):return min(A for(A,B)in V(A))
def Y(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return H(A)|Y(A)
def K(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def GX(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def GJ(A):return tuple(map(max,zip(*V(A))))
def G(A,B):
	C=set();K=X(B);D,E=len(A),len(A[0]);L,M=HW(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in HL(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def W(A):
	if len(A)==0:return frozenset({})
	B=V(A);C,D=Z(B);E,F=GJ(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def HV(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def GM(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=Z(A);J,K=-F,-G;L=HL(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return HL(frozenset(H),(F,G))
def HU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def GP(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return GL(GR(GL(A)))
def GR(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Z(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def GL(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Z(A)[1]+GJ(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def GQ(A):
	if isinstance(A,tuple):return A[::-1]
	B=Z(A)[0]+GJ(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def S(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def GH(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in V(A)if 0<=A<D and 0<=C<E)
def P(A):return len(GX(A))
def HG(A,B,C,D):
	N=U(A)if D else None;O=set();I=set();R,S=len(A),len(A[0]);T=K(A);V=E if C else H
	for F in T:
		if F in I:continue
		J=A[F[0]][F[1]]
		if J==N:continue
		P={(J,F)};L={F}
		while len(L)>0:
			Q=set()
			for G in L:
				M=A[G[0]][G[1]]
				if J==M if B else M!=N:P.add((M,G));I.add(G);Q|={(A,B)for(A,B)in V(G)if 0<=A<R and 0<=B<S}
			L=Q-I
		O.add(frozenset(P))
	return frozenset(O)
def H(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A):
	if len(A)==0:return A
	return HL(A,(-R(A),-GY(A)))
def HL(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def GU(A,B):return frozenset((A,B)for B in V(B))
def V(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return tuple(map(min,zip(*V(A))))
def HW(A):return HR(A),HP(A)
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def HJ(A,B):return HQ(YG(A,B))
def HY(A,B):return type(A)(A(B)for A in A)
def YY(A,a,b):return lambda x:A(a(x),b(x))
def HX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def HS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def GS(A,B):return lambda x:A(x)==B
def HZ(h,g,f):return lambda x:h(g(f(x)))
def HH(A,B):return lambda x:A(B(x))
def GW(a,b):return frozenset((B,A)for A in b for B in a)
def GG(A,B,C):return tuple(range(A,B,C))
def HM(A,B):return B.union(frozenset({A}))
def YJ(A):return max(enumerate(A))[1]
def HK(A):return next(iter(A))
def GK(A,B):return HQ(GV(A,B))
def GV(A,B):return type(A)(A for A in A if B(A))
def GZ(A):return frozenset({A})
def HE(A,B):return B(max(A,key=B,default=0))
def J(a,b):return type(a)(A for A in a if A not in b)
def GE(a,b):return type(a)((*a,*b))
def YV(b):return not b
def YM(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def L(x):return x
def p(I):I=tuple(map(tuple,I));D=HG(I,False,True,True);A=U(I);K=HE(D,P);M=GS(P,K);N=GK(D,M);O=W(N);Q=GH(O,I);R=GS(HK,A);T=HH(YV,R);E=GV(Q,T);Y=U(E);a=GZ(L);b=HM(GR,a);c=HM(GP,b);d=HM(GQ,c);e=HM(GL,d);f=HW(I);g=YM(2,f);h=HV(A,g);i=S(I);j=HL(i,(1,1));k=HU(h,j);l=GG(1,5,1);m=GS(HK,Y);n=HH(YV,m);o=HS(GV,n);B=HH(X,o);F=HZ(X,V,B);p=HX(GM,E);q=HH(GZ,YJ);r=HH(p,HK);s=YY(HY,q,r);C=HZ(X,HK,s);t=HH(X,B);u=HX(GU,A);v=HX(HJ,H);w=HH(v,F);x=YY(J,w,F);y=HH(u,x);z=YY(GE,t,y);A0=HH(z,C);A1=HX(HX,HL);A2=HZ(Z,B,C);A3=YY(HL,C,A2);A4=HH(A1,A3);A5=HX(G,k);A6=HH(A5,A0);A7=YY(HJ,A4,A6);A8=GW(l,e);A9=HJ(A7,A8);AA=HU(I,A9);return[*map(list,AA)]
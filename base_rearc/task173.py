def GQ(A):return type(A)(B for A in A for B in A)
def Y(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def M(A):return H(A)|Y(A)
def H(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def K(A):return max(A for(A,B)in J(A))
def E(A):return min(A for(A,B)in J(A))
def HG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return max(A for(B,A)in J(A))
def L(A):return min(A for(B,A)in J(A))
def GP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-L(A)+1
def GR(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return K(A)-E(A)+1
def GL(A):return GR(A),GP(A)
def G(A,B):
	C=set();K=R(B);D,E=len(A),len(A[0]);L,M=GL(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in GS(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def GU(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def Q(A):return len(GG(A))
def GG(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def GJ(A,B,C,D):
	L=X(A)if D else None;N=set();G=set();Q,R=len(A),len(A[0]);S=U(A);T=M if C else H
	for E in S:
		if E in G:continue
		I=A[E[0]][E[1]]
		if I==L:continue
		O={(I,E)};J={E}
		while len(J)>0:
			P=set()
			for F in J:
				K=A[F[0]][F[1]]
				if I==K if B else K!=L:O.add((K,F));G.add(F);P|={(A,B)for(A,B)in T(F)if 0<=A<Q and 0<=B<R}
			J=P-G
		N.add(frozenset(O))
	return frozenset(N)
def R(A):
	if len(A)==0:return A
	return GS(A,(-E(A),-L(A)))
def GS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def S(A):return tuple(map(min,zip(*J(A))))
def GM(A,B):return GQ(GZ(A,B))
def GZ(A,B):return type(B)(A(B)for B in B)
def HH(A,a,b):return lambda x:A(a(x),b(x))
def GX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def GH(A,B):return lambda x:A(x)==B
def GW(h,g,f):return lambda x:h(g(f(x)))
def GV(A,B):return lambda x:A(B(x))
def HY(A):return max(enumerate(A))[1]
def GK(A):return next(iter(A))
def GY(A):return tuple(A)
def W(A,B):return type(A)(A for A in A if B(A))
def Z(a,b):return type(a)((*a,*b))
def GE(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def P(x):return x
def p(I):I=tuple(map(tuple,I));E=GJ(I,False,True,True);F=GH(Q,2);H=W(E,F);J=GZ(R,H);K=GW(GK,GY,GG);L=GW(HY,GY,GG);M=GX(GH,GK);N=GV(M,K);O=GX(GH,GK);T=GV(O,L);A=HH(W,P,N);B=HH(W,P,T);C=GX(G,I);U=GW(GE,S,A);V=GW(GE,S,B);D=GX(GX,GS);X=HH(GS,P,U);Y=HH(GS,P,V);a=GV(D,X);b=GV(C,A);c=HH(GM,a,b);d=GV(D,Y);e=GV(C,B);f=HH(GM,d,e);g=HH(Z,c,f);h=GM(g,J);i=GU(I,h);return[*map(list,i)]
def HR(A,B):return type(B)(A(B)for B in B)
def HJ(A):return type(A)(B for A in A for B in A)
def HX(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Y(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def R(A):return H(A)|Y(A)
def Q(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def HM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-GG(A)+1
def GL(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return P(A)-U(A)+1
def GH(A):return tuple(map(max,zip(*M(A))))
def Z(A):return tuple(map(min,zip(*M(A))))
def E(A):return max(A for(B,A)in M(A))
def GG(A):return min(A for(B,A)in M(A))
def P(A):return max(A for(A,B)in M(A))
def U(A):return min(A for(A,B)in M(A))
def GE(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def HH(A,B):return GE(A,(A[0]+42*B[0],A[1]+42*B[1]))
def GS(A):G,H=U(A)-1,GG(A)-1;I,J=P(A)+1,E(A)+1;B,C=min(G,I),min(H,J);D,F=max(G,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,F)for A in range(B,D+1)};L={(B,A)for A in range(C,F+1)}|{(D,A)for A in range(C,F+1)};return frozenset(K|L)
def L(A):
	if len(A)==0:return frozenset({})
	B=M(A);C,D=Z(B);E,F=GH(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def GW(A):return U(A)+GL(A)//2,GG(A)+HM(A)//2
def HG(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def GX(A,B,C,D):
	M=K(A)if D else None;N=set();G=set();S,T=len(A),len(A[0]);U=Q(A);V=R if C else H
	for E in U:
		if E in G:continue
		I=A[E[0]][E[1]]
		if I==M:continue
		O={(I,E)};J={E}
		while len(J)>0:
			P=set()
			for F in J:
				L=A[F[0]][F[1]]
				if I==L if B else L!=M:O.add((L,F));G.add(F);P|={(A,B)for(A,B)in V(F)if 0<=A<S and 0<=B<T}
			J=P-G
		N.add(frozenset(O))
	return frozenset(N)
def H(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def GV(A,B):return frozenset((A,B)for B in M(B))
def M(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def K(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def GQ(A,B):return HJ(HR(A,B))
def GK(A,B):return type(A)(A(B)for A in A)
def HU(A,a,b):return lambda x:A(a(x),b(x))
def HV(A,n):
	if n==1:return A
	return GU(A,HV(A,n-1))
def GZ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def GM(A,B):return lambda x:A(x)==B
def HE(h,g,f):return lambda x:h(g(f(x)))
def GU(A,B):return lambda x:A(B(x))
def HY(A):return next(iter(A))
def GY(A,B):return type(A)(A for A in A if B(A))
def X(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def GR(A):return frozenset({A})
def HK(A):return len(A)
def V(a,b):return type(a)(A for A in a if A not in b)
def G(a,b):return a&b
def GJ(a,b):return type(a)((*a,*b))
def GP(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def S(x):return x
def p(I):D=False;I=tuple(map(tuple,I));E=GX(I,D,D,True);F=GZ(GM,HY);N=GU(F,J);O=HU(GY,S,N);A=GU(GW,O);P=GU(H,A);Q=HU(V,P,M);R=GU(HY,Q);C=HU(W,R,A);T=GU(GP,C);U=HU(HH,A,T);Y=HU(G,M,U);Z=HE(X,HK,Y);B=HU(HH,A,C);a=GZ(HV,GS);b=GU(a,Z);c=GU(GR,b);d=HU(GK,c,B);e=HE(L,HY,d);f=HU(GV,J,B);g=HU(V,e,B);h=HU(GV,K,g);i=HU(GJ,f,h);j=GQ(i,E);k=HG(I,j);return[*map(list,k)]
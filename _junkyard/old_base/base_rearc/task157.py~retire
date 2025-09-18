def HW(A,B):return type(B)(A(B)for B in B)
def HZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def GG(A):return min(A for(B,A)in M(A))
def X(A):return min(A for(A,B)in M(A))
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Q(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def GH(A):return tuple(map(max,zip(*M(A))))
def Z(A):return tuple(map(min,zip(*M(A))))
def GP(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Z(A)[1]+GH(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def YM(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def HK(A,B):return YJ(A,K(A),M(B))
def HG(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(YM(A,(B*C+C*E,0),(B,D))for C in range(n))
def YJ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in M(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def GX(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return GP(GV(GP(A)))
def GV(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Z(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def GR(A):
	if isinstance(A,tuple):return A[::-1]
	B=Z(A)[0]+GH(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def L(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def HR(A):return next(iter(A))[0]
def S(A):return len(GM(A))
def GM(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def P(A):return max(A for(A,B)in M(A))
def GL(A,B,C,D):
	M=K(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=Q(A);U=E if C else Y
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);P|={(A,B)for(A,B)in U(G)if 0<=A<R and 0<=B<S}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def E(A):return Y(A)|J(A)
def Y(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):
	if len(A)==0:return A
	return HP(A,(-X(A),-GG(A)))
def HP(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def GQ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def H(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def HM(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return P(A)-X(A)+1
def K(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def HH(A,B):return HX(HW(A,B))
def GZ(A,B):return type(A)(A(B)for A in A)
def YG(A,a,b):return lambda x:A(a(x),b(x))
def HE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def HQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def GU(A,B):return lambda x:A(x)==B
def HL(h,g,f):return lambda x:h(g(f(x)))
def GW(A,B):return lambda x:A(B(x))
def GK(a,b):return a,b
def HS(A,B):return HU(HJ(B,A))
def HJ(A,B):return type(B)(B for B in B if B!=A)
def HU(A):return next(iter(A))
def GY(A,B):return type(A)(A for A in A if B(A))
def R(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def YH(a,b):return a and b
def GS(A):return frozenset({A})
def HV(A,B):return min(A,key=B)
def HY(A,B):return max(A,key=B)
def HX(A):return type(A)(B for A in A for B in A)
def YV(A):return len(A)
def GE(a,b):return a>b
def V(a,b):return type(a)(A for A in a if A not in b)
def G(a,b):return a&b
def GJ(a,b):return type(a)((*a,*b))
def YY(b):return not b
def YE(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def W(x):return x
def p(I):F=True;I=tuple(map(tuple,I));X=GK(W,GV);Z=GK(GX,GR);a=GJ(X,Z);b=YG(HG,W,HM);B=HL(L,HU,b);C=K(I);c=HE(HL,S);d=HE(c,B);e=HE(HL,HR);f=HE(e,B);g=HQ(GZ,I);h=GW(GS,d);i=HL(HU,g,h);j=HQ(GZ,I);k=GW(GS,f);l=HL(HU,j,k);m=GU(i,1);n=GU(l,C);o=GW(YY,n);p=YG(YH,m,o);J=HY(a,p);A=J(I);q=B(A);N=HR(q);r=GM(A);s=HJ(N,r);t=HS(s,C);u=GL(A,F,F,F);O=H(u,t);Q=GQ(A,N);D=GQ(A,C);v=HH(E,D);w=HH(E,v);x=P(Q);y=Y((0,0));z=HJ((1,0),y);A0=HQ(HH,z);A1=HE(HL,A0);A2=HE(HE,YE);A3=HQ(A1,A2);A4=HE(HE,GW);A5=HE(HE,HP);A6=HL(A3,A4,A5);A7=HE(HL,YV);A8=HQ(G,Q);A9=HE(A7,A8);AA=HQ(GU,0);AB=HE(HE,HP);AC=HL(AA,A9,AB);AD=HQ(HL,HU);AE=HQ(AD,R);AF=HE(GE,x);AG=AE(AF);AH=HQ(GY,AG);AI=HE(GW,AH);AJ=HE(HL,YV);AK=HQ(V,D);AL=HE(AJ,AK);AM=HQ(GU,0);AN=HE(HE,HP);AO=HL(AM,AL,AN);AP=HE(HL,YV);AQ=HQ(G,D);AR=HE(AP,AQ);AS=HE(YG,V);AT=GW(AI,A6);AU=HE(HE,HP);AV=YG(AS,AT,AU);AW=GW(AR,AV);AX=HQ(GU,0);AY=GW(AX,AW);AZ=HE(YG,YH);Aa=YG(AZ,AY,AO);Ab=HE(YG,YH);Ac=YG(Ab,AC,Aa);T=GW(U,M);Ad=HE(GY,w);Ae=HL(Ad,Ac,T);Af=HQ(HV,HU);Ag=GW(Af,Ae);Ah=YG(HP,T,Ag);Ai=HH(Ah,O);Aj=HX(O);Ak=HK(A,Aj);Al=YJ(Ak,1,Ai);Am=J(Al);return[*map(list,Am)]
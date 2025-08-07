def PH(A,B):return type(B)(B for B in B if B!=A)
def ZJ(A):return next(iter(A))
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|J(A)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def ZP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return W(A)-R(A)+1
def PK(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return K(A)-M(A)+1
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def ZE(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(a,b):return len(set(A for(B,A)in U(a))&set(A for(B,A)in U(b)))>0
def ZU(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def ZL(A,B):return PE(A,(A[0]+42*B[0],A[1]+42*B[1]))
def V(A,B):
	H,I=PR(A);J,K=PR(B);C,D=0,0
	if X(A,B):C=1 if H<J else-1
	else:D=1 if I<K else-1
	E,F=C,D;G=0
	while not PP(A,B)and G<42:G+=1;E+=C;F+=D;A=ZU(A,(C,D))
	return E-C,F-D
def ZS(A,B):return ZM(A,L(A),U(B))
def PE(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PR(A):return M(A)+PK(A)//2,R(A)+ZP(A)//2
def PM(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def Q(A,B,C):
	G,H=len(A),len(A[0]);I=L(A);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def ZM(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PP(a,b):return G(a,b)==1
def G(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in U(a)for(C,D)in U(b))
def ZY(A):return PK(A)==len(A)and ZP(A)==1
def W(A):return max(A for(B,A)in U(A))
def R(A):return min(A for(B,A)in U(A))
def K(A):return max(A for(A,B)in U(A))
def M(A):return min(A for(A,B)in U(A))
def PS(A,B,C,D):
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
def PX(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def ZV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PL(A,B):return lambda x:A(B(x))
def PQ(A,a,b):return a if A else b
def PY(a,b):return a,b
def ZX(A,B):return ZJ(PH(B,A))
def PJ(A,B):return type(A)(A for A in A if B(A))
def PV(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def ZW(a,b):return a and b
def PZ(A):return frozenset({A})
def PG(A,B):return max(A,key=B)
def ZZ(A):return type(A)(B for A in A for B in A)
def PU(a,b):return a>b
def Z(a,b):return type(a)(A for A in a if A not in b)
def PW(a,b):return type(a)((*a,*b))
def H(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def ZQ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):T=False;I=tuple(map(tuple,I));D=PX(I,2);A=PX(I,3);U=ZY(D);E=ZY(A);B=PR(D);J=PQ(E,M,W);X=J(D);Y=J(A);a=PU(X,Y);b=ZW(E,a);c=PQ(b,K,M);d=c(A);e=PQ(E,R,W);f=e(A);C=PY(d,f);g=ZX(A,C);h=H(C,g);i=ZL(C,h);L=Q(I,1,i);j=PS(L,True,T,T);N=P(j,1);k=ZV(PP,A);l=PJ(N,k);m=Z(N,l);n=ZZ(m);O=ZS(L,n);o=ZL(B,(1,0));p=ZL(B,(-1,0));q=ZL(B,(0,-1));r=ZL(B,(0,1));s=PW(o,p);t=PW(q,r);u=PQ(U,s,t);v=PX(O,1);w=PZ(C);x=ZV(G,w);y=PL(x,PZ);F=PG(v,y);z=PZ(F);A0=V(z,u);A1=PV(A0);S=ZQ(F,A1);A2=PE(F,S);A3=ZM(O,1,A2);A4=PE(S,B);A5=Q(A3,1,A4);A6=PM(A5,1,3);return[*map(list,A6)]
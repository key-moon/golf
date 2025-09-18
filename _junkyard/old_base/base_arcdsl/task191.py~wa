def PV(A):return type(A)(B for A in A for B in A)
def X(A):return max(A for(A,B)in S(A))
def E(A):return max(A for(B,A)in S(A))
def Y(A):return min(A for(B,A)in S(A))
def U(A):return min(A for(A,B)in S(A))
def PK(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def ZU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PW(A):return PU(A),PY(A)
def K(A,B):return ZU(B,L(A),PW(A))
def ZJ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PE(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PL(A):return tuple(tuple(A[::-1])for A in A[::-1])
def PQ(A):return tuple(A for A in zip(*A[::-1]))
def J(A):
	if len(A)==0:return A
	return PG(A,(-U(A),-Y(A)))
def PG(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def L(A):return tuple(map(min,zip(*S(A))))
def R(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-Y(A)+1
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-U(A)+1
def W(A,a,b):return PV(PJ(A,a,b))
def PJ(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def PX(A,B):return PV(ZP(A,B))
def ZP(A,B):return type(B)(A(B)for B in B)
def ZS(A,a,b):return lambda x:A(a(x),b(x))
def PR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PH(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def H(A,B):return lambda x:A(x)==B
def PM(h,g,f):return lambda x:h(g(f(x)))
def PP(A,B):return lambda x:A(B(x))
def G(a,b):return frozenset((B,A)for A in b for B in a)
def PZ(a,b):return a,b
def V(A,B,C):return tuple(range(A,B,C))
def Q(A,B):return type(A)(A for A in A if B(A))
def Z(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def ZZ(A):return len(A)
def P(a,b):return type(a)(A for A in a if A not in b)
def PS(a,b):return type(a)((*a,*b))
def M(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));O=PU(I);S=PY(I);B=R(I,1);T=R(I,4);U=L(B);A=K(B,I);X=PQ(A);Y=PL(A);a=PE(A);b=H(ZZ,0);c=PH(R,1);d=PP(J,c);e=PH(R,4);f=PH(PG,U);g=PP(f,e);h=PR(M,O);i=PM(Z,h,PU);j=PR(M,S);k=PM(Z,j,PY);l=PH(V,1);C=PR(l,0);m=PP(C,i);n=PP(C,k);o=ZS(G,m,n);p=PH(PG,(-1,-1));D=PR(PR,PG);q=PM(D,p,d);r=PZ(A,X);s=PZ(Y,a);E=PS(r,s);F=ZP(g,E);t=PR(P,T);u=ZP(t,F);N=ZP(J,F);v=ZP(o,N);w=PR(PH,P);x=ZP(D,N);y=ZP(w,u);z=PJ(PP,y,x);A0=PR(PP,b);A1=ZP(A0,z);A2=PJ(Q,v,A1);A3=ZP(q,E);A4=W(PX,A3,A2);A5=ZJ(I,1,A4);return[*map(list,A5)]
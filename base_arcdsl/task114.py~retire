def X(A):return max(A for(A,B)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def U(A):return max(A for(B,A)in Z(A))
def Y(A):return min(A for(B,A)in Z(A))
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-Y(A)+1
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-J(A)+1
def G(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*Z(A)))))
def W(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*Z(A)))))
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return tuple(map(max,zip(*Z(A))))
def L(A):return tuple(map(min,zip(*Z(A))))
def PR(A):
	if len(A)==0:return A
	F,G=L(A);H,I=V(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def K(A):return frozenset({L(A),W(A),G(A),V(A)})
def PJ(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def M(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def E(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in Z(a)for(C,D)in Z(b))
def PY(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def S(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PX(A):return PS(A),PU(A)
def PG(A,B):return type(B)(A(B)for B in B)
def PK(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PE(h,g,f):return lambda x:h(g(f(x)))
def H(A,B):return lambda x:A(B(x))
def PP(a,b):return a,b
def PL(A):return next(iter(A))
def R(A):return frozenset({A})
def PZ(A,B):return min(A,key=B)
def P(a,b):return type(a)(A for A in a if A not in b)
def PH(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def Q(x):return x
def p(I):I=tuple(map(tuple,I));C=PX(I);D=PH(C,2);A=PJ(0,D);F=M(I);B=PY(F,(1,1));G=PW(A,B);J=S(A);L=PK(P,PR,K);N=L(J);O=PM(PM,E);T=PQ(H,R);U=PE(T,O,R);V=PM(PZ,B);W=PE(PL,V,U);X=PK(PP,W,Q);Y=PG(X,N);Z=PW(G,Y);return[*map(list,Z)]
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PS(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def V(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def M(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(PS(A,(0,B*C+C*E),(D,B))for C in range(n))
def J(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def Z(A):return tuple(map(min,zip(*P(A))))
def U(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def R(A,B):return type(B)(A(B)for B in B)
def PZ(A,a,b):return lambda x:A(a(x),b(x))
def H(A,n):
	if n==1:return A
	return X(A,H(A,n-1))
def K(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def E(A,B):return lambda x:A(x)==B
def Q(h,g,f):return lambda x:h(g(f(x)))
def X(A,B):return lambda x:A(B(x))
def L(a,b):return a,b
def W(A):return type(A)(B for A in A for B in A)
def PP(A):return len(A)
def Y(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def S(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PJ(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));D=M(I,3);F=L(2,1);B=K(U,0);A=X(Z,B);G=X(PP,B);N=E(G,0);O=E(A,(1,1));P=E(A,(1,0));T=E(A,F);a=K(S,3);C=H(Y,2);b=X(Y,N);c=Q(C,Y,O);d=X(a,P);e=X(C,T);f=PZ(PJ,b,c);g=PZ(PJ,d,e);h=PZ(PJ,f,g);i=K(V,(1,1));j=X(i,h);k=R(j,D);l=W(k);m=J(l,3);return[*map(list,m)]
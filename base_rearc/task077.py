def GG(A):return type(A)(B for A in A for B in A)
def GM(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def H(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def R(A):return tuple(map(max,zip(*H(A))))
def E(A):return tuple(map(min,zip(*H(A))))
def V(A):
	if len(A)==0:return frozenset({})
	B=H(A);C,D=E(B);F,G=R(A);return frozenset((A,B)for A in range(C,F+1)for B in range(D,G+1))
def GX(A,B,C):
	G,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in H(C):
		if 0<=E<G and 0<=F<I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def P(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def G(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def L(A,B):return GG(GV(A,B))
def GV(A,B):return type(B)(A(B)for B in B)
def GE(A,a,b):return lambda x:A(a(x),b(x))
def GH(A,n):
	if n==1:return A
	return S(A,GH(A,n-1))
def W(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def GY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def GJ(h,g,f):return lambda x:h(g(f(x)))
def S(A,B):return lambda x:A(B(x))
def Q(a,b):return a,b
def GR(A):return max(enumerate(A))[1]
def Z(A):return next(iter(A))
def X(A,B):return type(A)(A for A in A if B(A))
def GU(x):
	if isinstance(x,int):return 0 if x==0 else 1 if x>0 else-1
	return 0 if x[0]==0 else 1 if x[0]>0 else-1,0 if x[1]==0 else 1 if x[1]>0 else-1
def U(A):return max(A,default=0)
def K(a,b):return a>b
def Y(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def M(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def J(x):return x
def p(I):I=tuple(map(tuple,I));A=G(I);B=P(I,A);C=GE(M,Z,GR);D=GE(Y,GU,J);E=S(D,C);F=W(K,3);H=GJ(F,U,E);N=W(W,Q);O=GY(GJ,N);R=W(S,H);T=GY(O,R);a=W(W,X);b=S(T,a);c=W(L,V);d=GE(GV,b,J);e=S(c,d);f=GH(e,2);g=f(B);h=GX(I,4,g);i=GX(h,A,B);return[*map(list,i)]
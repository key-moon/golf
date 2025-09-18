def Y(A):return max(A for(A,B)in J(A))
def E(A):return min(A for(A,B)in J(A))
def L(A):return max(A for(B,A)in J(A))
def V(A):return min(A for(B,A)in J(A))
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-V(A)+1
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-E(A)+1
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A):return frozenset((A[0],B)for B in range(30))
def X(A):return frozenset((B,A[1])for B in range(30))
def PP(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PY(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def W(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in J(A)if 0<=A<D and 0<=C<E)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def Q(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def PJ(A):return H(A),PZ(A)
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PL(A,a,b):return lambda x:A(a(x),b(x))
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def K(A,B):return lambda x:A(x)==B
def PS(h,g,f):return lambda x:h(g(f(x)))
def G(A,B):return next(A for A in A if B(A))
def PX(A):return len(A)
def R(a,b):return type(a)((*a,*b))
def M(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def PV(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));C=PJ(I);B=Q(I,5);D=PY(I,0,B);A=S(D);E=PX(B);F=Q(I,A);H=PE(W,I);J=PE(P,A);L=PS(J,H,Z);N=K(L,4);O=G(F,N);T=M((1,-1),E);V=PV(T,O);Y=PP(0,C);a=PL(R,X,U);b=a(V);c=PY(Y,A,b);return[*map(list,c)]
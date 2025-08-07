def PZ(A):return type(A)(B for A in A for B in A)
def J(A):return max(A for(A,B)in P(A))
def S(A):return max(A for(B,A)in P(A))
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(A):return min(A for(B,A)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return S(A)-U(A)+1
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-Z(A)+1
def Y(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def H(A):return Z(A)+G(A)//2,U(A)+PP(A)//2
def PX(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def R(A):return tuple(tuple(A[::-1])for A in A[::-1])
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def V(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def K(A,B):return PZ(PE(A,B))
def PE(A,B):return type(B)(A(B)for B in B)
def PU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def M(a,b):return a,b
def X(A,B,C):return tuple(range(A,B,C))
def Q(i):return i,0
def W(a,b):return type(a)((*a,*b))
def E(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def L(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));D=V(I,8);F=H(D);G=Y((0,0),(1,0));J=Y((0,0),(0,2));N=W(G,J);A=L(F,(2,0));O=PS(N,A);P=M(-2,2);S=X(0,5,1);T=PU(E,P);U=PE(T,S);Z=PU(PS,O);B=K(Z,U);a=PX(I,5,B);C=R(a);b=V(C,8);c=H(b);d=L(c,A);e=PS(B,d);f=Q(-2);g=PS(e,f);h=PX(C,5,g);i=R(h);return[*map(list,i)]
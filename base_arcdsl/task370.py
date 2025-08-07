def PX(A):return type(A)(B for A in A for B in A)
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def E(A):return max(A for(A,B)in S(A))
def U(A):return max(A for(B,A)in S(A))
def L(A):return min(A for(B,A)in S(A))
def J(A):return min(A for(A,B)in S(A))
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-J(A)+1
def PU(A):return J(A)+PS(A)//2,L(A)+PE(A)//2
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def R(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def Q(a,b):
	A,B=PU(S(a));C,D=PU(S(b))
	if A==C:return 0,1 if B<D else-1
	elif B==D:return 1 if A<C else-1,0
	elif A<C:return 1,1 if B<D else-1
	elif A>C:return-1,1 if B<D else-1
def PG(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PY(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A):return tuple(map(max,zip(*S(A))))
def X(A):return tuple(map(min,zip(*S(A))))
def H(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PL(A):return PS(A),PE(A)
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PJ(A,B):return PX(PW(A,B))
def PW(A,B):return type(B)(A(B)for B in B)
def PQ(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PZ(A,a,b):return a if A else b
def V(A,B,C):return tuple(range(A,B,C))
def PP(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def P(a,b):return a&b
def K(a,b):return a==b
def Y(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def PK(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def G(x):return x
def p(I):I=tuple(map(tuple,I));B=Z(I);A=H(I,0);D=H(I,B);E=Q(A,D);F=PQ(R,X,M);C=F(A);J=P(A,C);L=K(C,J);N=PQ(W,G,PP);O=PQ(PK,G,N);S=PZ(L,G,O);T=PL(A);U=Y(T,E);a=PW(S,U);b=V(1,5,1);c=PM(Y,a);d=PW(c,b);e=PM(PY,A);f=PJ(e,d);g=PG(I,B,f);return[*map(list,g)]
def PE(A,B):return type(B)(A(B)for B in B)
def H(A):return type(A)(B for A in A for B in A)
def PS(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PU(A,B):return Y(A,(A[0]+42*B[0],A[1]+42*B[1]))
def U(A,B,C):
	G,H=len(A),len(A[0]);I=Z(A);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PL(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def S(A):return min(A for(A,B)in P(A))
def V(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def K(A,B):return H(PE(A,B))
def PX(A,a,b):return lambda x:A(a(x),b(x))
def PJ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def M(A,B):return lambda x:A(x)==B
def PP(h,g,f):return lambda x:h(g(f(x)))
def W(A,B):return lambda x:A(B(x))
def PZ(A):return next(iter(A))
def X(A,B):return type(A)(A for A in A if B(A))
def Q(i):return i,0
def J(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def L(a,b):return a>b
def G(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def R(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def E(x):return x
def p(I):I=tuple(map(tuple,I));C=V(I,1);D=V(I,2);F=V(I,5);H=S(F);B=PP(Q,J,G);N=PJ(L,H);A=W(N,PZ);O=PP(R,B,A);P=PX(PU,E,O);T=W(B,A);Y=PX(PU,E,T);Z=PJ(M,A);a=W(Z,A);b=PX(X,Y,a);c=K(P,C);d=K(b,D);e=U(I,2,d);f=PL(e,1,c);return[*map(list,f)]
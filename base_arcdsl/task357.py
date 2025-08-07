def U(A):return max(A for(A,B)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def J(A):return max(A for(B,A)in P(A))
def X(A):return min(A for(B,A)in P(A))
def L(A):return tuple(map(max,zip(*P(A))))
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PS(A):return R(A),PP(A)
def W(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PE(A,B):return W(A,(A[0]+42*B[0],A[1]+42*B[1]))
def K(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def V(A,B):return PL(B,E(A),PS(A))
def PX(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A):
	if isinstance(A,tuple):return A[::-1]
	B=E(A)[0]+L(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def PL(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def Y(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*P(A)))))
def E(A):return tuple(map(min,zip(*P(A))))
def Q(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-Z(A)+1
def G(a,b):return a,b
def PJ(A):return next(iter(A))
def S(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def PZ(A):return type(A)(B for A in A for B in A)
def H(A,B):return tuple(A for B in range(B))
def p(I):I=tuple(map(tuple,I));J=R(I);L=Q(I,1);N=PJ(L);O=PE(N,(-1,1));B=PX(I,1,O);P=Q(B,1);T=Y(P);U=PE(T,(-1,-1));A=PX(B,1,U);C=Q(A,1);D=V(C,A);W=R(D);F=PP(D);X=S(W);Z=G(X,F);a=E(C);b=PL(A,a,Z);c=H(b,9);d=PZ(c);e=G(J,F);f=PL(d,(0,0),e);g=M(f);h=K(g,0,8);return[*map(list,h)]
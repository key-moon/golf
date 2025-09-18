def W(A,B):return type(B)(A(B)for B in B)
def Y(A):return type(A)(B for A in A for B in A)
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def U(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def Q(A,B):return U(A,(A[0]+42*B[0],A[1]+42*B[1]))
def R(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def S(A):return tuple(map(max,zip(*P(A))))
def E(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def L(A,B):return Y(W(A,B))
def V(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def M(h,g,f):return lambda x:h(g(f(x)))
def H(A):return max(enumerate(A))[1]
def X(A,B):return type(A)(A for A in A if B(A))
def J(a,b):return type(a)((*a,*b))
def K(n):return n%2==0
def Z(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));C=E(I,7);A=S(C);D=Q(A,(-1,1));F=Q(A,(-1,-1));G=J(D,F);N=V(Q,(-1,0));B=L(N,G);O=H(A);P=V(Z,O);T=M(K,P,H);U=R(I,8,B);W=X(B,T);Y=R(U,7,W);return[*map(list,Y)]
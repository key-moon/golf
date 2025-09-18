def GZ(A,B):return type(B)(A(B)for B in B)
def P(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def V(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return max(A for(A,B)in H(A))
def J(A):return min(A for(A,B)in H(A))
def Y(A):return max(A for(B,A)in H(A))
def U(A):return min(A for(B,A)in H(A))
def GP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-U(A)+1
def GE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return M(A)-J(A)+1
def HG(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def H(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def K(A):return tuple(map(max,zip(*H(A))))
def GX(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def W(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=X(A)[1]+K(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def S(A):
	if isinstance(A,tuple):return A[::-1]
	B=X(A)[0]+K(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def GU(A):return next(iter(A))[0]
def GM(A):return len(A)==len(A[0])if isinstance(A,tuple)else GE(A)*GP(A)==len(A)and GE(A)==GP(A)
def G(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in P(A)-{V(A)})
def GL(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def X(A):return tuple(map(min,zip(*H(A))))
def GJ(A,B):return GK(GZ(A,B))
def GY(A,B):return type(A)(A(B)for A in A)
def HH(A,a,b):return lambda x:A(a(x),b(x))
def GR(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def GS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def L(A,B):return lambda x:A(x)==B
def GW(h,g,f):return lambda x:h(g(f(x)))
def GH(A,B):return lambda x:A(B(x))
def GV(A,B):return B.union(frozenset({A}))
def GQ(A):return next(iter(A))
def GG(A,B):return next(A for A in A if B(A))
def Q(A,B):return type(A)(A for A in A if B(A))
def HY(a,b):return a and b
def Z(A):return frozenset({A})
def GK(A):return type(A)(B for A in A for B in A)
def HJ(A):return len(A)
def R(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def E(x):return x
def p(I):I=tuple(map(tuple,I));A=G(I);C=L(HJ,4);D=HH(HY,GM,C);B=GG(A,D);F=GU(B);H=GK(A);J=GH(S,W);K=Z(J);M=GV(W,K);N=GV(S,M);O=GY(N,H);P=X(B);T=GR(R,P);U=L(GQ,F);V=GS(Q,U);Y=GW(T,X,V);a=HH(GL,E,Y);b=GJ(a,O);c=GX(I,b);return[*map(list,c)]
def GS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def GW(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def H(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return max(A for(B,A)in H(A))
def P(A):return min(A for(B,A)in H(A))
def E(A):return max(A for(A,B)in H(A))
def V(A):return min(A for(A,B)in H(A))
def GV(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def GK(A,B):return GV(A,(A[0]+42*B[0],A[1]+42*B[1]))
def GE(A):G,H=V(A)-1,P(A)-1;I,J=E(A)+1,Y(A)+1;B,C=min(G,I),min(H,J);D,F=max(G,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,F)for A in range(B,D+1)};L={(B,A)for A in range(C,F+1)}|{(D,A)for A in range(C,F+1)};return frozenset(K|L)
def Z(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=K(A);J,L=-F,-G;M=GS(A,(J,L));H=set()
		for(E,(N,O))in M:
			for P in range(B):
				for Q in range(B):H.add((E,(N*B+P,O*B+Q)))
		return GS(frozenset(H),(F,G))
def HG(A,B,C):
	G,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in H(C):
		if 0<=E<G and 0<=F<I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Q(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in H(A)if 0<=A<D and 0<=C<E)
def R(A):return len(GH(A))
def GH(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def S(A):return tuple(map(max,zip(*H(A))))
def L(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*H(A)))))
def U(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*H(A)))))
def K(A):return tuple(map(min,zip(*H(A))))
def GJ(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def GQ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return Y(A)-P(A)+1
def GX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-V(A)+1
def M(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def GZ(A,a,b):return lambda x:A(a(x),b(x))
def GU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def GP(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def GY(A,B):return lambda x:A(x)==B
def GL(h,g,f):return lambda x:h(g(f(x)))
def GM(A,B):return lambda x:A(B(x))
def W(A,B):return type(A)(A for A in A if B(A))
def J(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def GR(A,B):return min(A,key=B)
def G(a,b):return a&b
def GG(a,b):return type(a)((*a,*b))
def X(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));C=R(I);D=J(C);B=Z(I,D);E=GP(Q,I);F=GU(GJ,I);H=GM(GE,F);N=GL(R,E,H);O=GY(N,1);P=GH(I);T=W(P,O);V=GZ(X,GX,GQ);Y=GU(GJ,I);a=GM(V,Y);b=GR(T,a);A=GJ(B,b);c=GE(A);d=Q(c,B);e=M(d);f=K(A);g=GK(f,(-1,-1));h=S(A);i=GK(h,(1,1));j=U(A);k=GK(j,(-1,1));l=L(A);m=GK(l,(1,-1));n=GG(g,i);o=GG(k,m);p=GG(n,o);q=GJ(B,e);r=G(p,q);s=HG(B,2,r);return[*map(list,s)]
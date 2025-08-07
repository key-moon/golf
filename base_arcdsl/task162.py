def H(A,B):return type(B)(A(B)for B in B)
def M(A):return type(A)(B for A in A for B in A)
def G(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return tuple(map(min,zip(*Z(A))))
def Y(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=S(A);J,K=-F,-G;L=Q(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return Q(frozenset(H),(F,G))
def PS(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Q(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def V(A,B):return M(H(A,B))
def PZ(A,a,b):return lambda x:A(a(x),b(x))
def K(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def R(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def X(A,B):return lambda x:A(x)==B
def W(h,g,f):return lambda x:h(g(f(x)))
def L(a,b):return a,b
def U(A,B):return type(A)(A for A in A if B(A))
def PU(a,b):return a and b
def J(A):return frozenset({A})
def PP(A):return len(A)
def P(a,b):return type(a)(A for A in a if A not in b)
def PJ(b):return not b
def PE(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));A=E(I,0);D=L(0,(0,0));F=J(D);G=Y(F,3);H=Z(G);B=K(Q,H);M=R(P,A);N=W(PP,M,B);C=X(N,0);O=K(PE,(-1,-1));S=W(PJ,C,O);T=PZ(PU,C,S);a=U(A,T);b=V(B,a);c=PS(I,1,b);return[*map(list,c)]
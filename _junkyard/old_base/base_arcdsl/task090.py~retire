def H(A):return type(A)(B for A in A for B in A)
def E(A):return max(A for(A,B)in Z(A))
def U(A):return max(A for(B,A)in Z(A))
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-X(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-J(A)+1
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return min(A for(B,A)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def S(A):
	if len(A)==0:return A
	return PS(A,(-J(A),-X(A)))
def PZ(A):return Q(A),R(A)
def P(A,B):
	C=set();K=S(B);D,E=len(A),len(A[0]);L,M=PZ(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in PS(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def K(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PY(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Y(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def V(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def G(A,B):return H(PE(A,B))
def PE(A,B):return type(B)(A(B)for B in B)
def PL(A,a,b):return lambda x:A(a(x),b(x))
def PU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PP(h,g,f):return lambda x:h(g(f(x)))
def M(a,b):return a,b
def L(A,B,C):return tuple(range(A,B,C))
def W(A,B):return max(A,key=B)
def PX(A):return len(A)
def p(I):I=tuple(map(tuple,I));A=L(2,10,1);B=V(M,A,A);C=PU(K,0);D=PU(P,I);E=PU(PU,PS);F=PL(PE,E,D);H=PP(F,Y,C);J=G(H,B);N=W(J,PX);O=PY(I,6,N);return[*map(list,O)]
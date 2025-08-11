def X(A):return max(A for(A,B)in Z(A))
def U(A):return min(A for(A,B)in Z(A))
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):return max(A for(B,A)in Z(A))
def Y(A):return min(A for(B,A)in Z(A))
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-Y(A)+1
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-U(A)+1
def PS(A):return K(A),H(A)
def P(A,B):
	C=set();K=S(B);D,E=len(A),len(A[0]);L,M=PS(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in PJ(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def PX(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def S(A):
	if len(A)==0:return A
	return PJ(A,(-U(A),-Y(A)))
def PJ(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def M(A,B):return frozenset((A,B)for B in Z(B))
def L(A):return tuple(map(min,zip(*Z(A))))
def Q(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PY(A,B):return type(B)(A(B)for B in B)
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PL(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PZ(h,g,f):return lambda x:h(g(f(x)))
def G(a,b):return a,b
def R(A,B):return B.union(frozenset({A}))
def W(A,B):return type(A)(A for A in A if B(A))
def V(A):return frozenset({A})
def PP(A):return type(A)(B for A in A for B in A)
def J(A,B):return A in B
def PV(b):return not b
def p(I):I=tuple(map(tuple,I));B=Q(I,2);A=M(0,B);C=S(A);D=P(I,A);E=PE(PJ,C);F=PY(E,D);H=G(1,3);K=G(5,1);N=G(2,6);O=V(H);T=R(K,O);U=R(N,T);X=PL(J,U);Y=PZ(PV,X,L);Z=W(F,Y);a=PP(Z);b=M(2,a);c=PX(I,b);return[*map(list,c)]
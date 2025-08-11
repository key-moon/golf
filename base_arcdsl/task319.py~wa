def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def G(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def M(A):return tuple(map(max,zip(*S(A))))
def PE(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def L(A):return max(A for(A,B)in S(A))
def E(A):return min(A for(A,B)in S(A))
def X(A):return max(A for(B,A)in S(A))
def V(A):return min(A for(B,A)in S(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return X(A)-V(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-E(A)+1
def PM(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def Y(A):return tuple(map(min,zip(*S(A))))
def PU(A):return PP(A),PS(A)
def Q(A,B):return PM(B,Y(A),PU(A))
def R(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=Y(A);J,K=-F,-G;L=PE(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return PE(frozenset(H),(F,G))
def W(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Y(A)[1]+M(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def Z(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in G(A)-{U(A)})
def J(A):
	if len(A)==0:return A
	return PE(A,(-E(A),-V(A)))
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PJ(h,g,f):return lambda x:h(g(f(x)))
def K(A,B):return lambda x:A(B(x))
def PZ(A,B):return type(B)(B for B in B if B!=A)
def PW(A):return max(enumerate(A))[1]
def H(A,B):return max(A,key=B)
def PV(A):return len(A)
def PX(A,B):return tuple(sorted(A,key=B))
def P(a,b):return a&b
def p(I):I=tuple(map(tuple,I));A=W(I);D=Z(A);B=PX(D,PV);C=PW(B);E=PZ(C,B);F=K(S,J);G=PY(R,2);L=PJ(S,G,J);M=F(C);N=PY(P,M);O=PJ(PV,N,L);T=H(E,O);U=Q(T,A);V=W(U);return[*map(list,V)]
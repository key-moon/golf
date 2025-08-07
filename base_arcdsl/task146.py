def Y(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return tuple(map(min,zip(*P(A))))
def M(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def L(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(M(A,(B*C+C*E,0),(B,D))for C in range(n))
def E(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Z(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def W(A,a,b):return lambda x:A(a(x),b(x))
def U(A,B):return lambda x:A(B(x))
def X(A,B):return next(A for A in A if B(A))
def J(a,b):return a==b
def V(b):return not b
def S(x):return x
def p(I):I=tuple(map(tuple,I));A=L(I,3);B=W(J,E,S);C=U(V,B);D=X(A,C);return[*map(list,D)]
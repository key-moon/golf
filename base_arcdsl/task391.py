def R(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):return tuple(map(min,zip(*Z(A))))
def X(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=S(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def J(A):B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);C=tuple(A for(A,B)in enumerate(X(A))if len(set(B))==1);return tuple(tuple(B for(A,B)in enumerate(D)if A not in C)for(A,D)in enumerate(A)if A not in B)
def Y(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def L(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def H(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def G(A,B):return type(B)(A(B)for B in B)
def W(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def Q(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def U(A,B):return lambda x:A(B(x))
def E(a,b):return a,b
def M(A):return type(A)(B for A in A for B in A)
def K(A,B):return tuple(sorted(A,key=B))
def V(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def p(I):I=tuple(map(tuple,I));A=J(I);B=E(3,1);C=L(A);D=W(P,A);F=U(V,D);N=K(C,F);O=Q(Y,(1,1));R=G(O,N);S=M(R);T=H(S,(1,0),B);return[*map(list,T)]
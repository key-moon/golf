def S(A):return tuple(map(max,zip(*P(A))))
def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):return tuple(map(min,zip(*P(A))))
def U(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Z(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def X(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Z(A)[1]+S(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def L(A,a,b):return tuple(tuple(A if A!=a and A!=b else{a:b,b:a}[A]for A in A)for A in A)
def E(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return X(U(X(A)))
def Y(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def M(A,B):return type(B)(A(B)for B in B)
def V(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def W(A,B):return tuple(sorted(A,key=B))
def J(x):return x
def p(I):I=tuple(map(tuple,I));A=Y(I);B=V(W,J);C=L(A,1,2);D=M(B,C);F=L(D,1,2);G=E(F);return[*map(list,G)]
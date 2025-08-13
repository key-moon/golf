def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def S(A):return tuple(map(max,zip(*P(A))))
def Z(A):return tuple(map(min,zip(*P(A))))
def E(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=Z(A)[1]+S(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def L(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def U(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return E(J(E(A)))
def J(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Z(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def Y(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def M(A,B):return type(B)(A(B)for B in B)
def V(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def Q(a,b):return tuple(zip(a,b))
def X(A):return max(A,default=0)
def p(I):I=tuple(map(tuple,I));A=L(I,4,0);D=J(A);E=Y(Q,A,D);B=V(M,X);C=M(B,E);F=U(C);G=Y(Q,C,F);H=M(B,G);K=U(H);return[*map(list,K)]
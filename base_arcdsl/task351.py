def X(A):return tuple(map(max,zip(*P(A))))
def L(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=U(A)[1]+X(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def J(A):return max(A for(A,B)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def S(A):return max(A for(B,A)in P(A))
def E(A):return min(A for(B,A)in P(A))
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return S(A)-E(A)+1
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-Z(A)+1
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def PE(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def U(A):return tuple(map(min,zip(*P(A))))
def PP(A):return R(A),H(A)
def W(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def Y(A,B):return PE(B,U(A),PP(A))
def M(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return L(Q(L(A)))
def Q(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=U(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def V(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def K(A,a,b):return tuple(A(B,C)for(B,C)in zip(a,b))
def PJ(A,B):return type(B)(A(B)for B in B)
def PS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PU(a,b):return tuple(zip(a,b))
def G(A):return max(A,default=0)
def p(I):I=tuple(map(tuple,I));D=V(I,3);A=W(I,3,0);E=Q(A);F=K(PU,A,E);B=PS(PJ,G);C=PJ(B,F);H=M(C);J=K(PU,C,H);L=PJ(B,J);N=Y(D,L);return[*map(list,N)]
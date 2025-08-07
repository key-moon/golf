def J(A):return max(A for(A,B)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def H(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):return tuple(map(max,zip(*P(A))))
def U(A):return tuple(map(min,zip(*P(A))))
def PP(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def G(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def K(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(PP(A,(0,B*C+C*E),(D,B))for C in range(n))
def M(a,b):return a+b
def V(a,b):return tuple(A+B for(A,B)in zip(a,b))
def L(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=U(A)[1]+E(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def Y(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-Z(A)+1
def W(a,b):return a,b
def PZ(A):return max(enumerate(A))[1]
def R(A):return next(iter(A))
def S(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def X(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));C=Y(I,5);D=Y(I,8);E=Q(C);F=S(E);H=Q(D);A=X(F,H);J=W(1,A);N=G(8,J);O=X(6,A);P=W(1,O);T=G(0,P);U=V(N,T);B=K(U,2);Z=R(B);a=PZ(B);b=L(a);c=M(Z,b);d=W(1,3);e=G(0,d);f=M(c,e);return[*map(list,f)]
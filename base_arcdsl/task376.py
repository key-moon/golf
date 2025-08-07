def J(A):return max(A for(A,B)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def P(A):return max(A for(B,A)in Z(A))
def L(A):return min(A for(B,A)in Z(A))
def K(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return tuple(map(max,zip(*Z(A))))
def E(A):return tuple(map(min,zip(*Z(A))))
def Y(a,b):return a+b
def V(A):
	if isinstance(A,tuple):return A[::-1]
	B=E(A)[0]+X(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def R(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-L(A)+1
def W(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-S(A)+1
def M(a,b):return a,b
def U(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def Q(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def p(I):I=tuple(map(tuple,I));D=W(I);A=G(I);B=U(D);E=M(B,A);F=R(I,(0,0),E);H=V(F);C=Y(I,H);J=Q(B);K=M(J,A);L=R(C,(1,0),K);N=Y(C,L);return[*map(list,N)]
def X(A):return max(A for(A,B)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def E(A):return max(A for(B,A)in Z(A))
def Y(A):return min(A for(B,A)in Z(A))
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-Y(A)+1
def PP(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-J(A)+1
def R(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return tuple(map(min,zip(*Z(A))))
def PX(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PZ(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(PX(A,(0,B*C+C*E),(D,B))for C in range(n))
def K(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=L(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def S(A):return len(R(A))
def W(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def V(A):return PP(A)>PS(A)
def PE(A,B):return type(B)(A(B)for B in B)
def PU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def G(A,B):return lambda x:A(x)==B
def H(A,a,b):return a if A else b
def Q(A,B):return next(A for A in A if B(A))
def U(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def P(A):return min(set(A),key=A.count)
def M(x):return x
def p(I):I=tuple(map(tuple,I));D=S(I);X=K(I);E=V(I);A=H(E,K,M);F=A(I);J=U(D);B=PZ(F,J);C=PU(W,0);L=PE(C,B);N=P(L);O=G(C,N);R=Q(B,O);T=A(R);return[*map(list,T)]
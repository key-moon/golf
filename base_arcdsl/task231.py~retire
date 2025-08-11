def E(A):return max(A for(A,B)in Z(A))
def U(A):return max(A for(B,A)in Z(A))
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return min(A for(B,A)in Z(A))
def J(A):return min(A for(A,B)in Z(A))
def S(A):
	if len(A)==0:return A
	return PS(A,(-J(A),-L(A)))
def PS(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def V(A):
	B=S(A);C=H(B)
	for D in range(1,C):
		E=PS(B,(0,-D));F=frozenset({(B,(C,A))for(B,(C,A))in E if A>=0})
		if F.issubset(B):return D
	return C
def K(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PZ(A):return tuple(A for A in zip(*A[::-1]))
def Y(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def PU(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def X(A):return tuple(map(min,zip(*Z(A))))
def H(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return U(A)-L(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-J(A)+1
def M(a,b):return a,b
def P(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PP(A):return type(A)(B for A in A for B in A)
def R(A,B):return tuple(A for B in range(B))
def G(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def W(a,b):
	if isinstance(a,int)and isinstance(b,int):return a//b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]//b[0],a[1]//b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a//b[0],a//b[1]
	return a[0]//b,a[1]//b
def p(I):I=tuple(map(tuple,I));E=H(I);A=Y(I);B=V(A);C=Q(A);F=M(C,B);J=X(A);L=PU(I,J,F);N=PZ(L);D=G(E);O=W(D,B);S=P(O);T=R(N,S);U=PP(T);Z=K(U);a=M(C,D);b=PU(Z,(0,0),a);return[*map(list,b)]
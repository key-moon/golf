def R(A):return type(A)(B for A in A for B in A)
def J(A):return max(A for(A,B)in P(A))
def Z(A):return min(A for(A,B)in P(A))
def S(A):return max(A for(B,A)in P(A))
def U(A):return min(A for(B,A)in P(A))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return S(A)-U(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return J(A)-Z(A)+1
def PP(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PE(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def H(A):return K(A)==len(A)and Q(A)==1
def PZ(A):return Q(A)==len(A)and K(A)==1
def V(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def E(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PU(A,a,b):return lambda x:A(a(x),b(x))
def PS(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def W(A,B):return lambda x:A(B(x))
def M(A,B):return R(X(A,B))
def X(A,B):return type(A)(A for A in A if B(A))
def G(a,b):return a or b
def PJ(A):return len(A)
def L(a,b):return a>b
def p(I):I=tuple(map(tuple,I));A=V(I,8);B=E(Y,A,A);C=PS(L,1);D=W(C,PJ);F=X(B,D);J=PU(G,PZ,H);K=M(F,J);N=PE(I,3,K);O=PE(N,8,A);return[*map(list,O)]
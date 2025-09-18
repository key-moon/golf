def L(A,B):return type(A)(A for A in A if B(A))
def R(A):return type(A)(B for A in A for B in A)
def E(A):return max(A for(A,B)in P(A))
def S(A):return min(A for(A,B)in P(A))
def J(A):return max(A for(B,A)in P(A))
def X(A):return min(A for(B,A)in P(A))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return E(A)-S(A)+1
def PZ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def V(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def U(A,B,C):
	G,H=len(A),len(A[0]);I=Z(A);D=list(list(A)for A in A)
	for(E,F)in P(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PP(A):return K(A)==len(A)and Q(A)==1
def PS(A):return Q(A)==len(A)and K(A)==1
def M(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def PJ(A,B):return type(B)(A(B)for B in B)
def PU(A,a,b):return lambda x:A(a(x),b(x))
def Y(a,b):return frozenset((B,A)for A in b for B in a)
def PE(A):return max(enumerate(A))[1]
def H(A):return next(iter(A))
def W(A,B):return R(L(A,B))
def G(a,b):return a or b
def p(I):I=tuple(map(tuple,I));A=M(I,8);B=Y(A,A);C=PU(V,H,PE);D=PJ(C,B);E=PU(G,PS,PP);F=W(D,E);J=U(I,8,F);return[*map(list,J)]
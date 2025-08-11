def U(A):return max(A for(A,B)in Z(A))
def J(A):return max(A for(B,A)in Z(A))
def X(A):return min(A for(B,A)in Z(A))
def S(A):return min(A for(A,B)in Z(A))
def K(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return J(A)-X(A)+1
def Q(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return U(A)-S(A)+1
def G(A):return S(A)+Q(A)//2,X(A)+K(A)//2
def L(A):
	if len(A)==0:return frozenset({})
	B=Z(A);C,D=E(B);F,G=Y(A);return frozenset((A,B)for A in range(C,F+1)for B in range(D,G+1))
def H(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(max,zip(*Z(A))))
def E(A):return tuple(map(min,zip(*Z(A))))
def M(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PZ(A,B):return M(A,(A[0]+42*B[0],A[1]+42*B[1]))
def PJ(A):
	if len(A)==0:return A
	G,H=E(A);I,J=Y(A);B,C=min(G,I),min(H,J);D,F=max(G,I),max(H,J);K={(A,C)for A in range(B,D+1)}|{(A,F)for A in range(B,D+1)};L={(B,A)for A in range(C,F+1)}|{(D,A)for A in range(C,F+1)};return frozenset(K|L)
def PP(B):
	if len(B)==0:return frozenset({})
	return L(B)-Z(B)
def V(a,b):
	A,B=G(Z(a));C,D=G(Z(b))
	if A==C:return 0,1 if B<D else-1
	elif B==D:return 1 if A<C else-1,0
	elif A<C:return 1,1 if B<D else-1
	elif A>C:return-1,1 if B<D else-1
def PS(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def W(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def R(A):return next(iter(A))
def P(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));A=W(I,5);D=PP(A);E=PS(I,8,D);B=PJ(A);C=P(B,A);F=V(B,C);G=R(C);H=PZ(G,F);J=PS(E,8,H);return[*map(list,J)]
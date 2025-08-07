def M(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Q(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def X(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Z(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def Y(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def V(h,g,f):return lambda x:h(g(f(x)))
def E(A,B):return lambda x:A(B(x))
def L(A,B):return type(A)(A for A in A if B(A))
def W(A):return len(A)
def U(a,b):return a>b
def P(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));B=Z(I);A=X(I,B);C=Y(P,A);D=Y(U,2);F=V(D,W,C);G=E(F,S);H=L(A,G);J=Q(I,0,H);return[*map(list,J)]
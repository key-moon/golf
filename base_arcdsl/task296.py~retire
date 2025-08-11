def M(A,B):return type(B)(A(B)for B in B)
def Y(A):return type(A)(B for A in A for B in A)
def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def G(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def Q(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def U(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def E(A,B):return Y(M(A,B))
def V(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def J(a,b):return a,b
def L(j):return 0,j
def S(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=P(I);B=Q(I,(0,0),(3,3));C=Q(I,(2,0),(3,3));D=L(4);F=Q(I,D,(3,3));H=J(2,4);K=Q(I,H,(3,3));M=X(0,(3,3));N=V(U,A);O=J(B,C);R=J(F,K);T=S(O,R);W=E(N,T);Y=G(M,A,W);return[*map(list,Y)]
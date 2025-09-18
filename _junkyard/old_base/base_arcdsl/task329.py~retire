def P(A):return max(A for(B,A)in Z(A))
def J(A):return min(A for(B,A)in Z(A))
def V(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def W(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def S(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def L(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return P(A)-J(A)+1
def E(A,B):return lambda x:A(x)==B
def U(A,B):return lambda x:A(B(x))
def Q(A):return max(enumerate(A))[1]
def X(A,B):return type(A)(A for A in A if B(A))
def M(b):return not b
def Y(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
def p(I):I=tuple(map(tuple,I));A=S(I);B=L(I);C=Y(B);D=E(Q,C);F=U(M,D);G=X(A,F);H=W(I,0,G);return[*map(list,H)]
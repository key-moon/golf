def Q(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A):return tuple(map(max,zip(*S(A))))
def U(A):return tuple(map(min,zip(*S(A))))
def L(A):return A[:len(A)//2]
def P(A):return A[len(A)//2+len(A)%2:]
def M(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def W(A):return tuple(A for A in zip(*A[::-1]))
def Z(A):return M(P(W(A)))
def X(A):return M(L(W(A)))
def V(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def J(a,b,A):
	G,H=len(a),len(a[0]);B=tuple()
	for D in range(G):
		C=tuple()
		for E in range(H):F=a[D][E];I=F if F==b[D][E]else A;C=C+(I,)
		B=B+(C,)
	return B
def Y(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=U(A)[1]+E(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def p(I):I=tuple(map(tuple,I));A=Y(I);B=X(A);C=Z(A);D=Y(C);E=J(B,D,0);F=V(E,1,2);return[*map(list,F)]
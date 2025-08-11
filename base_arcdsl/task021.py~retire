def L(A):return max(A for(A,B)in S(A))
def U(A):return min(A for(A,B)in S(A))
def E(A):return max(A for(B,A)in S(A))
def V(A):return min(A for(B,A)in S(A))
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-V(A)+1
def G(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-U(A)+1
def H(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def Y(A):return tuple(map(min,zip(*S(A))))
def Q(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=Y(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def X(A):C,D=len(A),len(A[0]);B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);E=tuple(A for(A,B)in enumerate(Q(A))if len(set(B))==1);F=frozenset({frozenset({(A[B][C],(B,C))for C in range(D)})for B in B});G=frozenset({frozenset({(A[C][B],(C,B))for C in range(C)})for B in E});return F|G
def K(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PP(A):return G(A)==len(A)and R(A)==1
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PZ(A,B):return type(B)(A(B)for B in B)
def W(a,b):return a,b
def M(A,B):return type(A)(A for A in A if B(A))
def Z(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def PS(A):return len(A)
def P(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));C=J(I);A=X(I);B=M(A,PP);D=P(A,B);E=W(D,B);F=PZ(PS,E);G=Z(F);H=K(C,G);return[*map(list,H)]
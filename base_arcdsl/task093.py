def X(A):return max(A for(A,B)in S(A))
def U(A):return min(A for(A,B)in S(A))
def E(A):return max(A for(B,A)in S(A))
def Y(A):return min(A for(B,A)in S(A))
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return E(A)-Y(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return X(A)-U(A)+1
def PL(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return tuple(map(min,zip(*S(A))))
def Q(A):return A[:len(A)//2]
def Z(A):return A[len(A)//2+len(A)%2:]
def PS(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PE(A):return tuple(A for A in zip(*A[::-1]))
def J(A):return PS(Z(PE(A)))
def W(A):return PS(Q(PE(A)))
def R(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def K(a,b):return tuple(A+B for(A,B)in zip(a,b))
def H(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=L(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def G(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def V(A):return PZ(A)>PU(A)
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PV(A,B):return type(B)(A(B)for B in B)
def PY(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,a,b):return a if A else b
def PX(A,B):return tuple(sorted(A,key=B))
def PJ(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def M(x):return x
def p(I):I=tuple(map(tuple,I));C=P(I);D=R(I,C,5);E=G(I,5);F=V(E);A=PP(F,M,H);B=A(D);L=W(B);N=J(B);O=PY(PX,M);Q=PY(PX,PJ);S=PV(O,L);T=PV(Q,N);U=K(S,T);X=A(U);return[*map(list,X)]
def Y(A,B):return type(B)(A(B)for B in B)
def X(A):return type(A)(B for A in A for B in A)
def Z(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def V(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def U(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(V(A,(B*C+C*E,0),(B,D))for C in range(n))
def J(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(V(A,(0,B*C+C*E),(D,B))for C in range(n))
def P(A):return len(Z(A))
def S(A,B):return X(Y(A,B))
def L(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def E(A,B):return max(A,key=B)
def p(I):I=tuple(map(tuple,I));A=U(I,2);B=L(J,2);C=S(B,A);D=E(C,P);return[*map(list,D)]
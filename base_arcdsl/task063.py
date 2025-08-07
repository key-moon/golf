def L(A):return max(A for(A,B)in Z(A))
def U(A):return min(A for(A,B)in Z(A))
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def Z(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PY(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def S(A):return frozenset((A[0],B)for B in range(30))
def E(A):return frozenset((B,A[1])for B in range(30))
def K(A,n):B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(PY(A,(B*C+C*E,0),(B,D))for C in range(n))
def X(A,B,C):
	G,H=len(A),len(A[0]);I=J(A);D=list(list(A)for A in A)
	for(E,F)in Z(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PZ(A):return tuple(A for A in zip(*A[::-1]))
def P(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def R(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-U(A)+1
def H(A,B):return PP(PX(A,B))
def PX(A,B):return type(B)(A(B)for B in B)
def PU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def W(A,B):return lambda x:A(x)==B
def Q(A,B):return lambda x:A(B(x))
def PL(a,b):return tuple(zip(a,b))
def G(a,b):return a,b
def Y(A,B,C):return tuple(range(A,B,C))
def PV(A):return max(enumerate(A))[1]
def PS(A):return next(iter(A))
def M(A,B):return type(A)(A for A in A if B(A))
def PP(A):return type(A)(B for A in A for B in A)
def V(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));A=R(I);D=PZ(I);F=V(A,2);B=Y(0,A,1);J=PE(P,0);L=W(J,F);N=PE(K,A);O=PU(PX,L);C=Q(O,N);T=C(I);U=PL(B,T);Z=M(U,PV);a=H(S,Z);b=C(D);c=PL(b,B);d=M(c,PS);e=H(E,d);f=G(a,e);g=PP(f);h=X(I,3,g);return[*map(list,h)]
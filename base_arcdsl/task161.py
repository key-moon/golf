def G(A,B):return type(A)(A for A in A if B(A))
def PP(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def L(A):return max(A for(A,B)in J(A))
def E(A):return min(A for(A,B)in J(A))
def X(A):return max(A for(B,A)in J(A))
def V(A):return min(A for(B,A)in J(A))
def PJ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return X(A)-V(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-E(A)+1
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PY(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return tuple(map(max,zip(*J(A))))
def Y(A):return tuple(map(min,zip(*J(A))))
def PR(A):
	if len(A)==0:return A
	F,G=Y(A);H,I=M(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def PX(A,B):return PG(A,U(A),J(B))
def K(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PG(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PL(A):return PJ(A)==len(A)and PZ(A)==1
def PV(A):return PZ(A)==len(A)and PJ(A)==1
def P(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in PP(A)-{U(A)})
def R(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def Q(A,a,b):return frozenset(A(C,B)for B in b for C in a)
def PQ(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PE(h,g,f):return lambda x:h(g(f(x)))
def H(A,B):return PU(G(A,B))
def W(x):return x>0
def PS(a,b):return a or b
def PK(a,b):return a and b
def PU(A):return type(A)(B for A in A for B in A)
def PW(A):return len(A)
def Z(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));A=S(I);B=R(I,A);D=Q(K,B,B);E=P(I);C=PU(E);F=PX(I,C);G=PQ(PS,PL,PV);J=PR(C);L=PM(Z,J);M=PE(W,PW,L);N=PQ(PK,G,M);O=H(D,N);T=PG(F,A,O);return[*map(list,T)]
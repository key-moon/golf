def PG(A,B):return type(B)(A(B)for B in B)
def PE(A):return type(A)(B for A in A for B in A)
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in J(a)for(C,D)in J(b))
def Q(A):return max(A for(A,B)in J(A))
def M(A):return max(A for(B,A)in J(A))
def PV(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(A):return min(A for(B,A)in J(A))
def V(A):return min(A for(A,B)in J(A))
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-G(A)+1
def PZ(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Q(A)-V(A)+1
def PJ(A):return V(A)+PZ(A)//2,G(A)+PU(A)//2
def K(a,b):return W(a,b)==1
def E(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def Y(A,B):
	I,J=PJ(A);L,M=PJ(B);C,D=0,0
	if E(A,B):C=1 if I<L else-1
	else:D=1 if J<M else-1
	F,G=C,D;H=0
	while not K(A,B)and H<42:H+=1;F+=C;G+=D;A=PY(A,(C,D))
	return F-C,G-D
def PP(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PW(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def H(A,B,C,D):
	K=X(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=U(A);S=L if C else Z
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in S(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def PY(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PS(A,B):return PE(PG(A,B))
def PK(A,a,b):return lambda x:A(a(x),b(x))
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PQ(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PX(h,g,f):return lambda x:h(g(f(x)))
def PL(A):return next(iter(A))
def R(x):return x
def p(I):I=tuple(map(tuple,I));C=H(I,True,False,True);D=PP(I,3,0);E=PP(D,7,0);A=PM(P,C);F=PM(PQ,Y);B=PX(F,PL,A);G=B(2);J=B(1);K=A(3);L=A(7);M=PK(PY,R,G);N=PK(PY,R,J);O=PS(M,K);Q=PS(N,L);S=PW(E,O);T=PW(S,Q);return[*map(list,T)]
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|S(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(B,A)in J(A))
def Q(A):return max(A for(A,B)in J(A))
def PY(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in J(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def M(A,B):return Y(A)==0 or G(A)==0 or Q(A)==len(B)-1 or W(A)==len(B[0])-1
def E(a,b):return len(set(A for(B,A)in J(a))&set(A for(B,A)in J(b)))>0
def V(a,b):return len(set(A for(A,B)in J(a))&set(A for(A,B)in J(b)))>0
def G(A):return min(A for(B,A)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def K(A,B,C,D):
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
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PL(A,B):return type(B)(A(B)for B in B)
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PX(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,B):return lambda x:A(B(x))
def PJ(A,B):return type(B)(B for B in B if B!=A)
def H(A,B):return next(A for A in A if B(A))
def R(A,B):return type(A)(A for A in A if B(A))
def PZ(A,B):return min(A,key=B)
def PS(A,B):return max(A,key=B)
def PV(b):return not b
def p(I):L=False;I=tuple(map(tuple,I));N=K(I,True,L,L);O=P(N,0);B=PL(J,O);Q=PX(M,I);S=PP(PV,Q);A=H(B,S);C=PJ(A,B);T=PE(E,A);U=PE(V,A);D=R(C,T);F=R(C,U);W=PZ(D,Y);X=PS(D,Y);Z=PZ(F,G);a=PS(F,G);b=PY(I,6,A);c=PY(b,2,W);d=PY(c,1,X);e=PY(d,4,Z);f=PY(e,3,a);return[*map(list,f)]
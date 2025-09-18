def PP(A):return type(A)(B for A in A for B in A)
def PJ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def Y(A):return S(A)|U(A)
def X(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def PE(A,B,C):
	H,I=len(A),len(A[0]);D=list(list(A)for A in A)
	for(F,G)in E(C):
		if 0<=F<H and 0<=G<I:D[F][G]=B
	return tuple(tuple(A)for A in D)
def W(A,B):D,F=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in E(A)if 0<=A<D and 0<=C<F)
def M(a,b):return V(a,b)==1
def V(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in E(a)for(C,D)in E(b))
def G(A,B,C,D):
	K=L(A)if D else None;M=set();G=set();P,Q=len(A),len(A[0]);R=X(A);T=Y if C else S
	for E in R:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		N={(H,E)};I={E}
		while len(I)>0:
			O=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:N.add((J,F));G.add(F);O|={(A,B)for(A,B)in T(F)if 0<=A<P and 0<=B<Q}
			I=O-G
		M.add(frozenset(N))
	return frozenset(M)
def S(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def R(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def L(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PU(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PZ(h,g,f):return lambda x:h(g(f(x)))
def PS(A):return next(iter(A))
def H(A,B):return PP(K(A,B))
def K(A,B):return type(A)(A for A in A if B(A))
def Q(A):return frozenset({A})
def Z(a,b):return type(a)(A for A in a if A not in b)
def PX(n):return n%2==0
def p(I):N=False;I=tuple(map(tuple,I));A=J(I);O=G(I,True,N,N);B=R(I,A);T=PS(B);U=S(T);X=W(U,I);C=L(X);Y=R(I,C);a=P(O,0);b=PU(M,Y);c=H(a,b);D=E(c);d=PU(V,B);e=PZ(PX,d,Q);F=K(D,e);f=Z(D,F);g=PE(I,A,F);h=PE(g,C,f);return[*map(list,h)]
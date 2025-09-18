def R(A,B):return lambda x:A(B(x))
def J(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def L(A):return Z(A)|J(A)
def Z(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def E(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def X(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PX(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def U(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def V(A):return max(A for(B,A)in U(A))
def W(A):return min(A for(B,A)in U(A))
def M(A):return max(A for(A,B)in U(A))
def Y(A):return min(A for(A,B)in U(A))
def PJ(A):F,G=Y(A)-1,W(A)-1;H,I=M(A)+1,V(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def H(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PV(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in U(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def K(A,B,C,D):
	M=X(A)if D else None;N=set();H=set();Q,R=len(A),len(A[0]);S=E(A);T=L if C else Z
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};J={F}
		while len(J)>0:
			P=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=M:O.add((K,G));H.add(G);P|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=P-H
		N.add(frozenset(O))
	return frozenset(N)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return V(A)-W(A)+1
def S(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def PL(A,n):
	if n==1:return A
	return R(A,PL(A,n-1))
def PE(h,g,f):return lambda x:h(g(f(x)))
def PP(A,a,b):return a if A else b
def PZ(A,B):return min(A,key=B)
def PS(A,B):return max(A,key=B)
def PY(A):return len(A)
def G(a,b):return a==b
def Q(x):return x
def p(I):E=False;I=tuple(map(tuple,I));A=S(I);D=K(I,True,E,E);F=P(D,A);B=PS(F,PY);J=PZ(D,PU);L=PY(J);M=G(L,1);N=PP(M,Q,PJ);C=PE(PJ,PJ,N);O=PL(C,2);R=PL(C,3);T=C(B);U=O(B);V=R(B);W=PV(I,A,T);X=PV(W,A,U);Y=PV(X,A,V);Z=H(Y,0,5);return[*map(list,Z)]
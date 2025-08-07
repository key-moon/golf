def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return tuple(map(max,zip(*S(A))))
def PU(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def X(A):return tuple(map(min,zip(*S(A))))
def H(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def PP(A,n):D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(PY(A,(0,B*C+C*E),(D,B))for C in range(n))
def G(a,b):return a+b
def Q(a,b):return tuple(A+B for(A,B)in zip(a,b))
def R(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=X(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def W(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=X(A)[1]+Y(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def PS(A):return next(iter(A))[0]
def L(A):return min(A for(B,A)in S(A))
def M(A,B,C,D):
	M=U(A)if D else None;N=set();H=set();R,S=len(A),len(A[0]);T=J(A);V=E if C else P
	for F in T:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==M:continue
		O={(I,F)};K={F}
		while len(K)>0:
			Q=set()
			for G in K:
				L=A[G[0]][G[1]]
				if I==L if B else L!=M:O.add((L,G));H.add(G);Q|={(A,B)for(A,B)in V(G)if 0<=A<R and 0<=B<S}
			K=Q-H
		N.add(frozenset(O))
	return frozenset(N)
def PY(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PX(A,B):return type(B)(A(B)for B in B)
def PE(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def K(a,b):return a,b
def PZ(A):return type(A)(B for A in A for B in A)
def PL(A):return len(A)
def PJ(A,B):return tuple(sorted(A,key=B))
def V(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));C=M(I,True,False,True);A=K(1,3);D=PL(C);E=PJ(C,L);F=PX(PS,E);J=PE(H,(1,1));N=PX(J,F);O=PZ(N);P=R(O);S=V(9,D);T=K(1,S);U=H(0,T);X=Q(P,U);Y=PP(X,3);B=PZ(Y);Z=PY(B,(0,0),A);a=PY(B,(1,0),A);b=PY(B,(2,0),A);c=W(a);d=G(Z,c);e=G(d,b);return[*map(list,e)]
def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def X(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def U(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def E(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def W(A):return max(A for(A,B)in J(A))
def Y(A):return min(A for(A,B)in J(A))
def J(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def M(A):return max(A for(B,A)in J(A))
def Q(A):return min(A for(B,A)in J(A))
def PY(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return M(A)-Q(A)+1
def PX(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return W(A)-Y(A)+1
def PL(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def PM(A):return tuple(A for A in zip(*A[::-1]))
def L(A):return PL(S(PM(A)))
def G(A):return PL(PP(PM(A)))
def S(A):return A[len(A)//2+len(A)%2:]
def PP(A):return A[:len(A)//2]
def PQ(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def PU(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def PJ(a,b):return a+b
def PZ(a,b):return tuple(A+B for(A,B)in zip(a,b))
def PW(A):return PY(A)==len(A)and PX(A)==1
def PK(A):return PX(A)==len(A)and PY(A)==1
def K(A,B,C,D):
	L=E(A)if D else None;M=set();H=set();Q,R=len(A),len(A[0]);S=U(A);T=X if C else P
	for F in S:
		if F in H:continue
		I=A[F[0]][F[1]]
		if I==L:continue
		N={(I,F)};J={F}
		while len(J)>0:
			O=set()
			for G in J:
				K=A[G[0]][G[1]]
				if I==K if B else K!=L:N.add((K,G));H.add(G);O|={(A,B)for(A,B)in T(G)if 0<=A<Q and 0<=B<R}
			J=O-H
		M.add(frozenset(N))
	return frozenset(M)
def PV(A):return PX(A),PY(A)
def PG(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PS(A,B):return lambda x:A(B(x))
def PE(A,a,b):return a if A else b
def R(A,B):return type(A)(A for A in A if B(A))
def V(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def PR(A):return len(A)
def H(a,b):return a>b
def p(I):I=tuple(map(tuple,I));E=K(I,True,False,True);F=PG(R,E);C=PS(PR,F);J=C(PK);M=C(PW);A=H(J,M);N=PE(A,G,PP);O=PE(A,L,S);P=PE(A,PZ,PJ);D=N(I);B=O(I);Q=PQ(D,(0,0));T=PV(B);U=V(T);W=PQ(B,U);X=PU(D,3,Q);Y=PU(B,3,W);Z=P(X,Y);return[*map(list,Z)]
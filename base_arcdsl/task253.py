def Z(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def E(A):return P(A)|Z(A)
def P(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def J(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def U(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def Y(A):return max(A for(A,B)in S(A))
def X(A):return min(A for(A,B)in S(A))
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def L(A):return max(A for(B,A)in S(A))
def M(A):return min(A for(B,A)in S(A))
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return L(A)-M(A)+1
def PU(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return Y(A)-X(A)+1
def PW(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def PL(A):return PU(A),PE(A)
def PY(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def R(A,B):return PW(B,V(A),PL(A))
def PJ(a,b):return a+b
def PZ(a,b):return tuple(A+B for(A,B)in zip(a,b))
def K(A,B,C,D):
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
def W(A):return tuple(map(max,zip(*S(A))))
def G(A):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def Q(A):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*S(A)))))
def V(A):return tuple(map(min,zip(*S(A))))
def PV(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def PM(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def PP(A,B):return lambda x:A(x)==B
def PX(h,g,f):return lambda x:h(g(f(x)))
def PS(A,B):return lambda x:A(B(x))
def H(A,B):return next(A for A in A if B(A))
def p(I):I=tuple(map(tuple,I));B=K(I,True,False,True);C=PV(PY,I);D=PP(C,0);E=PV(H,B);F=PM(R,I);J=PV(PS,D);A=PX(F,E,J);L=A(V);M=A(Q);N=A(G);O=A(W);P=PZ(O,N);S=PZ(M,L);T=PJ(P,S);return[*map(list,T)]
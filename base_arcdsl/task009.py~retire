def K(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def L(A):return max(A for(A,B)in S(A))
def E(A):return min(A for(A,B)in S(A))
def X(A):return max(A for(B,A)in S(A))
def Y(A):return min(A for(B,A)in S(A))
def PE(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return X(A)-Y(A)+1
def PS(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return L(A)-E(A)+1
def PM(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def G(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def PQ(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def ZZ(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def PL(A):return next(iter(A))[0]
def PV(A):return PE(A)==len(A)and PS(A)==1
def PW(A):return PS(A)==len(A)and PE(A)==1
def U(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in K(A))
def M(A,B):return frozenset((A,B)for B in S(B))
def R(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def P(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def J(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def PK(A,B):return type(B)(A(B)for B in B)
def PH(A,a,b):return lambda x:A(a(x),b(x))
def PG(A,n):
	if n==1:return A
	return PP(A,PG(A,n-1))
def PP(A,B):return lambda x:A(B(x))
def Q(a,b):return frozenset((B,A)for A in b for B in a)
def PU(A,B):return type(B)(B for B in B if B!=A)
def ZP(A):return max(enumerate(A))[1]
def PY(A):return next(iter(A))
def H(A,B):return PX(W(A,B))
def W(A,B):return type(A)(A for A in A if B(A))
def PJ(a,b):return a or b
def PZ(A,B):return max(A,key=B)
def PX(A):return type(A)(B for A in A for B in A)
def PR(A):return len(A)
def Z(a,b):return type(a)(A for A in a if A not in b)
def V(a,b):return a==b
def p(I):I=tuple(map(tuple,I));A=U(I);B=J(I);D=R(I,B);E=P(A,0);F=PZ(A,PR);K=Z(A,E);L=PU(F,K);C=PX(L);N=Q(C,C);O=PG(PY,2);S=PP(PY,ZP);T=PH(V,O,S);X=W(N,T);Y=PP(ZP,PY);a=PG(ZP,2);b=PH(G,Y,a);c=PH(M,PL,b);d=PK(c,X);e=PH(PJ,PW,PV);f=H(d,e);g=PQ(I,f);h=ZZ(g,B,D);return[*map(list,h)]
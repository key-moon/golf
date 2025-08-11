def W(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def S(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def P(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def L(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def Z(A,B,C):
	G,H=len(A),len(A[0]);I=P(A);D=list(list(A)for A in A)
	for(E,F)in S(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def U(A):return min(A for(B,A)in S(A))
def J(A):return min(A for(A,B)in S(A))
def V(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def Y(a,b):return a,b
def X(Aa):return min(Aa,default=0)
def M(A):return max(A,default=0)
def E(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=V(I,2);D=V(I,3);A=J(C);H=U(C);K=J(D);B=U(D);F=Y(A,K);N=X(F);O=M(F);P=Y(N,B);Q=Y(O,B);R=L(P,Q);G=Y(H,B);S=X(G);T=M(G);W=Y(A,S);a=Y(A,T);b=L(W,a);c=E(R,b);d=Z(I,8,c);return[*map(list,d)]
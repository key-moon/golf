def p(g):
	A={}
	for O in g:
		for H in O:A[H]=A.get(H,0)+1
	I=sorted(A,key=lambda k:-A[k])[1];D=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==I];J=[A for(A,B)in D];K=[A for(B,A)in D];P,Q=min(J),max(J);R,S=min(K),max(K);E=[(A,B)for(A,B)in D if P<A<Q and R<B<S and g[A][B]!=I];from collections import Counter as T;B=T(g[A][B]for(A,B)in E);U=min(B,key=lambda c:B[c]);L=max(B,key=lambda c:B[c]);C=[(A,B)for(A,B)in E if g[A][B]==U][0]
	def V(dy,dx):return dx,-dy
	for(M,N)in E:
		if g[M][N]==L:
			F,G=M-C[0],N-C[1]
			for W in range(3):F,G=V(F,G);g[C[0]+F][C[1]+G]=L
	return g
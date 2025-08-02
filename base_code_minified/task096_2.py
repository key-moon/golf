def p(g):
	U,V=len(g),len(g[0]);A={}
	for B in g:
		for E in B:A[E]=A.get(E,0)+1
	F=max(A,key=A.get);G=[(A,B)for A in range(U)for B in range(V)if g[A][B]!=F];W=sorted({A for(A,B)in G});X=sorted({A for(B,A)in G})
	def H(a):
		B=[];A=[a[0]]
		for(D,C)in zip(a,a[1:]):
			if C==D+1:A.append(C)
			else:B.append(A);A=[C]
		B.append(A);return B
	C=H(W);D=H(X);I=len(C[0]);J=len(D[0]);K=len(C);L=len(D);Y=K*I+(K-1);Z=L*J+(L-1);B=[[F]*Z for A in range(Y)]
	for(a,M)in enumerate(C):
		for(b,N)in enumerate(D):
			O,P=M[0],M[-1];Q,R=N[0],N[-1];c,d=P-O+1,R-Q+1;e=[g[A][Q:R+1]for A in range(O,P+1)];f=a*(I+1);h=b*(J+1)
			for S in range(c):
				for T in range(d):B[f+S][h+T]=e[S][T]
	return B
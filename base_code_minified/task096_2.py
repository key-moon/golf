def p(A):
	V,W=len(A),len(A[0]);B={}
	for C in A:
		for F in C:B[F]=B.get(F,0)+1
	G=max(B,key=B.get);H=[(B,C)for B in range(V)for C in range(W)if A[B][C]!=G];X=sorted({A for(A,B)in H});Y=sorted({A for(B,A)in H})
	def I(A):
		C=[];B=[A[0]]
		for(E,D)in zip(A,A[1:]):
			if D==E+1:B.append(D)
			else:C.append(B);B=[D]
		C.append(B);return C
	D=I(X);E=I(Y);J=len(D[0]);K=len(E[0]);L=len(D);M=len(E);Z=L*J+(L-1);a=M*K+(M-1);C=[[G]*a for A in range(Z)]
	for(b,N)in enumerate(D):
		for(c,O)in enumerate(E):
			P,Q=N[0],N[-1];R,S=O[0],O[-1];d,e=Q-P+1,S-R+1;f=[A[B][R:S+1]for B in range(P,Q+1)];g=b*(J+1);h=c*(K+1)
			for T in range(d):
				for U in range(e):C[g+T][h+U]=f[T][U]
	return C
def p(A):
	C,D=len(A),len(A[0]);M=[(B,C,A[B][C])for B in range(C)for C in range(D)if A[B][C]];(N,O,G),(P,Q,H)=M;B=D>C;I=sorted([(O,G),(Q,H)])if B else sorted([(N,G),(P,H)]);F,R=I[0];S,T=I[1];J=S-F;E=0
	while F+E*J<(D if B else C):
		K=F+E*J;U=R if E%2<1 else T
		for L in range(C*B+D*(1-B)):A[B*L+(1-B)*K][B*K+(1-B)*L]=U
		E+=1
	return A
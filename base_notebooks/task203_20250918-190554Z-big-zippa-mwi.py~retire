def p(g,L=len,R=range):
	B=L(g);C=L(g[0]);A=g[B//2][:C//2];A={A[B]:A[-(B+1)]for B in R(L(A))}
	for D in R(B):
		for E in R(C):g[D][E]=A[g[D][E]]
	return g
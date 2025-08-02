def p(g):
	N,O=len(g),len(g[0]);A={}
	for R in g:
		for D in R:
			if D:A[D]=A.get(D,0)+1
	P=max(A,key=A.get);S=N*O;G=H=A=I=J=E=K=F=S;H=I=E=F=-1
	for B in range(N):
		for C in range(O):
			D=g[B][C]
			if D==P:G,H,A,I=min(G,B),max(H,B),min(A,C),max(I,C)
			elif D:J,E,K,F=min(J,B),max(E,B),min(K,C),max(F,C)
	L,M=E-J+1,F-K+1;T=(H-G)//(L-1)if L>1 else 0;U=(I-A)//(M-1)if M>1 else 0;Q=[A[K:F+1]for A in g[J:E+1]]
	for B in range(L):
		for C in range(M):
			if g[G+T*B][A+U*C]!=P:Q[B][C]=0
	return Q
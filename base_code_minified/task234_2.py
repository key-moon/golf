def p(g):
	L={A for B in g for A in B if A};E=[]
	for B in L:F=[A for(A,C)in enumerate(g)for(E,D)in enumerate(C)if D==B];G=[C for(E,A)in enumerate(g)for(C,D)in enumerate(A)if D==B];E.append((B,min(F),max(F),min(G),max(G)))
	M,N=sorted(E,key=lambda t:t[4]-t[3]-(t[2]-t[1]),reverse=True);O,H,A,I,J=M;P,S,T,K,U=N
	for C in range(H,A+1):
		for D in range(I,J+1):g[C][D]=O
	Q,R=A-H+1,J-I+1
	for C in range(A+1,A+1+Q):
		for D in range(K,K+R):g[C][D]=P
	return g
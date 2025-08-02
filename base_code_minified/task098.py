def p(A):
	E={}
	for(B,J)in enumerate(A):
		for(C,D)in enumerate(J):
			if D:F,G,H,I=E.get(D,(B,B,C,C));E[D]=min(F,B),max(G,B),min(H,C),max(I,C)
	for(D,(F,G,H,I))in E.items():
		for B in range(F+1,G):
			for C in range(H+1,I):
				if A[B][C]==D:A[B][C]=0
	return A
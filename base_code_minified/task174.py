def p(g):
	D={}
	for(B,H)in enumerate(g):
		for(C,E)in enumerate(H):
			if E:
				A=D.get(E)
				if A:A[:4]=[min(A[0],B),min(A[1],C),max(A[2],B),max(A[3],C)];A[4]+=1
				else:D[E]=[B,C,B,C,1]
	for(F,G)in D.items():
		if G[4]==F:I,J,K,L,M=G;break
	return[[F if g[A][B]==F else 0 for B in range(J,L+1)]for A in range(I,K+1)]
def p(A):
	G,H=len(A),len(A[0]);I=min(A for B in A for A in B if A not in(0,2,8));D,E=next((B,C)for B in range(G)for C in range(H)if A[B][C]==I);F=[(D,E)]
	while F:
		D,E=F.pop()
		for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
			B,C=D+J,E+K
			if 0<=B<G and 0<=C<H and A[B][C]==0:A[B][C]=I;F.append((B,C))
	return A
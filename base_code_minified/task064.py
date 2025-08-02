def p(A):
	L={}
	for(D,G)in enumerate(A):
		for(C,E)in enumerate(G):
			B=L.get(E)
			if B:B[0]+=1;B[1]=min(B[1],D);B[2]=max(B[2],D);B[3]=min(B[3],C);B[4]=max(B[4],C)
			else:L[E]=[1,D,D,C,C]
	M=N=0
	for(E,(O,H,I,J,K))in L.items():
		B=(I-H+1)*(K-J+1)
		if O==B>1 and B>N:N=B;M=E
	if N:
		H,I,J,K=L[M][1:]
		for(D,G)in enumerate(A):
			for(C,E)in enumerate(G):
				if E!=M:
					if H<=D<=I:
						if C<J:
							for F in range(C+1,J):G[F]=E
						elif C>K:
							for F in range(K+1,C):G[F]=E
					if J<=C<=K:
						if D<H:
							for F in range(D+1,H):A[F][C]=E
						elif D>I:
							for F in range(I+1,D):A[F][C]=E
	return A
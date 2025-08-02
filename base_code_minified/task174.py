def p(A):
	E={}
	for(C,I)in enumerate(A):
		for(D,F)in enumerate(I):
			if F:
				B=E.get(F)
				if B:B[:4]=[min(B[0],C),min(B[1],D),max(B[2],C),max(B[3],D)];B[4]+=1
				else:E[F]=[C,D,C,D,1]
	for(G,H)in E.items():
		if H[4]==G:J,K,L,M,N=H;break
	return[[G if A[B][C]==G else 0 for C in range(K,M+1)]for B in range(J,L+1)]
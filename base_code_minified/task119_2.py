def p(A):
	I=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==8];(D,E),(F,G)=I;J,K=(F-D)//abs(F-D),(G-E)//abs(G-E)
	for(L,M)in((D,E),(F,G)):
		for H in(1,-1):
			B,C=L,M
			while 1:
				B+=H*J;C+=H*K
				if A[B][C]==2:break
				if A[B][C]==0:A[B][C]=3
	return A
def p(A):
	G,H=len(A),len(A[0]);P=[(B,D,A)for(B,C)in enumerate(A)for(D,A)in enumerate(C)if A];(J,K,L),(I,M,F)=P;N,O=abs(I-J),abs(M-K);E=[[0]*H for A in range(G)]
	if O<=N:
		C=O*2
		for B in range(G):
			for D in range(H):
				if(D-K)%C==0:E[B][D]=L
				if(D-M)%C==0:E[B][D]=F
	else:
		C=N*2
		for B in range(G):
			for D in range(H):
				if(B-J)%C==0:E[B][D]=L
				if(B-I)%C==C-F%C:E[B][D]=F
				if(B-I)%C==0:E[B][D]=F
	return E
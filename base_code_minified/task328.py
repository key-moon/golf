def p(A):
	B,C=len(A),len(A[0]);G=[(B,D,A[B][D])for B in range(B)for D in range(C)if A[B][D]];H=[[0]*C for A in range(B)]
	for D in range(B):
		for E in range(C):
			F=[abs(D-A)+abs(E-B)for(A,B,C)in G];I=min(F)
			if F.count(I)==1:
				J,K,L=G[F.index(I)]
				if max(abs(D-J),abs(E-K))%2<1:H[D][E]=L
	return H
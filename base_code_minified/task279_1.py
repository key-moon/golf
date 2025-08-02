def p(A):
	H=len(A);I=len(A[0]);D=[[0]*I for A in range(H)];J=[]
	for E in range(H):
		for F in range(I):
			if A[E][F]==1 and not D[E][F]:
				G=[(E,F)];D[E][F]=1
				for(K,L)in G:
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						B=K+M;C=L+N
						if 0<=B<H and 0<=C<I and A[B][C]==1 and not D[B][C]:D[B][C]=1;G.append((B,C))
				if len(G)>len(J):J=G
	for(K,L)in J:A[K][L]=8
	return A
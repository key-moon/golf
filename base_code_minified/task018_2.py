def p(A):
	K,D=len(A),len(A[0]);N=[[0]*D for A in A];E=[[0]*D for A in A]
	for F in range(K):
		for G in range(D):
			if A[F][G]and not E[F][G]:
				H=[(F,G)];E[F][G]=1
				for S in H:
					I,J=S
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=I+L,J+M
						if 0<=B<K and 0<=C<D and A[B][C]and not E[B][C]:E[B][C]=1;H.append((B,C))
				O,P=zip(*H);Q,R=(min(O)+max(O))//2,(min(P)+max(P))//2
				for(I,J)in H:L,M=I-Q,J-R;N[K-1-Q-M][R+L]=A[I][J]
	return N
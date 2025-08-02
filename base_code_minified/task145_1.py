def p(A):
	D,E=len(A),len(A[0]);N=[(1,0),(-1,0),(0,1),(0,-1)]
	for F in range(D):
		for G in range(E):
			if A[F][G]==2:
				H=[B for B in N if 0<=F+B[0]<D and 0<=G+B[1]<E and A[F+B[0]][G+B[1]]==2]
				for O in range(len(H)):
					for R in range(O+1,len(H)):
						B,C=H[O],H[R]
						if B[0]*C[0]+B[1]*C[1]==0:
							for(P,Q)in[((-B[0]-C[0],-B[1]-C[1]),1),((B[0]+C[0],B[1]+C[1]),8)]:
								I,J=F+P[0],G+P[1]
								if 0<=I<D and 0<=J<E and A[I][J]==0:
									M=[(I,J)];A[I][J]=Q
									while M:
										S,T=M.pop()
										for(U,V)in N:
											K,L=S+U,T+V
											if 0<=K<D and 0<=L<E and A[K][L]==0:A[K][L]=Q;M.append((K,L))
	return A
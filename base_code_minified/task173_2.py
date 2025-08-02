def p(A):
	I,J=len(A),len(A[0]);F,K={},{}
	for C in range(I):
		for D in range(J):
			B=A[C][D]
			if B and B not in F:
				E=[]
				for(G,H)in((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
					L,M=C+G,D+H
					if 0<=L<I and 0<=M<J and A[L][M]:E.append((G,H))
				if len(E)>1:F[B]=E;K[B]=A[C+E[0][0]][D+E[0][1]]
	for C in range(I):
		for D in range(J):
			B=A[C][D]
			if B in F:
				for(G,H)in F[B]:A[C+G][D+H]=K[B]
	return A
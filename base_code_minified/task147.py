def p(A):
	I,J=len(A),len(A[0])
	for E in range(I):
		for F in range(J):
			if A[E][F]==3:
				B=[(E,F)];A[E][F]=0
				for(G,H)in B:
					for(K,L)in((1,0),(-1,0),(0,1),(0,-1)):
						C=G+K;D=H+L
						if 0<=C<I and 0<=D<J and A[C][D]==3:B.append((C,D));A[C][D]=0
				for(G,H)in B:A[G][H]=8 if len(B)>2 else 3
	return A
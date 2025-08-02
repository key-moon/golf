def p(A):
	D=[A[:]for A in A];E,F=len(D),len(D[0])
	for H in range(E):
		for I in range(F):
			if D[H][I]==2:
				for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
					B,C=I+J,H+K
					if 0<=B<F and 0<=C<E:
						G=D[C][B]
						if G and G-2:
							while 0<=B<F and 0<=C<E and D[C][B]==G:A[C][B]=4;B+=J;C+=K
	return A
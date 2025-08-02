def p(val_g):
	D=val_g;C=[A[:]for A in D];E,F=len(C),len(C[0])
	for H in range(E):
		for I in range(F):
			if C[H][I]==2:
				for(J,K)in((1,0),(-1,0),(0,1),(0,-1)):
					A,B=I+J,H+K
					if 0<=A<F and 0<=B<E:
						G=C[B][A]
						if G and G-2:
							while 0<=A<F and 0<=B<E and C[B][A]==G:D[B][A]=4;A+=J;B+=K
	return D
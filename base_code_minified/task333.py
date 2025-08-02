def p(A):
	for(G,D)in enumerate(A):
		if 3 in D:H=D.index(3);break
	I=G+1;J=H+1
	for(F,D)in enumerate(A):
		for(B,E)in enumerate(D):
			if E and E-3:
				if G<=F<=I:
					if B<H:
						for C in range(B,H):D[C]=E
					elif B>J:
						for C in range(J+1,B+1):D[C]=E
				elif H<=B<=J:
					if F<G:
						for C in range(F,G):A[C][B]=E
					elif F>I:
						for C in range(I+1,F+1):A[C][B]=E
	return A
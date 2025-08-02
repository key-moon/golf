def p(val_g):
	C=val_g;H,I=len(C),len(C[0])
	for K in range(H):
		for L in range(I):
			J=C[K][L]
			if J:
				D,E,F,G=H,0,I,0
				for A in range(H):
					for B in range(I):
						if C[A][B]==J:
							if A<D:D=A
							if A>E:E=A
							if B<F:F=B
							if B>G:G=B
				if E-D>1 and G-F>1:
					for A in range(D+1,E):
						for B in range(F+1,G):
							if C[A][B]==0:C[A][B]=8
	return C
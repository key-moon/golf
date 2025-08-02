def p(A):
	for(B,F)in enumerate(A):
		for(C,G)in enumerate(F):
			if G==2:
				for D in A[max(B-1,0):B+2]:
					for E in range(max(C-1,0),C+2):
						if not D[E]:D[E]=1
	return A
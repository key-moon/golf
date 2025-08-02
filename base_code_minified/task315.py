def p(val_g):
	B=val_g;A=len(B);D=max(max(A)for A in B);C=[[0]*A*A for B in range(A*A)]
	for(E,F)in enumerate(B):
		for(G,H)in enumerate(F):
			if H==D==2:
				for(I,J)in enumerate(B):
					for(K,L)in enumerate(J):C[E*A+I][G*A+K]=L
	return C
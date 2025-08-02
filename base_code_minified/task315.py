def p(A):
	B=len(A);D=max(max(A)for A in A);C=[[0]*B*B for A in range(B*B)]
	for(E,F)in enumerate(A):
		for(G,H)in enumerate(F):
			if H==D==2:
				for(I,J)in enumerate(A):
					for(K,L)in enumerate(J):C[E*B+I][G*B+K]=L
	return C
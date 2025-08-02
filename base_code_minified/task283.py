def p(A):
	for(G,D)in enumerate(A):
		for(E,H)in enumerate(D):
			if H==5:
				F=0
				for(I,J)in((1,0),(-1,0),(0,1),(0,-1)):
					B,C=G+I,E+J
					if B<0 or C<0 or B>=len(A)or C>=len(A[0])or A[B][C]!=5:F+=1
				D[E]=(2,4,1)[F]
	return A
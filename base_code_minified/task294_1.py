def p(A):
	F,G=len(A),len(A[0])
	for B in range(F):
		for C in range(G):
			if A[B][C]==5 and(B==0 or A[B-1][C]!=5)and(C==0 or A[B][C-1]!=5):
				D=1
				while B+D<F and A[B+D][C]==5:D+=1
				E=1
				while C+E<G and A[B][C+E]==5:E+=1
				for H in range(B+1,B+D-1):
					for I in range(C+1,C+E-1):
						if A[H][I]==5:A[H][I]=2
	return A
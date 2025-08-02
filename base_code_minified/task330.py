def p(A):
	K=len(A)
	for(H,I)in enumerate(A):
		for(J,L)in enumerate(I):
			if L==5:
				B=[(H,J)];A[H][J]=0
				for(F,G)in B:
					for C in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=F+C[0],G+C[1]
						if 0<=D<K and 0<=E<len(I)and A[D][E]==5:A[D][E]=0;B+=[(D,E)]
				C=2 if len(B)==6 else 1
				for(F,G)in B:A[F][G]=C
	return A
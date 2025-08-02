def p(A):
	G=[[0]*len(A[0])for B in A];H,I=len(A),len(A[0])
	for B in range(H):
		for C in range(I):
			D=A[B][C]
			if D and(B<1 or A[B-1][C]!=D)and(C<1 or A[B][C-1]!=D):
				E=1
				while C+E<I and A[B][C+E]==D:E+=1
				F=1
				while B+F<H and A[B+F][C]==D:F+=1
				if E>1 and F>1 and all(A[B+F][C+G]==D for F in range(F)for G in range(E)):
					for J in range(F):
						for K in range(E):G[B+J][C+K]=D
	return G
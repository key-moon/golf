def p(A):
	for B in range(len(A)):
		for C in range(len(A[0])):
			if A[B][C]==5:
				D=B
				while D+1<len(A)and A[D+1][C]==5:D+=1
				E=C
				while E+1<len(A[0])and A[B][E+1]==5:E+=1
				for F in range(B,D+1):
					for G in range(C,E+1):
						if A[F][G]==5:A[F][G]=1 if F in(B,D)and G in(C,E)else 4 if F in(B,D)or G in(C,E)else 2
	return A
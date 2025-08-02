def p(A):
	F=len(A)
	for G in range(F):
		for H in range(F):
			if A[G][H]==5:
				E=[(G,H)];A[G][H]=0
				for(B,C)in E:
					for D in(1,-1):
						if 0<=B+D<F and A[B+D][C]==5:E+=[(B+D,C)];A[B+D][C]=0
						if 0<=C+D<F and A[B][C+D]==5:E+=[(B,C+D)];A[B][C+D]=0
				I=5-len(E)
				for(B,C)in E:A[B][C]=I
	return A
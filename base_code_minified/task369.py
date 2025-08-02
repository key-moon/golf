def p(A):
	I,J=len(A),len(A[0])
	for G in range(I):
		for H in range(J):
			if not A[G][H]:
				D=[(G,H)];A[G][H]=1
				for(B,C)in D:
					for(E,F)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
						if 0<=E<I and 0<=F<J and not A[E][F]:A[E][F]=1;D+=[(E,F)]
				K=4-len(D)
				for(B,C)in D:A[B][C]=K
	return A
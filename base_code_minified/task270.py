def p(A):
	E=[[0]*15 for A in[0]*15]
	for B in range(15):
		for C in range(15):
			F=A[B][C]
			if 0<F<3:
				E[B][C]=F;I=sorted([D for D in range(15)if A[B][D]>F and D<C],reverse=1)
				for(D,G)in enumerate(I):E[B][C-D-1]=A[B][G]
				J=sorted([D for D in range(15)if A[B][D]>F and D>C])
				for(D,G)in enumerate(J):E[B][C+D+1]=A[B][G]
				K=sorted([D for D in range(15)if A[D][C]>F and D<B],reverse=1)
				for(D,H)in enumerate(K):E[B-D-1][C]=A[H][C]
				L=sorted([D for D in range(15)if A[D][C]>F and D>B])
				for(D,H)in enumerate(L):E[B+D+1][C]=A[H][C]
	return E
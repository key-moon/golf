def p(A):
	from collections import Counter as E;F,G=len(A),len(A[0])
	for B in range(F):
		for C in range(G):
			if A[B][C]==0:H=[A[B+D][C+E]for D in(-1,0,1)for E in(-1,0,1)if D|E if 0<=B+D<F and 0<=C+E<G if A[B+D][C+E]];D=E(H).most_common();A[B][C]=D[1][0]if len(D)>1 else D[0][0]
	return A
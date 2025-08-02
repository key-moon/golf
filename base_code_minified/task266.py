def p(A):
	B,C=next((B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]==2);A[B][C]=0
	for(F,G,H)in((-1,-1,3),(-1,1,6),(1,1,7),(1,-1,8)):
		D,E=B+F,C+G
		if 0<=D<len(A)and 0<=E<len(A[0]):A[D][E]=H
	return A
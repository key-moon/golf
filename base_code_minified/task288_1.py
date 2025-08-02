def p(A):
	B=A[-1];F=min({*B}-{0},key=B.count);G=[A for(A,B)in enumerate(B)if B==F];H,I=G[0],G[-1];J=len(A)-2;K=len(A[0])
	for C in range(1,len(A)):
		D=J-C
		if D<0:break
		for E in(H-C,I+C):
			if 0<=E<K and A[D][E]==0:A[D][E]=F
	return A
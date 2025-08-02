def p(A):
	for B in range(1,min(len(A),len(A[0]))):
		C={}
		for D in range(0,len(A)-B+1,B):
			for E in range(0,len(A[0])-B+1,B):F=tuple(tuple(A[C][E:E+B])for C in range(D,D+B));C[F]=C.get(F,0)+1
		G=C.values()
		if len({*G})>1:H=min(G);return[list(A)for(A,B)in C.items()if B==H][0]
def p(A):
	G=max(A.count(8)for A in A);B=[A for(A,B)in enumerate(A)if B.count(8)==G]
	for(D,C)in enumerate(A):
		if any(A==8 for A in C):
			E=B[D%2]if len(B)>1 else B[0]
			if D>E:
				for(F,H)in enumerate(C):
					if H==0 and A[E][F]==8:C[F]=1
	return A
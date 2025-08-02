def p(A):
	D,E=next((A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==7);B=0
	while D+B<len(A)and A[D+B][E]==7:B+=1
	for C in range(B):
		F=E-B+C+1
		for G in range(F,E+B-C):A[D+C][G]=(8,7)[(C+G-F)%2]
	return A
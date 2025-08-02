def p(A):
	for B in A:
		try:C,E=next((B,A)for(B,A)in enumerate(B)if A)
		except:continue
		for D in range(len(B)-C):B[C+D]=[E,5][D&1]
	return A
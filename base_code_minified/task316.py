def p(A):
	E=[A for(B,A)in sorted((C,A)for B in A for(C,A)in enumerate(B)if A)];C=[]
	for B in range(3):D=E[B*3:B*3+3];C.append(((D[::-1]if B&1 else D)+[0]*3)[:3])
	return C
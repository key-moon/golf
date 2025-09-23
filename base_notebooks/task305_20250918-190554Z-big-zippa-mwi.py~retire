def p(j):
	A=len(j);B=[A for B in j for A in B if A]
	if not B:return j
	C=sorted(set(B));G=len(C);D=[[0]*A for B in[0]*A]
	for E in range(A):
		for F in range(A):D[E][F]=C[(E+F)%G]
	return D
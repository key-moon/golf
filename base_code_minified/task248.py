def p(A):
	B=len(A[0]);D=2*B-2;F=-9%D
	for E in range(10):C=(E+F)%D;A[E]=[(C<B and C or 2*B-2-C)==A for A in range(B)]
	return A
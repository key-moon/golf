def p(A):
	for(E,B)in enumerate(A):
		if 3 in B:C=E;D=B.index(3)
		if 4 in B:F=E;G=B.index(4)
	A[C][D]=0;A[C+(F>C)-(F<C)][D+(G>D)-(G<D)]=3;return A
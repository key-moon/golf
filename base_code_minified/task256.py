def p(A):
	for(B,E)in enumerate(A):
		if 2 in E:break
	C=E.count(2)
	for F in range(B):
		for D in range(C+B-F):A[F][D]=3
	for G in range(1,C):
		for D in range(C-G):A[B+G][D]=1
	return A
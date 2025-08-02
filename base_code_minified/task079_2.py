def p(A):
	D=max({A for B in A for A in B if A},key=lambda D:sum(A.count(D)for A in A));E=sum(A.count(D)for A in A)//3;F,G=len(A),len(A[0])
	for B in range(F-2):
		for C in range(G-2):
			H=sum(A[B+E][C+F]==D for E in(0,1,2)for F in(0,1,2))
			if H==E and all(A[B+E][C+F]in(0,D)for E in(0,1,2)for F in(0,1,2)):return[A[C:C+3]for A in A[B:B+3]]
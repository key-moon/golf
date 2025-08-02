def p(A):
	D=len(A);E=len(A[0])
	for G in range(1,D+1):
		if D%G:continue
		for H in range(1,E+1):
			if E%H:continue
			F=1
			for B in range(D):
				for C in range(E):
					if A[B][C]and A[B][C]!=A[B%G][C%H]:F=0;break
				if not F:break
			if F:break
		if F:break
	for B in range(D):
		for C in range(E):
			if not A[B][C]:A[B][C]=A[B%G][C%H]
	return A
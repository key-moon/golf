def p(a):
	D,E=len(a),len(a[0])
	while 1:
		C=0
		for A in range(D):
			for B in range(E):
				if a[A][B]==0:
					if A and B and a[A-1][B]==1 and a[A][B-1]==1 and a[A-1][B-1]==1:a[A][B]=2;C=1
					elif A and B<E-1 and a[A-1][B]==1 and a[A][B+1]==1 and a[A-1][B+1]==1:a[A][B]=2;C=1
					elif A<D-1 and B and a[A+1][B]==1 and a[A][B-1]==1 and a[A+1][B-1]==1:a[A][B]=2;C=1
					elif A<D-1 and B<E-1 and a[A+1][B]==1 and a[A][B+1]==1 and a[A+1][B+1]==1:a[A][B]=2;C=1
		if not C:break
	return a
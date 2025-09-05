def	p(j):
	C=range;c,E=len(j),len(j[0]);k={}
	for	B	in	C(c):
		for	l	in	C(E):
			if	j[B][l]:k[j[B][l]]=k.get(j[B][l],[]);k[j[B][l]].append((B,l))
	D=[A[:]for	A	in	j]
	for(a,A)in	k.items():
		if	len(A)==2:
			if	A[0][0]==A[1][0]:
				for	l	in	C(min(A[0][1],A[1][1]),max(A[0][1],A[1][1])+1):D[A[0][0]][l]=a
	for(a,A)in	k.items():
		if	len(A)==2:
			if	A[0][1]==A[1][1]:
				for	B	in	C(min(A[0][0],A[1][0]),max(A[0][0],A[1][0])+1):D[B][A[0][1]]=a
	return	D
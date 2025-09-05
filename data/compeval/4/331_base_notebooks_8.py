def	p(j,A=enumerate):
	c=[]
	for(C,k)in	A(j):
		for(D,l)in	A(k):
			if	j[C][D]==1:c+=[[C,D]]
	for	E	in	c:
		a,B=E
		if	a>0:j[a-1][B]=2
		if	a<9:j[a+1][B]=8
		if	B>0:j[a][B-1]=7
		if	B<9:j[a][B+1]=6
	return	j